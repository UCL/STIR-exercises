#! /bin/sh
# An example script to do a simplistic analytic simulation
# Zero scatter, image-based blurring
#
#  Copyright (C) 2011 - 2011-01-14, Hammersmith Imanet Ltd
#  Copyright (C) 2011-07-01 - 2011-08-23, Kris Thielemans
#  Copyright (C) 2013-2014 University College London
#  This file is part of STIR.
#
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  See STIR/LICENSE.txt for details
#      
# Author Kris Thielemans
# 

if [ $# -ne 3 ]; then
  echo "Usage: `basename $0` emission_image attenuation_image template_sino"
  echo "Creates my_prompts.hs  my_multfactors.hs  my_additive_sinogram.hs "
  echo "and some other intermediate files"
  exit 1
fi

emission_image=$1
atten_image=$2
template_sino=$3

echo "===  create line integrals"
# Call forward_project to compute line integrals
forward_project my_line_integrals.hs ${emission_image}  ${template_sino} forward_projector_PSF.par > my_create_line_integrals.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running forward_project. Check my_create_line_integrals.log"; exit 1; 
fi

echo "===  create ACFs"
# currently need to pre-blur as we still can't pass a forward_project.par file
postfilter smoothed_atten_image.hv ${atten_image} postfilter_Gaussian.par > my_smooth_atten_image.log 2>&1 
calculate_attenuation_coefficients --ACF my_acfs.hs smoothed_atten_image.hv ${template_sino} > my_create_acfs.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running calculate_attenuation_coefficients. Check my_create_acfs.log"; exit 1; 
fi

echo "===  create normalisation factors"
# right now, just use a constant sinogram 
# (all bins set to 3.4 here, just to check if it's handled properly in the script)
stir_math -s --including-first \
         --times-scalar 0 --add-scalar 3.4 \
         my_norm.hs my_acfs.hs > my_stir_math_1.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running stir_math for norm"; exit 1; 
fi

echo "===  multiply ACF and norm"
stir_math -s --mult my_multfactors.hs my_norm.hs my_acfs.hs  > my_stir_math_2.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running stir_math for multiplying norm and ACFs"; exit 1; 
fi



echo "===  create constant randoms background"
# TODO compute sensible randoms-to-true background here
stir_math -s --including-first \
         --times-scalar 0 --add-scalar 10 \
         my_randoms.hs my_line_integrals.hs  > my_stir_math_3.log 2>&1
# we divide by the norm here to put some efficiency pattern on the data.
# this isn't entirely accurate as a "proper" norm contains geometric effects
# which shouldn't be in the randoms, but this is supposed to be a "simple" simulation :-;
stir_divide -s --accumulate \
         my_randoms.hs my_norm.hs  > my_stir_math_4.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running stir_math"; exit 1; 
fi


echo "===  create scatter"
# we could just use zero scatter
stir_math -s --including-first \
         --times-scalar 0 --add-scalar 0 \
         my_scatter.hs my_line_integrals.hs  > my_stir_math_5.log 2>&1

echo "===  create additive sinogram for reconstruction"
# model is
#   data = 1/(ACF*norm) * ( fwd(image) + additive_sinogram)
#
# Therefore, we need (randoms+scatter)  multiplied by ACF and norm 
stir_math -s   my_additive_sinogram.hs  my_randoms.hs my_scatter.hs  > my_stir_math_6.log 2>&1
stir_math -s --mult --accumulate  my_additive_sinogram.hs my_multfactors.hs  > my_stir_math_7.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running stir_math for additive sinogram"; exit 1; 
fi

echo "===  create prompts"
stir_math -s my_prompts.hs my_line_integrals.hs my_additive_sinogram.hs   > my_stir_math_8.log 2>&1
stir_divide -s --accumulate  my_prompts.hs my_multfactors.hs  > my_stir_math_9.log 2>&1

echo "===  create zero sinogram"
# for convenience of the scripts
stir_math -s --including-first \
         --times-scalar 0 \
         my_zeros.hs my_line_integrals.hs  > my_stir_math_10.log 2>&1

echo "Done creating simulated data"
