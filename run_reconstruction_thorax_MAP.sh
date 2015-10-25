#! /bin/sh -e

cp EX_reconstruction/* working_folder/single_slice/

cd working_folder/single_slice/

# check if initial image present
if [ ! -r OSEM_24.hv ]; then
   echo 'Are you sure you ran the non-MAP reconstructions already?'
   exit 1
fi

echo run OSL
OSMAPOSL OSMAPOSL_QuadraticPrior.par > OSL_QP.log 2>&1

echo run OSSPS
OSSPS OSSPS_QuadraticPrior.par > OSSPS_QP.log 2>&1

amide *_240.hv&

cd ../..
