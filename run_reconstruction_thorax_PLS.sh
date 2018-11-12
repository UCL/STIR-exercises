#! /bin/sh -e

#cp EX_reconstruction/* working_folder/single_slice/
echo "updating working_folder/single_slice"
rsync -auCv EX_reconstruction/ working_folder/single_slice/

cd working_folder/single_slice/

echo "Creating anatomical image from attenuation image (with appropriate voxel size)"
zoom_image --template ground_truth.hv anatomical_image.hv CTAC.hv

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
