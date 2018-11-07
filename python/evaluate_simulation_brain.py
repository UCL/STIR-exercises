# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for display the results of the brain simulation

The current script reads results from the simulation and displays them.

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulation_brain.sh

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
image=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('emission.hv'));
mu_map=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('attenuation.hv'));
#%% bitmap display of images
slice=7;
fig=plt.figure();
ax=plt.subplot(1,2,1);
plt.imshow(image[slice,:,:,]);
plt.colorbar();
plt.axis('off');
ax.set_title('emission image');

ax=plt.subplot(1,2,2);
plt.imshow(mu_map[slice,:,:,]);
plt.colorbar();
plt.axis('off');
ax.set_title('attenuation image');

fig.savefig('input_images.png')

#%% read in sinograms
# prompts (i.e. all counts) including trues and randoms)
prompts=to_numpy(stir.ProjData.read_from_file('my_prompts.hs'));
# scatter (zero for the brain simulation)
scatter=to_numpy(stir.ProjData.read_from_file('my_scatter.hs'));
# randoms (constant)
randoms=to_numpy(stir.ProjData.read_from_file('my_randoms.hs'));
#%% A note on projection data sizes
# In STIR Python, projection data after conversion to numpy is currently always a 3D array. This
# simulation is of an acquisition in "2D" mode, but with several rings of detectors.
# In that case, the projection  data has size num_sinograms x num_views x num_tangential_positions.
# In "3D" acquisition mode, the situation is more complicated. Effectively all "segments"
# are concatenated. You can ignore this terminology now, or check it out at
# http://stir.sourceforge.net/documentation/STIR-glossary.pdf
prompts.shape
#%% Display bitmaps of a middle sinogram
# Note that scatter is zero in this brain simulation
fig=plt.figure()
ax=plt.subplot(1,3,1);
plt.imshow(prompts[5,:,:,]);
plt.clim(0,prompts.max())
ax.set_title('Prompts');
plt.axis('off');
plt.colorbar()

ax=plt.subplot(1,3,2);
plt.imshow(scatter[5,:,:,]);
plt.clim(0,scatter.max());
ax.set_title('scatter');
plt.axis('off');
plt.colorbar()

ax=plt.subplot(1,3,3);
plt.imshow(randoms[5,:,:,]);
plt.clim(0,randoms.max());
ax.set_title('randoms');
plt.axis('off');
plt.colorbar()

fig.savefig('sinogram_bitmaps.png')

#%% Display central horizontal profiles through the sinogram
fig=plt.figure()
#plt.hold(True)
plt.plot(prompts[5,64/2,:],'b');
plt.plot(scatter[5,64/2,:],'c');
plt.plot((scatter+randoms)[5,64/2,:],'g');
plt.legend(('prompts','scatter', 'scatter+randoms'));

fig.savefig('sinogram_profiles.png')

#%%  Display some different views in an a movie
import matplotlib.animation as animation
bitmaps=[]
fig=plt.figure()
for view in range(0,64,4):
    bitmap=plt.imshow(prompts[:,view,:,]);
    plt.clim(0,prompts.max())
    #plt.set_title('Prompts view %d');
    plt.axis('off');
    bitmaps.append([bitmap])

ani = animation.ArtistAnimation(fig, bitmaps, interval=100, blit=True, repeat_delay=1000)

#%% close all plots
plt.close('all')
