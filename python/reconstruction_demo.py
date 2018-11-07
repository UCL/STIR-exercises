# -*- coding: utf-8 -*-
"""
Demo of how to use STIR from python to reconstruct some data.

This currently relies on existing data and reconstruction parameter files, but would work
for any data that you have.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulation_brain.sh
    ./run_reconstruction_brain.sh
However, it is easy to adapt this to other data-sets.

Author: Kris Thielemans
"""
# Copyright 2012-06-05 - 2013 Kris Thielemans
# Copyright 2015, 2018 University College London

#%% Initial imports
import stir
import stirextra
import matplotlib.pyplot as plt
import os

#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir(os.getenv('STIR_exercises_PATH'))
#%% change directory to where the output files are
os.chdir('working_folder/brain')

#%% initialise reconstruction object
# we will do this here via a .par file 
recon=stir.OSMAPOSLReconstruction3DFloat('OSEM.par')
#%% check its parameters
# There's quite a few! Most of these are the default values.
# You could compare to the .par file.
print(recon.parameter_info());
#%% get initial image 
# Here we're using image size as set by the parameter file.
# You could read an image instead, and use that for initialisation.
target=recon.get_initial_data_ptr()
# we will just fill the whole array with 1 here
target.fill(1)

#%% run
s=recon.set_up(target);
recon.reconstruct(target);
#%% Display
plt.figure()
# extract to python for plotting
npimage=stirextra.to_numpy(target);
plt.imshow(npimage[10,:,:])
plt.show()
#%% save a copy
reconstructed=target.clone();
#%% Let's continue for a few more subiterations
# we could just use `set_num_subiterations`, but we will make
# sure that the subiteration counter increases such that selected subsets,
# filenames etc are correct.
previous_nsubiters=recon.get_subiteration_num()
recon.set_start_subiteration_num(previous_nsubiters)
recon.set_num_subiterations(previous_nsubiters+3)
recon.reconstruct(target);
# plot slice of final image
plt.figure()
plt.imshow(npimage[10,:,:])
plt.show()
# What now?
# You could check what other parameter files are available, check their content.
# Advanced topic would be to add some filtering between iterations for regularisation
