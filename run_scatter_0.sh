#! /bin/bash
export OMP_NUM_THREADS=1
for g in 1 2 ; do 
    # set some initial variable such that the rest of the script is
    # the same for all runs
    ctac=CTAC_g${g}.hv
    scatterparameters=scatter_correction_350keV.par
    output_suffix=_run0
  
    cd working_folder/GATE${g}
    stir_subtract -s input_g${g} my_prompts_g${g}.hs my_randoms_g${g}.hs
    cp ../../EX_scatter/* . 
    # run scatter in a subdirectory
    mkdir -p scatter${output_prefix}
    cd scatter${output_prefix}
    endN=3 ATTEN_IMAGE=../${ctac} scatterpar=../${scatterparameters} ../estimate_scatter.sh ../${ctac} ../input_g${g}.hs ../scatter_template.hs ../my_acfs_g${g}.hs ../my_norm_g${g}.hs
    INPUT=atten_corr_seg0_scatter_corrected_data_3.hs \
	 OUTPUT=FBP_recon_with_scatter_correction FBP2D ../FBP2D_full.par
    # copy to main directory with results
    stir_math -s ../scatter_estimate${output_suffix}.hs scatter_estimate_3.hs
  stir_math ../FBP_recon_with_scatter_correction${output_suffix}.hv FBP_recon_with_scatter_correction.hv
  cd ../../..
done

echo DONE
