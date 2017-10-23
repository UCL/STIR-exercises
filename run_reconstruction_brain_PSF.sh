#! /bin/sh

echo "updating working_folder/brain"
rsync -auCv EX_reconstruction/ working_folder/brain

cd working_folder/brain/

../../run_reconstructions_PSF.sh

cd ../..
