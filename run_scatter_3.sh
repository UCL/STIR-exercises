for g in 1 2 ; do 
cd working_folder/GATE${g}
stir_subtract -s input_g${g} my_prompts_g${g}.hs my_randoms_g${g}.hs
cp ../../EX_scatter/* . 
cp ../*g${g}*v .
calculate_attenuation_coefficients --ACF my_acfs_g${g}.hs wrong_CTAC.hv template_sinogram.hs
endN=3 ATTEN_IMAGE=wrong_CTAC.hv scatterpar=scatter_correction_350keV.par ./estimate_scatter.sh wrong_CTAC.hv input_g${g}.hs scatter_template.hs my_acfs_g${g}.hs my_norm_g${g}.hs 
cd ../.. 
done

