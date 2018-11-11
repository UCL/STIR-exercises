#! /bin/sh

# cp EX_reconstruction_SPECT/* working_folder/single_slice_SPECT
echo "updating working_folder/single_slice_SPECT"
rsync -auCv EX_reconstruction_SPECT/ working_folder/single_slice_SPECT

cd working_folder/single_slice_SPECT/

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
