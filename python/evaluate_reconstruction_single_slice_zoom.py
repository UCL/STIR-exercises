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
os.chdir('working_folder/single_slice')
#%% Read in images
OSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240.hv'));
OSEMZ240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_240.hv'));
OSEMZ10R240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_240.hv'));
#%% find max and slice number for plots
maxforplot=OSEM240.max();
# pick central slice
slice=numpy.int(OSEM240.shape[0]/2);
#%% bitmap display of images OSEM vs OSEM zoomed
fig=plt.figure();
ax=plt.subplot(1,2,1);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.axis('off');
ax.set_title('OSEM240');

ax=plt.subplot(1,2,2);
plt.imshow(2*OSEMZ240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.axis('off');
ax.set_title('OSEM z2');

fig.savefig('OSEM_vs_OSEMx2zoom.png')
#%% bitmap display of images OSEM vs OSEM with half voxel size in each direction
fig=plt.figure();
ax=plt.subplot(2,2,1);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM 240');

ax=plt.subplot(2,2,2);
plt.imshow(2*OSEMZ240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEMz2 240');

ax=plt.subplot(2,2,3);
plt.imshow(2*OSEMZ10R240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEMz2 R10 240');

diff=OSEMZ240-OSEMZ10R240;
ax=plt.subplot(2,2,4);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('diff');

fig.savefig('OSEM_vs_OSEMx2zoom_bitmaps.png')
#%% Display central horizontal profiles through the image
# pick line through tumor
row=84;

fig=plt.figure()
plt.plot(OSEM240[slice,row,0:185],'b');
#plt.hold(True)
plt.plot(2*OSEMZ240[slice,2*row-1,0:369:2],'c');
plt.plot(2*OSEMZ10R240[slice,2*row-1,0:369:2],'r');
plt.legend(('OSEM240','OSEMx2zoom240','OSEMx2zoom10rays240'));

fig.savefig('OSEM_vs_OSEM2zoom_profiles.png')

for line in open("OSEM.log"):
 if "Total CPU" in line:
   print line

for line in open("OSEM_more_voxels.log"):
 if "Total CPU" in line:
   print line

for line in open("OSEM_more_voxels_more_rays.log"):
 if "Total CPU" in line:
   print line

#%% example code for seeing evaluation over iterations with OSEM, OSEM with zoom, OSEM with more rays 
# First read in all iterations
OSEM24=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_24.hv'));
OSEM48=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_48.hv'));
OSEM72=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_72.hv'));
OSEM96=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_96.hv'));
OSEM120=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_120.hv'));
OSEM144=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_144.hv'));
OSEM168=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_168.hv'));
OSEM192=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_192.hv'));
OSEM216=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_216.hv'));
OSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240.hv'));
OSEMZ10R24=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_24.hv'));
OSEMZ10R48=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_48.hv'));
OSEMZ10R72=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_72.hv'));
OSEMZ10R96=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_96.hv'));
OSEMZ10R120=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_120.hv'));
OSEMZ10R144=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_144.hv'));
OSEMZ10R168=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_168.hv'));
OSEMZ10R192=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_192.hv'));
OSEMZ10R216=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_216.hv'));
OSEMZ10R240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_zoom_10rays_240.hv'));

it = [24, 48, 72, 96, 120, 144, 168, 192, 216, 240];
#The location of the voxel is chosen to be in the lung lesion 
col=59;
colz=col*2;
rowz=2*row-1;
OSEMvalues = [OSEM24[slice,row,col], OSEM48[slice,row,col], OSEM72[slice,row,col], OSEM96[slice,row,col], OSEM120[slice,row,col], OSEM144[slice,row,col], OSEM168[slice,row,col], OSEM192[slice,row,col], OSEM216[slice,row,col], OSEM240[slice,row,col]];
OSEMZ10Rvalues = [2*OSEMZ10R24[slice,rowz,colz], 2*OSEMZ10R48[slice,rowz,colz], 2*OSEMZ10R72[slice,rowz,colz], 2*OSEMZ10R96[slice,rowz,colz], 2*OSEMZ10R120[slice,rowz,colz], 2*OSEMZ10R144[slice,rowz,colz], 2*OSEMZ10R168[slice,rowz,colz], 2*OSEMZ10R192[slice,rowz,colz], 2*OSEMZ10R216[slice,rowz,colz], 2*OSEMZ10R240[slice,rowz,colz]];
fig=plt.figure()
plt.plot(it, OSEMvalues, 'bo')
plt.plot(it, OSEMZ10Rvalues, 'ro')
plt.axis([0, 250, 40, 70])
plt.title('Image value over subiteration')
plt.legend(('OSEM','Zoomed OSEM'))
plt.show();


#%% close all plots
plt.close('all')
