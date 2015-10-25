
copy EX_reconstruction\* working_folder\single_slice

cd working_folder/single_slice/

echo run OSL
OSMAPOSL OSMAPOSL_QuadraticPrior.par > OSL_QP.log 2>&1

echo run OSSPS
OSSPS OSSPS_QuadraticPrior.par > OSSPS_QP.log 2>&1

start amide OSEM_240.hv filtered_OSEM_240.hv OSL_QP_240.hv OSSPS_QP_240.hv 

cd ..\..
