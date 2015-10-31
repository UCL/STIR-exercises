#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

# It is called by run_reconstruction_brain.sh etc and assumed that
# certain par files and input data are available in the current directory

# running FBP, but need to know if PET or SPECT for precorrections
if test -r my_prompts.hs
then
    # PET
    echo "running precorrection and FBP"
    stir_math -s --mult norm_ac_prompts.hs my_prompts.hs my_multfactors.hs > precorrection.log 2>&1
    stir_subtract -s precorrected.hs norm_ac_prompts.hs my_additive_sinogram.hs >> precorrection.log 2>&1
else
    # SPECT
    # no precorrections
    echo "running FBP (without attenuation correction)"
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

echo continue OSEM from 240 iterations onwards
OSMAPOSL OSEMcont.par > OSEMcont.log 2>&1

echo running OSEM with PSF
OSMAPOSL OSEMPSF.par > OSEMPSF.log 2>&1

echo filtering the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1
