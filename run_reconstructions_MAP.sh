#! /bin/sh -e

# This script does everything in one go. You might want to execute the steps one by one.

# It is called by run_reconstruction_brain_MAP.sh etc and assumed that
# certain par files and input data are available in the current directory

# check if initial image present
if [ ! -r OSEM_24.hv ]; then
   echo 'Are you sure you ran the non-MAP reconstructions already?'
   exit 1
fi

echo "running OS-OSL"
OSMAPOSL OSMAPOSL_QuadraticPrior.par > OSL_QP.log 2>&1

echo "running OSSPS"
OSSPS OSSPS_QuadraticPrior.par > OSSPS_QP.log 2>&1

echo "running OS-OSL with higher penalty"
OSMAPOSL OSMAPOSL_QuadraticPriorHigh.par > OSL_QP_High.log 2>&1

echo "running OSSPS with higher penalty"
OSSPS OSSPS_QuadraticPriorHigh.par > OSSPS_QP_High.log 2>&1

echo "running OS-OSL with lower penalty"
OSMAPOSL OSMAPOSL_QuadraticPriorLow.par > OSL_QP_Low.log 2>&1

echo "running OSSPS with lower penalty"
OSSPS OSSPS_QuadraticPriorLow.par > OSSPS_QP_Low.log 2>&1

echo DONE
