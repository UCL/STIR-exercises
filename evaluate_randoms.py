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
import io
#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir(os.getenv('STIR_exercises_PATH'))
#%% change directory to where the output files are
os.chdir('working_folder/randoms')
#%% Define functions that read and write the .out files used by STIR
"""
  STIR uses a Mathematica-type of text-format for arrays, where {} are used for every row.
  Here we define a function that gets rid of the braces and then uses numpy.fromstring
  to read the comma-separated values into a numpy array.
  
  Warning: the next implementation only works for 1D arrays
"""
def readSinglesFile(filename):
    f=io.open(filename,'r');
    lines=f.readlines();
    f.close();
    array=numpy.array([]);
    for l in lines:
        l=l.replace('}','').replace('{','').strip();
        if len(l)!=0:
            a=numpy.fromstring(l,sep=',');
            array=numpy.append(array,a);
    return array;
    
"""
  Write a 1D array as a STIR text-file for 2D arrays, as appropriate for the STIR normalisation code
"""
def writeSinglesFile(filename, singles):
    numpy.savetxt(filename, singles.reshape(1,singles.shape[0]), delimiter=',', fmt='%g',header='{{', footer='}}', comments='');

#%% read original and estimated singles
mean_singles=readSinglesFile('true_singles_eff_1_1.out');
estimated_singles=readSinglesFile('estimated_singles_eff_1_10.out');
fansums=readSinglesFile('fansums_for_my_randoms.dat');
#%% read sinograms
mean_randoms=to_numpy(stir.ProjData.read_from_file('mean_randoms.hs'));
noisy_randoms=to_numpy(stir.ProjData.read_from_file('my_randoms.hs'));
estimated_randoms=to_numpy(stir.ProjData.read_from_file('estimated_randoms.hs'));
#%% Plot sinograms
maxforplot=mean_randoms.max()*1.3;
slice=0;

plt.figure()
ax=plt.subplot(1,3,1);
plt.imshow(mean_randoms[slice,:,:,]);
plt.clim(0,maxforplot)
ax.set_title('mean of\nrandoms');
plt.axis('off');
plt.colorbar();

ax=plt.subplot(1,3,2);
plt.imshow(noisy_randoms[slice,:,:,]);
plt.clim(0,maxforplot);
ax.set_title('noisy randoms\n(i.e. delayeds)');
plt.axis('off');
plt.colorbar();

ax=plt.subplot(1,3,3);
plt.imshow(estimated_randoms[slice,:,:,]);
plt.clim(0,maxforplot);
ax.set_title('estimated\nrandoms');
plt.axis('off');
plt.colorbar();

#%% plot singles themselves
plt.figure()
#plt.hold(True)
plt.plot(mean_singles,'b.-')
plt.plot(estimated_singles,'g.-')
plt.legend(('original singles','estimated singles'));
plt.xlabel('detector number')
plt.gca().set_title('singles');

#%% Plot the ratio of the fansums with estimated
plt.figure()
plt.plot(fansums/estimated_singles,'r.-')
plt.xlabel('detector number')
plt.gca().set_title('fansums / estimated');

#%% Extended exercise: set some singles to zero
# Here we modify the mean of the singles (i.e. the simulation input)
# by setting some values to zero (e.g. to simulate a defective block)
# 
# After this, run the run_randoms.sh script again to get new sinograms and estimates.
# You can the just repeat the evaluation by executing this evaluation script again).
mean_singles[10:18]=0;
writeSinglesFile('true_singles_eff_1_1.out',mean_singles)
