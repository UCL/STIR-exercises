#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

# It is called by run_reconstruction_brain.sh etc and assumed that
# certain par files and input data are available in the current directory

echo "running EMML 240 iterations (this might take a while)"
OSMAPOSL EMML.par > EMML.log 2>&1

echo filtering the end result
postfilter filtered_EMML_240.hv EMML_240.hv postfilter_Gaussian.par > postfilter_EMML.log 2>&1

echo running OSEM 240 subiterations
OSMAPOSL OSEM.par > OSEM.log 2>&1

echo filtering the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1

echo continue OSEM from 240 iterations onwards
OSMAPOSL OSEMcont.par > OSEMcont.log 2>&1

echo running OSEM with PSF
OSMAPOSL OSEMPSF.par > OSEMPSF.log 2>&1

echo filtering the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1

