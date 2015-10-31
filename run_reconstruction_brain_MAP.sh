#! /bin/sh -e

#cp EX_reconstruction/* working_folder/brain/
echo "updating working_folder/brain"
rsync -auCv EX_reconstruction/ working_folder/brain/

cd working_folder/brain/

../../run_reconstructions_MAP.sh

cd ../..
