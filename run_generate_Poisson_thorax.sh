#! /bin/sh -e

echo "updating working_folder/single_slice"
rsync -auCv EX_reconstruction/ working_folder/single_slice

cd working_folder/single_slice/

../../run_generate_Poisson.sh $*

cd ../..
