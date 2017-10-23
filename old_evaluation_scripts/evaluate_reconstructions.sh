#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

echo subtract images EM and OSEM images
stir_subtract EM_diff.hv EMML_240.hv OSEM_240.hv

echo start amide with display
amide EM_diff.hv EMML_240.hv OSEM_240.hv&

echo subtracting images from 2 different subiterations
stir_subtract OSEM_diff.hv OSEM_240_continued_1.hv OSEM_240_continued_4.hv

echo start amide with display
amide OSEM_diff.hv OSEM_240_continued_1.hv OSEM_240_continued_4.hv&

if test -r OSEMPSF_240.hv
then
    echo subtract images OSEM with and without PSF images
    stir_subtract OSEMPSF_diff.hv OSEMPSF_240.hv OSEM_240.hv

    echo start amide with display
    amide OSEMPSF_diff.hv  OSEMPSF_240.hv OSEM_240.hv&
fi

echo DONE
