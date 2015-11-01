#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

# It is called by run_reconstruction_SPECT_PSF.sh etc and assumed that
# certain par files and input data are available in the current directory


echo running OSEM with PSF
OSMAPOSL OSEMPSF.par > OSEMPSF.log 2>&1

echo filtering the end result
postfilter filtered_OSEMPSF_240.hv OSEMPSF_240.hv postfilter_Gaussian.par > postfilter_OSEMPSF.log 2>&1

echo running OSSPS with PSF
OSSPS OSSPSPSF_QuadraticPrior.par > OSSPSPSF.log 2>&1

echo DONE
