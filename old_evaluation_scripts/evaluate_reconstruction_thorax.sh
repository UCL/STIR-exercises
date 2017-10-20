#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

cd working_folder/single_slice/

../../evaluate_reconstructions.sh

cd ../..

echo DONE
