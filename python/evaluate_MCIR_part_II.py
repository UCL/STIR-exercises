# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for displaying and comparing results of motion correction versus no motion correction.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulations_thorax.sh
    ./run_MCIR_0.sh
    ./run_MCIR_2.sh
    ./run_MCIR_3.sh

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
#%% read in images
MCIR=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('working_folder/MCIR/MCIR_64.hv'));
avAC=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('working_folder/MCIR/avAC/MCIR_64.hv'));
g1AC=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('working_folder/MCIR/g1AC/MCIR_64.hv'));
Original=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EX_simulation/FDG_g1.hv'));
#%% bitmap display of images
# pick central slice
slice=numpy.int(MCIR.shape[0]/2);
fig=plt.figure();

maxforplot=MCIR.max()/500;
ax=plt.subplot(1,3,1);
plt.imshow(MCIR[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plt.axis('off');
ax.set_title('MCIR');

ax=plt.subplot(1,3,2);
plt.imshow(avAC[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plt.axis('off');
ax.set_title('AverageAC');

ax=plt.subplot(1,3,3);
plt.imshow(g1AC[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plt.axis('off');
ax.set_title('Gate1-AC');

fig.savefig('MCIR_with_atten_mismatch_bitmaps.png')
#%% Display difference images
fig=plt.figure();
diff1=Original-MCIR;
ax=plt.subplot(1,3,1);
plt.imshow(diff1[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('Correct AC Diff');

diff2=Original-avAC;
ax=plt.subplot(1,3,2);
plt.imshow(diff2[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('AvAC Diff');

diff3=Original-g1AC;
ax=plt.subplot(1,3,3);
plt.imshow(diff3[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('g1AC Diff');

fig.savefig('MCIR_with_atten_mismatch_diff_bitmaps.png')

#%% Display central horizontal profiles through the image
# pick a line close to central line
row=numpy.int(MCIR.shape[1]/2+3);

fig=plt.figure()
plt.plot(MCIR[slice,row,:],'b');
#plt.hold(True)
plt.plot(avAC[slice,row,:],'c');
plt.plot(g1AC[slice,row,:],'r');
plt.legend(('MCIR','avAC','g1AC'));

#%% close all plots
plt.close('all')
