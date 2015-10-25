for g in 1 2 ; do 
cd working_folder/GATE${g}
stir_subtract -s input_g${g} my_prompts_g${g}.hs my_randoms_g${g}.hs
cp ../../EX_scatter/* . 
endN=3 ATTEN_IMAGE=CTAC_g${g}.hv scatterpar=scatter_correction_425keV.par ./estimate_scatter.sh CTAC_g${g}.hv input_g${g}.hs scatter_template.hs my_acfs_g${g}.hs my_norm_g${g}.hs 
cd ../.. 
done

