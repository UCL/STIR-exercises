#! /bin/sh -e

#cp EX_reconstruction/* working_folder/single_slice/
echo "updating working_folder/single_slice"
rsync -auCv EX_reconstruction/ working_folder/single_slice

cd working_folder/single_slice/
if test -r OSEM.par
then
if test -r OSEM_more_voxels.par
then
if test -r OSEM_more_voxels_more_rays.par
then
echo "Running reconstructions. Files are/will be in"
echo "   `pwd`"
OSMAPOSL OSEM.par > OSEM.log 2>&1
OSMAPOSL OSEM_more_voxels.par > OSEM_more_voxels.log 2>&1
OSMAPOSL OSEM_more_voxels_more_rays.par > OSEM_more_voxels_more_rays.log 2>&1
    : # everything ok
else
    echo "The parameter files are missing. Please, check"
    exit 1
fi
fi
fi

cd ../..
