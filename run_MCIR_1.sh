#! /bin/sh -e

# copy data to working_folder/noMC
mkdir -p working_folder/noMC
cp EX_motion/* working_folder/noMC
cd working_folder/noMC
cp ../GATE1/*s .
cp ../GATE2/*s .

# make noMC.par by changing some names in MCIR_template.par
# to the specific case needed here
# To do no motion correction, we use a trick here: use zero deformation fields.
# This is actually a waste of CPU time (it would be better to add the gates)
# but let's keep it simple...
sed -e s/INPUTFILE/my_prompts/ -e s/NORMALIZATION/my_multfactors/ -e s/SENSOFILE/sens.hv/ -e s/ADDITIVE/my_additive_sinogram/ -e s/MOTIONFILE/zero_motion/ -e s/MOTIONINVFILE/zero_motion/ -e s/OUTPUTFILE/noMC/ MCIR_template.par > noMC.par

# Run OSMAPOSL with parameters without motion correction
OSMAPOSL noMC.par > noMC.log  2>&1

echo "output images are called noMC_16.hv etc (located in `pwd`)"

echo "you could now rerun OSMAPOSL by editing noMC.par and changing some parameters"

echo "Done"

