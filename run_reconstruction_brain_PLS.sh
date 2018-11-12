#! /bin/sh -e

#cp EX_reconstruction/* working_folder/brain/
echo "updating working_folder/brain"
rsync -auCv EX_reconstruction/ working_folder/brain/

cd working_folder/brain/

echo "Creating anatomical image from T1 (with appropriate voxel size)"
zoom_image --template ground_truth.hv anatomical_image.hv T1.hv

if ../../run_reconstructions_PLS.sh
then
    : # everything ok
else
    echo "Something went wrong."
    echo "If you don't know what, you might need to check the most recent log file in"
    echo "  `pwd`"
    exit 1
fi

cd ../..
