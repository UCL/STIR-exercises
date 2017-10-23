#! /bin/sh

echo "updating working_folder/single_slice_SPECT"
rsync -auCv EX_reconstruction_SPECT/ working_folder/single_slice_SPECT

cd working_folder/single_slice_SPECT/

../../run_generate_Poisson.sh $*

cd ../..
