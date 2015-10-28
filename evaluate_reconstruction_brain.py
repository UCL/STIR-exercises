# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for displaying the results of the brain reconstruction.

Author: Kris Thielemans
"""
#%% Initial imports
import matplotlib.pyplot as plt
import stir
from stirextra import *
import os
#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir('/home/stir/exercises')
#%% run simulation (if you haven't done it yet)
print(os.popen('./run_reconstruction_brain.sh').read())
#%% change directory to where the output files are
os.chdir('working_folder/brain')
#%% Read in images
EMML240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('EMML_240.hv'));
OSEM240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240.hv'));
OSEMPSF240=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEMPSF_240.hv'));
OSEM240_continued_1=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240_continued_1.hv'));
OSEM240_continued_2=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240_continued_2.hv'));
OSEM240_continued_4=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('OSEM_240_continued_4.hv'));

#%% bitmap display of images EMML vs OSEM
maxforplot=EMML240.max();

slice=5;
plt.figure();
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

#%% Display central horizontal profiles through the image
plt.figure()
plt.plot(EMML240[slice,92/2,:],'b');
plt.hold(True)
plt.plot(OSEM240[slice,92/2,:],'c');
plt.legend(('EMML240','OSEM240'));

#%% example of display over subiterations
maxforplot=EMML240.max();

slice=5;
plt.figure();
ax=plt.subplot(1,3,1);
plt.imshow(OSEM240[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM240');

ax=plt.subplot(1,3,2);
plt.imshow(OSEM240_continued_1[slice,:,:,]);
plt.clim(0,maxforplot)
plt.colorbar();
plt.axis('off');
ax.set_title('OSEM241');

diff=OSEM240_continued_1-OSEM240;
ax=plt.subplot(1,3,3);
plt.imshow(diff[slice,:,:,]);
plt.clim(-maxforplot/50,maxforplot/50)
plt.colorbar();
plt.axis('off');
ax.set_title('diff');

#%% Display central horizontal profiles through the image
plt.figure()
plt.hold(True)
plt.plot(OSEM240_continued_1[slice,92/2,:],'b');
plt.plot(OSEM240[slice,92/2,:],'c');
plt.legend(('OSEM240_continued_1','OSEM240'));

plt.figure()
plt.hold(True);
plt.plot((OSEM240_continued_1-OSEM240)[slice,92/2,:],'b');
plt.plot((OSEM240_continued_2-OSEM240_continued_1)[slice,92/2,:],'k');
plt.legend(('subiter 241 - subiter 240', 'subiter 242 - subiter 241'));
#%% close all plots
plt.close('all')
