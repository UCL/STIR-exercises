#! /bin/sh -e

#cp EX_reconstruction/* working_folder/single_slice/
echo "updating working_folder/single_slice"
rsync -auCv EX_reconstruction/ working_folder/single_slice

cd working_folder/single_slice/

../../run_reconstructions_MAP.sh

cd ../..
