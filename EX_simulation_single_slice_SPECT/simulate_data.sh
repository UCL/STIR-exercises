#! /bin/sh
# An example script to do a simplistic analytic simulation
# Zero scatter, image-based blurring
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
# Call forward_project
forward_project my_sim.hs ${emission_image}  ${template_sino} forward_projector_SPECT.par > my_fwd.log 2>&1
if [ $? -ne 0 ]; then 
  echo "ERROR running forward_project. Check my_fwd.log"; exit 1; 
fi

echo "===  add noise"
poisson_noise my_noisy_data.hs my_sim.hs 1 1

echo "Done creating simulated data"
