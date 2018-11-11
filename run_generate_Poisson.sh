#! /bin/sh -e

if test $# -ne 1
then
    echo ""
    echo "ERROR: this script expects one numerical argument: the scaling_factor to use."
    exit 1
fi
scaling_factor=$1

# create a subdir with the original noiseless data
if test -d noiseless
then
    : # no need to do anything first
else
    echo "First copying all files to a 'noiseless' directory"
    mkdir noiseless
    cp *.* noiseless
fi

# find out if PET or SPECT data as they have a different name
if test -r my_prompts.hs
then
    data=my_prompts
else
    data=my_sim
fi

# now generate noise

seed=1

poisson_noise -p $data.hs noiseless/$data.hs $scaling_factor $seed
# echo "===  fixing SPECT headers"
# It appears that the data is written with a "PET" header, as opposed to SPECT.
# This is a bug in current STIR (a regression?).
# So we will have to fix this up by using the template and some fancy scripting
if [ $data = my_sim ]; then
    sed -e"s/name of data file :=.*/name of data file := $data.s/" noiseless/$data.hs > $data.hs
fi

# save it elsewhere
mkdir -p noise_$scaling_factor
cp $data.* noise_$scaling_factor

# finish

echo "Used a scaling factor $scaling_factor"
echo "Original noise-less data copied to sub-folder noiseless"
echo "Noisy data copied to sub-folder noise_$scaling_factor"
echo "Data in place is the noisy version"
echo ""
echo "Done"


       
