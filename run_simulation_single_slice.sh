#! /bin/sh -e

mkdir -p working_folder/single_slice
cp EX_simulation_single_slice/* working_folder/single_slice
cd working_folder/single_slice
./simulate_data.sh emission.hv CTAC.hv template_sinogram.hs
rm -f  *zero* *scatter*

echo DONE
