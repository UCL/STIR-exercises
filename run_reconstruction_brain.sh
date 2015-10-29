#! /bin/sh -e

cp EX_reconstruction/* working_folder/brain/

cd working_folder/brain/

../../run_reconstructions.sh

cd ../..
