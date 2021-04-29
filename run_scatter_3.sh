#! /bin/bash
# almost a copy of run_scatter0.sh
# The only different is the use of a wrong attenuation file
set -e # exit on error
trap "echo ERROR in $0. Rerun with 'bash -vx $0' to debug" ERR

## scatter settings
export num_scat_iters=3
## recon settings during scatter estimation
# adjust for your scanner (needs to divide number of views/4 as usual)
export scatter_recon_num_subsets=4
# keep num_scatter_iters*scatter_recon_num_subiterations relatively small as everything is at low resolution
export scatter_recon_num_subiterations=7

for g in 1 2 ; do 
    # set some initial variable such that the rest of the script is
    # the same for all runs
    ctac=wrong_CTAC.hv
    output_suffix=_run3
  
    cd working_folder/GATE${g}
    cp -rp ../../EX_scatter/* . 
    export scatter_pardir=${PWD}/scatter_estimation_par_files
    # run scatter in a subdirectory
    mkdir -p scatter${output_suffix}
    cd scatter${output_suffix}

    ## filenames for input
    export sino_input=../my_prompts_g${g}.hs
    export atnimg=../${ctac}
    export NORM=../my_norm_g${g}.hs
    export randoms3d=../my_randoms_g${g}.hs
    ## filenames for output
    export acf3d=my_acf_g${g}.hs
    export scatter_prefix=scatter_g${g}
    export total_additive_prefix=addsino_g${g}
    # internal scatter variables. ignore
    export mask_projdata_filename=mask_g${g}.hs
    export mask_image=mask_image_g${g}.hv

    echo "compute attenuation correction factors"
    if [ -r ${acf3d} ]; then
        echo "Re-using existing ${acf3d}"
    else
        calculate_attenuation_coefficients --ACF ${acf3d} ${atnimg} ${sino_input}
    fi

    echo "Estimating scatter"
    estimate_scatter $scatter_pardir/scatter_estimation.par >& estimate_${scatter_prefix}.log

    echo "Precorrect data for FBP"
    INPUT=${sino_input} OUTPUT=precorrected_g${g}.hs \
         MULTFACTORS=../my_multfactors_g${g}.hs \
         ADDSINO=${total_additive_prefix}_${num_scat_iters}.hs \
         correct_projdata ../correct_projdata.par
    echo "Running FBP"
    INPUT=precorrected_g${g}.hs \
	 OUTPUT=FBP_recon_with_scatter_correction FBP2D ../FBP2D_full.par

    # copy to main directory with results
    stir_math -s ../scatter_estimate${output_suffix}.hs ${scatter_prefix}_${num_scat_iters}.hs
  stir_math ../FBP_recon_with_scatter_correction${output_suffix}.hv FBP_recon_with_scatter_correction.hv
  cd ../../..
done

echo DONE
