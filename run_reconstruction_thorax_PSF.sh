#! /bin/sh

echo "updating working_folder/single_slice"
rsync -auCv EX_reconstruction/ working_folder/single_slice

cd working_folder/single_slice/

if ../../run_reconstructions_PSF.sh
then
    : # everything ok
else
    echo "Something went wrong."
    echo "If you don't know what, you might need to check the most recent log file in"
    echo "  `pwd`"
    exit 1
fi

cd ../..
