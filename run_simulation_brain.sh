#! /bin/sh -e

mkdir -p working_folder/brain
cp EX_brain/* working_folder/brain
cd working_folder/brain
./make_images.sh
./simulate_data.sh emission.hv attenuation.hv template_sinogram.hs
#./simulate_data.sh emission.hv attenuation.hv template_sinogram.hs scatter_simulation.par scatter_template.hs
rm -f  *zero* *scatter_low* *line_integrals* *log pre*

echo DONE
