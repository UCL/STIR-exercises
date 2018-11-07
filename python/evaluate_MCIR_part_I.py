# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for displaying and comparing results of motion correction versus no motion correction.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulations_thorax.sh
    ./run_MCIR_0.sh
    ./run_MCIR_1.sh

Authors: Kris Thielemans & Harry Tsoumpas
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
#%% Read in images
MCIR=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('working_folder/MCIR/MCIR_64.hv'));
noMC=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('working_folder/noMC/noMC_64.hv'));
Original=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_simulation/FDG_g1.hv'));

#%% bitmap display of images
# pick central slice
slice=numpy.int(Original.shape[0]/2);

fig=plt.figure();
maxforplot=Original.max()/2;
ax=plt.subplot(1,3,1);
plt.imshow(Original[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plt.axis('off');
ax.set_title('Original');


ax=plt.subplot(1,3,2);
plt.imshow(MCIR[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plt.axis('off');
ax.set_title('MCIR');

ax=plt.subplot(1,3,3);
plt.imshow(noMC[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plt.axis('off');
ax.set_title('noMC');

fig.savefig('MCIR_vs_noMC_bitmaps.png')
#%% Display difference image
diff=MCIR-noMC;
fig=plt.figure()
ax=plt.subplot(1,1,1);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('diff');

fig.savefig('MCIR_vs_noMC_diff_bitmap.png')
#%% Display central horizontal profiles through the image
# pick a line close to central line
row=numpy.int(MCIR.shape[1]/2+3);

fig=plt.figure()
plt.plot(MCIR[slice,row,:],'b');
#plt.hold(True)
plt.plot(noMC[slice,row,:],'c');
plt.legend(('MCIR','noMC'));

#%% bitmap display of motion vectors 
# The motion files forward & backward
# First read in motion information from images
ForwardMotion_X=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_motion/motion_g1d1.hv'));
ForwardMotion_Y=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_motion/motion_g1d2.hv'));
ForwardMotion_Z=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_motion/motion_g1d3.hv'));
BackwardMotion_X=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_motion/motion_inv_g1d1.hv'));
BackwardMotion_Y=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_motion/motion_inv_g1d2.hv'));
BackwardMotion_Z=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_motion/motion_inv_g1d3.hv'));
#%% bitmaps showing forward motion images
# In the current demo, they are quite boring: the example motion is just a translation
maxforplot=ForwardMotion_Z.max();

# pick central slice
slice=numpy.int(ForwardMotion_X.shape[0]/2);

plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(ForwardMotion_X[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Forward_X');

ax=plt.subplot(1,3,2);
plt.imshow(ForwardMotion_Y[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Forward_Y');

ax=plt.subplot(1,3,3);
plt.imshow(ForwardMotion_Z[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Forward_Z');

#%% bitmaps showing backward motion images
maxforplot=BackwardMotion_Z.max();

# pick central slice
slice=numpy.int(BackwardMotion_X.shape[0]/2);

plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(BackwardMotion_X[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Backward_X');

ax=plt.subplot(1,3,2);
plt.imshow(BackwardMotion_Y[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Backward_Y');

ax=plt.subplot(1,3,3);
plt.imshow(BackwardMotion_Z[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('Backward_Z');

#%% close all plots
plt.close('all')
