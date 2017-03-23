#! /bin/sh -e

mkdir -p working_folder
cd working_folder 
for g in 1 2 ; do 
cp ../EX_simulation/* ./
./simulate_data.sh FDG_g${g}.hv CTAC_g${g}.hv template_sinogram.hs scatter_simulation.par scatter_template.hs
stir_math -s my_acfs_g${g} my_acfs.hs
stir_math -s my_additive_sinogram_g${g} my_additive_sinogram.hs 
stir_math -s my_multfactors_g${g} my_multfactors.hs
stir_math -s my_prompts_g${g}  my_prompts.hs
stir_math -s my_norm_g${g}  my_norm.hs
stir_math -s my_randoms_g${g} my_randoms.hs
stir_math -s my_scatter_g${g} my_scatter.hs
mkdir -p GATE$g
rm -f *log my_zoomed* *.par *.sh
mv *g${g}.* GATE${g}/
rm -f  *.s *.hs  CTAC*v FDG*v
done

echo DONE
