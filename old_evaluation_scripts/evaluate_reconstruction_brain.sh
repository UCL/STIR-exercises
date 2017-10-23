#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

cd working_folder/brain/

../../old_evaluation_scripts/evaluate_reconstructions.sh

cd ../..

echo DONE
