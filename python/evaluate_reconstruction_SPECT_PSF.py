# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for displaying the results of the brain reconstruction.

The current script reads results from the simulation and displays them.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulation_SPECT.sh
    ./run_reconstruction_SPECT.sh
    ./run_reconstruction_SPECT_MAP.sh
    ./run_reconstruction_SPECT_PSF.sh
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
os.chdir('working_folder/single_slice_SPECT')
#%% Read in images
# OSSPS_QP_240.hv is the output of the relaxed OSSPS algorithm with a Quadratic Prior, 240 subiterations
# "PSF" means that PSF modelling was enabled during the reconstruction
ground_truth_image=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('emission.hv'));
OSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240.hv'));
OSSPSQP240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSSPS_QP_240.hv'));
OSEMPSF240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEMPSF_240.hv'));
OSSPSPSFQP240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSSPSPSF_QP_240.hv'));

#%% find max and slice number
maxforplot=OSEMPSF240.max();
# pick central slice
slice=numpy.int(OSEM240.shape[0]/2);
#%% bitmap display of images OSEM vs OSL vs OSSPS
fig=plt.figure();
ax=plt.subplot(2,2,1);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM\n240 subiters.');

ax=plt.subplot(2,2,2);
plt.imshow(OSSPSQP240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSSPS');

ax=plt.subplot(2,2,3);
plt.imshow(OSEMPSF240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM with PSF\n240 subiters.');


ax=plt.subplot(2,2,4);
plt.imshow(OSSPSPSFQP240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSSPS with PSF');


plt.savefig('PSF_bitmaps.png')
#%% Display horizontal profiles through lesion
fig=plt.figure()
row=67;
#plt.hold(True)
plt.plot(ground_truth_image[slice,row,:],'r');
plt.plot(OSEM240[slice,row,:],'b');
plt.plot(OSSPSQP240[slice,row,:],'c');
plt.plot(OSEMPSF240[slice,row,:],'m.-');
plt.plot(OSSPSPSFQP240[slice,row,:],'g.-');
plt.legend(('ground truth','OSEM240','OSSPS', 'OSEM with PSF', 'OSSPS with PSF'));

plt.savefig('PSF_profiles.png')
