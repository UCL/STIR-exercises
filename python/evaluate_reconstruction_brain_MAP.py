# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for displaying the results of the brain reconstruction.

The current script reads results from the simulation and displays them.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulation_brain.sh
    ./run_reconstruction_brain.sh
    ./run_reconstruction_brain_MAP.sh
    
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
#%% Read in images
# OSL_QP_240.hv is the output of the One Step Late algorithm with a Quadratic Prior, 240 subiterations
# OSSPS_QP_240.hv is the output of the relaxed OSSPS algorithm with a Quadratic Prior, 240 subiterations
# "High" means a 10 times higher penalty
OSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240.hv'));
OSLQP240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSL_QP_240.hv'));
OSSPSQP240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSSPS_QP_240.hv'));
OSLQPLow240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSL_QP_Low_240.hv'));
OSSPSQPLow240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSSPS_QP_Low_240.hv'));
OSLQPHigh240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSL_QP_High_240.hv'));
OSSPSQPHigh240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSSPS_QP_High_240.hv'));

#%% bitmap display of images OSEM vs OSL vs OSSPS
maxforplot=OSEM240.max();
# pick central slice
slice=numpy.int(OSEM240.shape[0]/2);
#%%
plt.figure();
ax=plt.subplot(1,4,1);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM\n240 subiters.');

ax=plt.subplot(1,4,2);
plt.imshow(OSLQP240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSL');

ax=plt.subplot(1,4,3);
plt.imshow(OSSPSQP240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSSPS');


diff=OSLQP240-OSSPSQP240;
ax=plt.subplot(1,4,4);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/10,maxforplot/10)
plt.colorbar();
plt.axis('off');
ax.set_title('OSL - OSSPS');

#%% Display central horizontal profiles through the image
plt.figure()
# pick central line
row=numpy.int(OSEM240.shape[1]/2);
#plt.hold(True)
plt.plot(OSEM240[slice,row,:],'b');
plt.plot(OSLQP240[slice,row,:],'c');
plt.plot(OSSPSQP240[slice,row,:],'r');
plt.legend(('OSEM240','OSL','OSSPS'));

#%% bitmap display of OSSPS images for different penalties
fig=plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(OSSPSQPLow240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Low penalty');

ax=plt.subplot(1,3,2);
plt.imshow(OSSPSQP240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Medium penalty');

ax=plt.subplot(1,3,3);
plt.imshow(OSSPSQPHigh240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('High penalty');

#%% bitmap display of OSL vs OSSPS images for high penalty
# This might be surprising. What happened here?

plt.figure();
ax=plt.subplot(1,2,1);
plt.imshow(OSLQPHigh240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSL high penalty');

ax=plt.subplot(1,2,2);
plt.imshow(OSSPSQPHigh240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSSPS high penalty');
