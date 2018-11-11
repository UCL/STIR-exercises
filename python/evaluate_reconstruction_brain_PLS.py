# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for display evaluation of reconstructions
using the Parallel Level Sets (PLS) prior.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulation_brain.sh
    ./run_reconstruction_brain.sh
    ./run_reconstruction_brain_PSF.sh
    ./run_reconstruction_brain_PLS.sh

This will use the existing data in the folder. The exercise gets more interesting
if you added noise to the data.

Author: Kris Thielemans
"""
#%% Initial imports
import numpy
import matplotlib.pyplot as plt
import stir
from stirextra import *
import os
#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir(os.getenv('STIR_exercises_PATH'))
#%% change directory to where the output files are
os.chdir('working_folder/brain')
#%% Read origin images
groundtruth=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('ground_truth.hv'));
anatomical=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('anatomical_image.hv'));

#%% variables for future display
maxforplot=groundtruth.max();
# pick central slice
slice=numpy.int(groundtruth.shape[0]/2)
#%% Display
plt.figure();

ax=plt.subplot(1,2,1);
plt.imshow(groundtruth[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('ground truth');

ax=plt.subplot(1,2,2);
plt.imshow(anatomical[slice,:,:,]);
plt.colorbar();
plt.axis('off');
ax.set_title('anatomical image');

#%% Read in images
# All reconstruction were run with 240 subiterations using OSL
# OSL_PLS_240.hv is the output with the PLS prior
# OSLPSF_PLS_240.hv is the output with the PLS prior when using resolution modelling
# We also read the OSEM imges with resolution modelling for comparison
OSEMPSF240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEMPSF_240.hv'));
OSLPSF240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSL_PLS_240.hv'));
OSLPLSPSF240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSLPSF_PLS_240.hv'));
#%% bitmap display of images 
plt.figure();

ax=plt.subplot(2,2,1);
plt.imshow(groundtruth[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('ground truth');

ax=plt.subplot(2,2,2);
plt.imshow(OSEMPSF240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM (with PSF)');

ax=plt.subplot(2,2,3);
plt.imshow(OSLPSF240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('PLS (no PSF)');

ax=plt.subplot(2,2,4);
plt.imshow(OSLPLSPSF240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('PLS (with PSF)');

#%% What now?
# You can change the parameters of the PLS prior (edit OSMAPOSLPSF_PLS.par)
