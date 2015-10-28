# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for display the results of the brain simulation

The current script reads results from run_scatter0 and displays them comparing 
with the truth (i.e. simulation input and simulation scatter output)

Author: Kris Thielemans
"""
#%% Initial imports
import matplotlib.pyplot as plt
import stir
from stirextra import *
import os
#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir('/home/stir/stir-exercises')
#%% run simulation (if you haven't done it yet)
print(os.popen('./run_simulation_brain.sh').read())
#%% change directory to where the output files are
os.chdir('working_folder/brain')
#%% Read in images
image=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('emission.hv'));
mu_map=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('attenuation.hv'));
#%% bitmap display of images
slice=7;
plt.figure();
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

#%% read in sinograms
# prompts (i.e. all counts) including trues and randoms)
prompts=to_numpy(stir.ProjData.read_from_file('my_prompts.hs'));
# scatter (zero for the brain simulation)
scatter=to_numpy(stir.ProjData.read_from_file('my_scatter.hs'));
# randoms (constant)
randoms=to_numpy(stir.ProjData.read_from_file('my_randoms.hs'));
#%% Display bitmaps of a middle sinogram
maxforplot=prompts.max();

plt.figure()
ax=plt.subplot(1,3,1);
plt.imshow(prompts[5,:,:,]);
plt.clim(0,maxforplot)
ax.set_title('Prompts');
plt.axis('off');

ax=plt.subplot(1,3,2);
plt.imshow(scatter[5,:,:,]);
plt.clim(0,maxforplot);
ax.set_title('scatter');
plt.axis('off');

ax=plt.subplot(1,3,3);
plt.imshow(randoms[5,:,:,]);
plt.clim(0,maxforplot);
ax.set_title('randoms');
plt.axis('off');
#%% Display central horizontal profiles through the sinogram
plt.figure()
plt.plot(prompts[5,64/2,:],'b');
plt.hold(True)
plt.plot(scatter[5,64/2,:],'c');
plt.plot((scatter+randoms)[5,64/2,:],'g');
plt.legend(('prompts','scatter','randoms', 'scatter+randoms'));

#%% close all plots
plt.close('all')