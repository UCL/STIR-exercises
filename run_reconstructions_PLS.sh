#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

# It is called by run_reconstruction_brain_PLS.sh etc and assumed that
# certain par files and input data are available in the current directory

if test -r OSMAPOSL_PLS.par -a -r OSEM_24.hv
then
    echo "Running reconstructions. Files are/will be in"
    echo "   `pwd`"
else
    echo "Either OSMAPOSL_PLS.par or OSEM_24.hv is missing in the current directory."
    echo "Did you run the normal reconstruction scripts first?"
    echo "Alternatively, you might be executing this script directly as opposed to via"
    echo "run_reconstruction_brain_PLS.sh etc."
    echo "Aborting."
    exit 1
fi


echo "running OSMAPOSL with PLS (no PSF) 240 subiterations"
OSMAPOSL OSMAPOSL_PLS.par > OSMAPOSL_PLS.log 2>&1

echo "running OSMAPOSL with PLS (with PSF) 240 subiterations"
OSMAPOSL OSMAPOSLPSF_PLS.par > OSMAPOSLPSF_PLS.log 2>&1

echo DONE
