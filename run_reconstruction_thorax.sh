#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

cp EX_reconstruction/* working_folder/single_slice/

cd working_folder/single_slice/

echo running EMML 240 iterations (this might take a while)
OSMAPOSL EMML.par > EMML.log 2>&1
postfilter filtered_EMML_240.hv EMML_240.hv postfilter_Gaussian.par > postfilter_EMML.log 2>&1

echo running OSEM
OSMAPOSL OSEM.par > OSEM.log 2>&1

echo filtering the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1

echo subtract images EM and OSEM images
stir_subtract EM_diff.hv EMML_240.hv OSEM_240.hv

echo start amide with display
amide EM_diff.hv EMML_240.hv OSEM_240.hv&


echo continue OSEM from 240 iterations
OSMAPOSL OSEMcont.par > OSEMcont.log 2>&1

echo subtract images from 2 different subiterations
stir_subtract OSEM_diff.hv OSEM_240_continued_1.hv OSEM_240_continued_4.hv

echo start amide with display
amide OSEM_diff.hv OSEM_240_continued_1.hv OSEM_240_continued_4.hv&

echo running OSEM with PSF
OSMAPOSL OSEMPSF.par > OSEMPSF.log 2>&1

echo filter the end result
postfilter filtered_OSEM_240.hv OSEM_240.hv postfilter_Gaussian.par > postfilter_OSEM.log 2>&1

echo subtract images OSEM with and without PSF images
stir_subtract OSEMPSF_diff.hv OSEMPSF_240.hv OSEM_240.hv

echo start amide with display
amide OSEMPSF_diff.hv  OSEMPSF_240.hv OSEM_240.hv&

cd ../..
