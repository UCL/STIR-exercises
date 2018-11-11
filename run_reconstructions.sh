#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

# It is called by run_reconstruction_brain.sh etc and assumed that
# certain par files and input data are available in the current directory

if test -r FBP2D.par
then
    echo "Running reconstructions. Files are/will be in"
    echo "   `pwd`"
else
    echo "I do not find FBP2D.par in the current directory."
    echo "You might be executing this script directly as opposed to via"
    echo "run_reconstruction_brain.sh etc."
    echo "Aborting."
    exit 1
fi

# running FBP, but need to know if PET or SPECT for precorrections
if test -r my_prompts.hs
then
    # PET
    echo "running precorrection and FBP"
    stir_math -s --mult norm_ac_prompts.hs my_prompts.hs my_multfactors.hs > precorrection.log 2>&1
    stir_subtract -s precorrected.hs norm_ac_prompts.hs my_additive_sinogram.hs >> precorrection.log 2>&1
elif test -r my_sim.hs
then        
    # SPECT
    # no precorrections
    echo "running FBP (without attenuation correction)"
else
    echo "I find no data in the folder."
    echo "Expecting either my_prompts.hs or my_sim.hs."
    echo "Did you run the simulation?"
    echo "Aborting."
    exit 1
fi

# note: currently need 1 thread only
OMP_NUM_THREADS=1 FBP2D FBP2D.par > FBP2D.log 2>&1

echo "running EMML 240 iterations (this might take a while)"
OSMAPOSL EMML.par > EMML.log 2>&1

echo filtering the end result
postfilter filtered_EMML_240.hv EMML_240.hv postfilter_Gaussian.par > postfilter_EMML.log 2>&1

echo running OSEM 240 subiterations
OSMAPOSL OSEM.par > OSEM.log 2>&1

echo filtering the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1

echo "continue OSEM from 240 sub-iterations onwards, saving every sub-iteration"
OSMAPOSL OSEMcont.par > OSEMcont.log 2>&1

echo "continue EMML from 240 iterations onwards, saving every iteration"
OSMAPOSL EMMLcont.par > EMMLcont.log 2>&1

#echo running OSEM with PSF
#OSMAPOSL OSEMPSF.par > OSEMPSF.log 2>&1

echo filtering the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1

echo "Creating ground_truth.hv (with same voxel-size as the reconstruction)"
zoom_image --template OSEM_24.hv ground_truth.hv emission.hv
# rescale to STIR units used by the reconstruction
zoom=`../../print_zoom_ratio.py emission.hv OSEM_24.hv`
stir_math --including-first --accumulate --times-scalar $zoom --times-scalar $zoom ground_truth.hv

echo DONE
