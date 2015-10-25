#! /bin/sh -e

# copy data to working_folder/MCIR
mkdir -p working_folder/MCIR
cp EX_motion/* working_folder/MCIR
cd working_folder/MCIR
cp ../GATE1/*s .
cp ../GATE2/*s .

# make MCIR.par by changing some names in MCIR_template.par
# to the specific case needed here
sed -e s/INPUTFILE/my_prompts/ -e s/NORMALIZATION/my_multfactors/ -e s/SENSOFILE/sens.hv/ -e s/ADDITIVE/my_additive_sinogram/ -e s/MOTIONFILE/motion/ -e s/MOTIONINVFILE/motion_inv/ -e s/OUTPUTFILE/MCIR/ MCIR_template.par > MCIR.par
# Run OSMAPOSL with parameters for motion correction
OSMAPOSL MCIR.par > MCIR.log  2>&1

echo "output images are called MCIR_16.hv etc (located in `pwd`)"

# you could now rerun OSMAPOSL by editing MCIR.par and changing some parameters
