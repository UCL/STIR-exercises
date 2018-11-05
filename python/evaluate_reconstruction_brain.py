# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for displaying the results of the brain reconstruction.

The current script reads results from the simulation and displays them.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulation_brain.sh
    ./run_reconstruction_brain.sh

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
FBP=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('fbp_recon.hv'));
EMML240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EMML_240.hv'));
OSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240.hv'));
#OSEMPSF240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEMPSF_240.hv'));

filteredEMML240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('filtered_EMML_240.hv'));
filteredOSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('filtered_OSEM_240.hv'));
#%% find max and slice number for plots
maxforplot=EMML240.max();
# pick central slice
slice=numpy.int(EMML240.shape[0]/2);
#%% bitmap display of images FBP vs EMML
fig=plt.figure();
ax=plt.subplot(1,2,1);
plt.imshow(EMML240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('EMML240');

ax=plt.subplot(1,2,2);
plt.imshow(FBP[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('FBP');

fig.savefig('EMML_vs_FBP.png')
#%% bitmap display of images EMML vs OSEM
fig=plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(EMML240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('EMML240');

ax=plt.subplot(1,3,2);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM240');

diff=EMML240-OSEM240;
ax=plt.subplot(1,3,3);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('diff');

fig.savefig('EMML_vs_OSEM_bitmaps.png')
#%% Display central horizontal profiles through the image
# pick central line
row=numpy.int(OSEM240.shape[1]/2);

fig=plt.figure()
plt.plot(EMML240[slice,row,:],'b');
#plt.hold(True)
plt.plot(OSEM240[slice,row,:],'c');
plt.legend(('EMML240','OSEM240'));

fig.savefig('EMM_vs_OSEM_profiles.png')
#%% bitmap display of images EMML vs OSEM after postfiltering
# note: check postfilter_Gaussian.par for parameters used for the postfilter
maxforplot=filteredEMML240.max();
# pick central slice
slice=numpy.int(EMML240.shape[0]/2);

fig=plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(filteredEMML240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('EMML240\nfiltered');

ax=plt.subplot(1,3,2);
plt.imshow(filteredOSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM240\nfiltered');

diff=filteredEMML240-filteredOSEM240;
ax=plt.subplot(1,3,3);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('diff');

fig.savefig('EMML_vs_OSEM_postfiltered_bitmaps.png')
#%% example code for seeing evaluation over (sub)iterations with EMML and OSEM
# The reconstruction script runs EMML and OSEM for 240 (sub)iterations, saving 
# after every 24 (sub)iterations, i.e. image-updates.
# We can see what the difference is between after one image-update, or for OSEM
# after when full iteration (using all 8 subsets)
#
# First read in extra images
OSEM241=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240_continued_1.hv'));
OSEM242=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240_continued_2.hv'));
OSEM248=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240_continued_8.hv'));
EMML241=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EMML_240_continued_1.hv'));
EMML242=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EMML_240_continued_2.hv'));
EMML248=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EMML_240_continued_8.hv'));

#%% bitmaps showing images and differences
maxforplot=EMML240.max();

# pick central slice
slice=numpy.int(EMML240.shape[0]/2);

fig=plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM240');

ax=plt.subplot(1,3,2);
plt.imshow(OSEM241[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM241');

diff=OSEM241-OSEM240;
ax=plt.subplot(1,3,3);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('diff');

fig.savefig('EMML_vs_OSEM_update_bitmaps.png')
#%% Display central horizontal profiles through the image for EMML
# pick central line
row=numpy.int(EMML240.shape[1]/2);

fig=plt.figure()
plt.subplot(1,2,1)
#plt.hold(True)
plt.plot(EMML241[slice,row,:],'b');
plt.plot(EMML240[slice,row,:],'c');
plt.legend(('EMML241','EMML240'));

plt.subplot(1,2,2)
#plt.hold(True);
plt.plot((EMML241-EMML240)[slice,row,:],'b');
plt.plot((EMML242-EMML241)[slice,row,:],'k');
plt.plot((EMML248-EMML240)[slice,row,:],'r');
plt.legend(('iter 241 - iter 240', 'iter 242 - iter 241', 'iter 248 - iter 240'));
#%% Display central horizontal profiles through the image for OSEM

fig=plt.figure()
plt.subplot(1,2,1)
#plt.hold(True)
plt.plot(OSEM241[slice,row,:],'b');
plt.plot(OSEM240[slice,row,:],'c');
plt.legend(('OSEM241','OSEM240'));

plt.subplot(1,2,2)
#plt.hold(True);
plt.plot((OSEM241-OSEM240)[slice,row,:],'b');
plt.plot((OSEM242-OSEM241)[slice,row,:],'k');
plt.plot((OSEM248-OSEM240)[slice,row,:],'r');
plt.legend(('subiter 241 - subiter 240', 
    'subiter 242 - subiter 241', 'subiter 248 - subiter 240'));

#%% close all plots
plt.close('all')
