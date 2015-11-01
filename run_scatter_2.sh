echo "This exercise is currently broken."
exit 1
for g in 1 ; do 
cd working_folder/GATE${g}
stir_subtract -s input_g${g} my_prompts_g${g}.hs my_randoms_g${g}.hs
cp ../../EX_scatter/* . 
endN=3 ATTEN_IMAGE=CTAC_g${g}.hv scatterpar=scatter_correction_350keV.par ./estimate_scatter.sh CTAC_g${g}.hv input_g${g}.hs scatter_template.hs my_acfs_g${g}.hs my_norm_g${g}.hs 
cd ../.. 
done

cd working_folder/GATE2
cp ../GATE1/*s .
cp ../*g1*v .
endN=3 ATTEN_IMAGE=CTAC_g1.hv scatterpar=scatter_correction_350keV.par ./estimate_scatter.sh CTAC_g1.hv input_g1.hs scatter_template.hs my_acfs_g1.hs my_norm_g1.hs
 
echo DONE
