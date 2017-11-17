#! /bin/sh -e

mkdir -p working_folder/single_slice_SPECT
cp EX_simulation_single_slice_SPECT/* working_folder/single_slice_SPECT
cd working_folder/single_slice_SPECT
./simulate_data.sh emission.hv CTAC.hv template_sinogram.hs

echo DONE
