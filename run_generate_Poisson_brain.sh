#! /bin/sh -e

echo "updating working_folder/brain"
rsync -auCv EX_reconstruction/ working_folder/brain/

cd working_folder/brain/

../../run_generate_Poisson.sh $*

cd ../..
