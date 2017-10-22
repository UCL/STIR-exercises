# Exercises for STIR.

This material is intended for practical demonstrations using 
[STIR](http://stir.sourceforge.net) on PET and SPECT Image Reconstruction.

This repository contains exercises to get you going
with STIR. Please check [INSTALL.md](INSTALL.md) first (unless
you have a Virtual Machine with the exercises
pre-installed).

Authors:
- Kris Thielemans
- Charalampos Tsoumpas (initial scatter and motion exercises)
- The instructions below were completed with help from Elisabetta Grecchi and Irene Polycarpou

This software is distributed under an open source license, see [LICENSE.txt](LICENSE.txt)
for details.


Introduction
============

These exercises introduce you to forward project, image reconstruction, scatter
etc in PET and SPECT. 
Simulated data will be prepared during the exercises. These are based on 2 sets of images:

-   Thorax phantom data are obtained from the open access article: 
    *Tsoumpas et al 2013 Phys Med Biol*.
    We use two respiratory gated positions of a thorax FDG PET phantom 
	along with the corresponding CTAC image.

-   Brain data are obtained from [BrainWeb](http://www.bic.mni.mcgill.ca/brainweb/).
    We use a segmented brain-map.

You will probably only want to run either the brain or the thorax data (except for the motion 
correction exercise which is currently only for the thorax).

The input data are stored in the folders called `EX_*`, but you will need to
**run the scripts from the "main" STIR-exercises folders** (open a terminal, 
`cd` to where you extracted the exercises, and always `cd` back after every exercise).

We are using Python for the exercises. Python is an open-source interactive language, 
a bit like MATLAB. We provide Python scripts for the evaluation, so you should be fine.
It would be best to read a Python tutorial first, see the [Appendices](#appendices). We will use
[Spyder](https://pythonhosted.org/spyder) as our Python environment.

As an alternative to Python, we also provide instructions (in the sections 
"command line evaluation")
for loading sinograms and images in a display program. However, this is really not
recommended as the Python scripts are much more convenient. 
***If you are attending a course, only the Python scripts will be used.***
Note that in the text below we’re using [AMIDE](http://amide.sf.net/) for
display. ImageJ would work as well (see the end of the document).

See the appendices at the end of this document for some information to get started.
***Please read this before the course.***


Start of exercises
==================

Open a terminal and type
```
export STIR_exercises_PATH=~/devel/STIR-exercises
cd $STIR_exercises_PATH
spyder&
```
Of course, use the path where the STIR-exercises were installed. Note that on the VM,
the first line is not necessary as it is incorporated into the start-up script.

You will then alternate between the terminal (to run shell scripts that execute STIR commands)
and the spyder window (to run Python scripts that read in data and make plots).

**Note:**

The shell scripts `*.sh` should all write `DONE` or `Done` at the end. If they didn’t,
something went wrong. Check the log files (`*.log`) in the output directory
for the script that failed.

Exercise 1: Brain Data Simulation
=================================

(Always run scripts from the STIR-exercises directory)

This is a simple simulation of a brain phantom. PSF is incorporated. Scatter is set to
zero. Randoms are constant.

The aim of the exercise is get familiar with the scripts and evaluation environment, and
to look at projection data in different ways (sinograms, by view etc)

Read and run script:
```
./run_simulation_brain.sh
```
Python evaluation
-----------------

Open the file `~/devel/STIR-exercises/evaluate_simulation_brain.py` in Spyder (obviously adjust
the path if you installed the exercises elsewhere). You can do this via its menus, or by
typing in the terminal:
```
spyder evaluate_simulation_brain.py
```
Command line evaluation
-----------------------
You will need to extract the sinograms in an "image" Interfile to be able to load them in AMIDE
```
cd working_folder/brain
extract_segments my_prompts.hs
Extract as SegmentByView (0) or BySinogram (1)?[0,1 D:0]: 1
amide my_promptsseg0_by_sino.hv&
```
Check the central sinogram plane to see if it looks as expected.

Go back to main directory
```
cd ../..
```
We can also extract profiles through the sinogram to display these in Excel or GNUmeric
or similar. An example of this is given in the script
```
./evaluate_simulation_brain.sh
```
which will extract the segments and create profile text files for you. Output files will be

`working_folder/brain/profile_prompts.txt`

`working_folder/brain/profile_randoms.txt`

Exercise 2: Data Simulation Thorax with PET
===========================================

(Always run scripts from the `STIR-exercises` directory)

This is a simple simulation of a thorax phantom (2 gates). PSF is not incorporated. 
catter is simulated using STIR. Randoms are constant.

The aim of the exercise is first to do the same things as for the brain, to see differences
in sinograms etc, get a first view on scatter, but then to move on to seeing the effect of motion.

Read and run script:
```
./run_simulations_thorax.sh
```

Python evaluation
-----------------

Start spyder with the evaluation script

spyder evaluate_simulation_thorax.py&

or if spyder is running, just open the file.

Exercise 3: Data Simulation Thorax with SPECT
=============================================

(Always run scripts from the STIR`-exercises` directory)

This is a simple simulation of single slice of a thorax phantom for SPECT.
PSF is incorporated. Scatter is set to zero.

The aim of the exercise is first to see how SPECT sinograms differ from PET.

Read and run script:
```
./run_simulations_SPECT.sh
```
Output is in `working_folder/single_slice_SPECT`.

Python evaluation
-----------------

Start spyder with the evaluation script
```
spyder evaluate_simulation_SPECT.py&
```
or if spyder is running, just open the file.

Command line evaluation
-----------------------

You will need to extract the sinograms in an "image" Interfile to be able to load them in AMIDE
```
cd working_folder/GATE1/
extract_segments my_prompts_g1.hs
Extract as SegmentByView (0) or BySinogram (1)?[0,1 D:0]: 1
cd ../GATE2/
extract_segments my_prompts_g2.hs
Extract as SegmentByView (0) or BySinogram (1)?[0,1 D:0]: 1
cd ..
```
Import the extracted sinogram (e.g. `my_prompts_g1seg0_by_sino.hv`) using **AMIDE**.

Select and export the central sinogram plane and upload them online.

Subtract the two sinograms. This can be done in AMIDE or on the command line
```
stir_subtract -s diff.hs GATE1/my_prompts_g1.hs GATE2/my_prompts_g2.hs
extract_segments diff.hs
Extract as SegmentByView (0) or BySinogram (1)?[0,1 D:0]: 1
```
How does the difference look like in sinogram space?

Go back to main directory
```
cd ..
```
We can also extract profiles through the sinogram to display these in Excel or similar. You could run
```
./evaluate_simulation_thorax.sh
```
to extract the segments and create profiles for you.

Exercise 4: Preparation for Image reconstruction exercise
=========================================================

For the thorax reconstruction exercise, we first need to generate a new simulation data set.
This time just a single slice to speed things up. Scatter is also set to zero for simplicity here.
```
./run_simulation_single_slice.sh
```
Output is in `working_folder/single_slice`. There is no real need to look at the generated results
as they are a single sinogram of the thorax simulation (but without scatter and with PSF).

Exercise 5: Image reconstruction part 1: EMML and OSEM
======================================================

(Always run scripts from the `STIR-exercises` directory)

You will need to have run the corresponding simulation script from the previous section. 
Output is in `working_folder/single_slice` or `working_folder/brain` or
`working_folder/single_slice_SPECT`.

We will now look at EMML and OSEM. A sample script is provided to generate results
```
./run_reconstruction_thorax.sh
```
Or
```
./run_reconstruction_brain.sh
```
Or
```
./run_reconstruction_SPECT.sh
```
This will first run FBP, EMML (also known as MLEM) for 240 iterations, then OSEM (with 8 subsets)
for 240 sub-iterations. For both of these, the images obtained after every 24 updates will be saved.
It will also continue EMML and OSEM from 240 sub-iterations and continue for 8 more, writing images
at every subiterations. In addition, the EMML and OSEM images at 240 iterations are also post-filtered
with a Gaussian filter.

Output is in `working_folder/single_slice` or `working_folder/brain` or
`working_folder/single_slice_SPECT` *resp*.

The script runs the reconstruction on the noiseless simulations. See the next exercise for adding noise.

Sample questions to address:

-   Is it worth running EMML? Why not simply use OSEM?
-   At late iterations, is there a difference between OSEM and MLEM convergence behaviour?

Python evaluation
-----------------

Start spyder with the evaluation script
```
spyder evaluate_reconstruction_brain.py&
```
or if spyder is running, just open the file. If you have run the thorax or SPECT simulation, 
just adjust the path in Line 23 (or there abouts)
```
os.chdir('working_folder/brain')
```
to the appropriate location.

Command line evaluation
-----------------------

Run
```
./evaluate_reconstruction_brain.sh
```
(or choose `evaluate_reconstruction_thorax.sh` or `evaluate_reconstruction_SPECT.sh`).

The script generates some differences images and launches AMIDE. You can of course modify
the script for yourself or type commands on the command line.

Exercise 6: Image reconstruction part 2: adding Poisson noise
=============================================================

(You will have to run the simulation and reconstruction scripts first.)

We can make the simulation more realistic by adding noise to the data. An example would be
(please ***adjust the directory name to your case***, e.g. `working_folder/brain` or
`working_folder/single_slice_SPECT`)
```
cd working_folder/single_slice
# save noiseless data results in a subfolder
mkdir noiseless
cp *.* noiseless
# Generate Poisson noise (after scaling the data with a factor 0.5)
poisson_noise -p my_prompts.hs noiseless/my_prompts.hs 0.5 1
cd ../..
```
For the SPECT exercise, replace `my_prompts.hs` in the text above with `my_sim.hs`.

Run `poisson_noise` to understand what these arguments mean.

As we overwrite the data, we can just use the same reconstruction and
evaluation scripts as before (Exercise 5). An alternative would be to let
`poisson_noise` create a new output file, adjust the reconstruction
parameter files to use your new noisy data (input) and change the
filename used for the output, and change your evaluation scripts.

If you want to "reset" to the noiseless case, you can of course copy the data
in `noiseless` back:
```
cd working_folder/single_slice
# save noisy data
mkdir noisy
cp *.* noisy
# now copy back
cp noiseless/* .
cd ../..
```
Note that if you want to try different noise levels, you have to make sure you
are adding Poisson noise to the noiseless data, not to noisy data that you’ve
created in a previous step.

Sample questions to address:

-   Try different noise levels. Do the images change as you expected?
-   Are the answers to the questions in Exercise 5 the same now that we added noise?

Exercise 7: Image reconstruction part 3: MAP
============================================

This exercise needs results from the previous step (as the MAP reconstruction
starts from an OSEM image in this exercise). Output is in `working_folder/single_slice`
or `working_folder/brain` or `working_folder/single_slice_SPECT` *resp.*

We will now look at OSL and OSSPS with a Quadratic Prior. A sample script
is provided to generate results
```
./run_reconstruction_thorax_MAP.sh
```
or
```
./run_reconstruction_brain_MAP.sh
```
or
```
./run_reconstruction_SPECT_MAP.sh
```
This will run OSL and OSSPS (continuing from a previous OSEM image after 24 subiterations).

**Warning**:

If you added noise to the data (exercise 6), the MAP reconstructions will also use
the noisy data of course. However, because of the initialization with OSEM, you
want to run the normal reconstruction script (Exercise 5) first whenever you
change the noise level.

You could for instance first run this exercise with the noisy data, then move
the noiseless data back in place, then re-run the reconstruction script for
the current exercise.

Sample questions to address:

-   Do OSL and OSSPS generate the same results?
-   Does this depend on the penalty factor? Noise level? Iteration number?
    Initialisation (try to remove the initial estimate for instance).

Start spyder with the evaluation script
```
spyder evaluate_reconstruction_brain_MAP.py&
```
or if spyder is running, just open the file. If you have run the thorax or 
SPECT simulation, just adjust the path in Line 23 (or there-abouts)
```
os.chdir('working_folder/brain')
```
to the appropriate location.

Exercise 8: Random estimation
=============================

This exercise uses Maximum Likelihood estimation to find singles from a
sinogram of ‘delayed coincidences’. These estimated singles are then
used to construct the randoms estimate.

Output is in `working_folder/randoms*.*`

First run
```
./run_randoms.sh
```
This will construct a noiseless randoms sinogram (by using ground-truth
singles), add noise, and run the Maximum Likelihood estimation.

Sample questions to address:

-   How do the estimated singles differ from the fansums? In which situations
does this matter?

-   Is there still noise in the estimated random sinogram? (You could do this
by changing the seed for the Poisson noise generator and re-running the script).

Start spyder with the evaluation script to help you
```
spyder evaluate_randoms.py&
```
or if spyder is running, just open the file.

Exercise 9: Scatter Correction
==============================

(Always run scripts from the `STIR-exercises` directory)

There are 4 example scatter estimation scripts which can be used to investigate
different questions about scatter.

**Run 0**

Ideal (i.e. correct attenuation map, scatter simulation matches with how the data
was generated) scatter correction (using 3 scatter correction loops)

**Run 1**

Calculate scatter by using a smaller energy window than that simulated. This will
demonstrate if the scaling technique works. We have selected 425keV for the lower
energy window (original is 350keV).

~~**Run 2**~~ (this is currently not available)

~~Scatter correction using the scatter estimation from the first gate for both gates.
This will demonstrate how sensitive is scatter in choosing different but adjacent gates.~~

**Run 3**

Perform reconstruction & attenuation correction by using wrong attenuation map. In the
particular exercise we have assigned bone attenuation value to lung attenuation value
for the first gate. Then we use this wrong attenuation map located at the first gate
to correct for attenuation and scatter for each gates.

You will first need to simulate the thorax data
```
./run_simulations_thorax.sh
```
You should run the scripts as folllows (you can try reading it but these scripts are
relatively complicated):
```
./run_scatter_0.sh
```
The scripts make the following files in `working_folder/GATE1` (and similar in 
`working_folder/GATE2`)

-   `input_g1.hs`: "measured" sinogram after randoms correction

-   `my_scatter.hs`: sinogram output of the simulation (i.e. ground truth)

-   `scatter_estimate_run0.hs` etc: sinogram output of the iterative scatter estimation

-   `FDG_g1.hv`: input of the simulation (i.e. ground truth image)

-   `FBP_recon_with_scatter_correction_run0.hv`: FBP reconstruction of the scatter
corrected data

Example questions to answer:

-   How close is the scatter estimate in the ideal case of a simulation and how does
this affect the image reconstruction? (run0)

-   How different is the scatter (and its estimate) between gate 1 and gate 2? (run0)

-   How different is the scatter (and its estimate) if you have a wrong estimate of
the energy dependence of the detection efficiency? (run1)

-   What happens to the scatter estimate and the reconstructed image if you use the
wrong attenuation image? (run3)

Python evaluation
-----------------

2 Python scripts are provided as a starting point for investigating the results.

- `evaluate_scatter_run0.py` which reads results from `run_scatter0.sh` and
displays them comparing with the truth (i.e. simulation input and simulation scatter output) for GATE1

- `evaluate_scatter_run3.py` reads results from run0 and run3 and displays them (also for GATE1).
You should be able to use this script with small modifications to look at results from run 2.
(make a copy, don’t overwrite the existing one).

Evaluation using AMIDE
----------------------

Use **AMIDE** to visualize your FBP_recon_with_scatter_correction_run0.hv for each
gate and the original simulated image. Use maximum display value 25.

Can you display the subtraction (e.g. using stir_subtract) between the two gates?

How much motion do you see in the reconstructed images?

Extract sinograms for display with AMIDE for each of the two gates, e.g.:
```
cd working_folder
extract_segments GATE2/scatter_estimate_run0.hs
extract_segments GATE2/my_scatter_g2.hs
```
Can you display the difference of the two sinograms e.g. using `stir_subtract –s`?
Can you see motion in the original sinograms? Scatter sinograms?

Exercise 10: Motion Correction 
===============================

(Always run scripts from the `STIR-exercises` directory. This exercise depends on the
output of `run_simulations_thorax.sh`)

There are 2 scripts for Part I (MCIR vs noMC):
- `run_MCIR_0.sh`
    - Correct for motion using valid motion vectors and the previously calculated scatter background.
    - output folder: `working_folder/MCIR`

- `run_MCIR_1.sh`
    - Do not correct for motion
    - output folder: `working_folder/noMC`

and 2 scripts for Part II (mismatched AC):

- `run_MCIR_2.sh`
    - Correct for motion using valid motion vectors for emission and the previously calculated
      scatter background but use the same average attenuation map for both gates
    - output folder: `working_folder/MCIR/avAC`

- `run_MCIR_3.sh`
    - Correct for motion using valid motion vectors for emission and the previously calculated
      scatter background but use the same attenuation map
      (based on CTAC_g1) for both gates
    - output folder: `working_folder/MCIR/g1AC`

Run the scripts, e.g.:
```
./run_MCIR_0.sh
./run_MCIR_1.sh
```
It takes about 30seconds to complete each reconstruction. If there are problems, you
can confirm the scripts ran OK:
```
less working_folder/MCIR/MCIR.log
less working_folder/noMC/noMC.log
```
(quit `less` by pressing `q`)

To save some time, you can run Part II in the terminal while already evaluating Part I.

Two Python scripts are provided as a starting point for investigating the results: 
`evaluate_MCIR_Part_I.py` and `evaluate_MCIR_Part_II.py`.

Part I compares motion correction with no motion correction result and shows
the forward motion & backward motion vector images.

Part II compares motion correction using the three different attenuation correction
files (one for each gate, the one obtained from the average, the one obtained from gate 1)

Example questions to answer:

-   How close is motion correction in the ideal case of a simulation and how does this
affect image reconstruction? (Part I)

- What type of motion is simulated? (Part I)

- How important is the use of the correct attenuation map? (Part II)

- Any comment on scatter correction? (Part II)

Exercise 11: Image reconstruction part 4: PSF and MAP
=====================================================

This exercise needs results from exercises 5 and 7. So, you should already have done
the following steps:
```
./run_simulation_SPECT.sh
# optionally add noise as in Exercise 6
./run_reconstruction_SPECT.sh
./run_reconstruction_SPECT_MAP.sh
```
We will now look at OSEM and OSSPS (with a Quadratic Prior) when PSF modelling is
included in the reconstruction. We will only do this for SPECT as at present,
STIR PSF modelling is PET is hard to modify. A script is provided to generate results
```
./run_reconstruction_SPECT_PSF.sh
```
This will run OSEM and OSSPS (continuing from a previous OSEM image after 24
subiterations) with PSF model (check e.g. `OSEMPSF.par`).

Output is in `working_folder/single_slice_SPECT`.

**Warning**:

If you added noise to the data (exercise 6), the MAP reconstructions will also use
the noisy data of course. See the MAP exercise for more info.

Sample questions to address:

-   Does PSF-modelling increase resolution?

-   Do you see edge-effects or overshoots in the reconstructed images? For both
OSEM and OSSPS or only OSEM? Why?

-   What happens to the noise "texture" of the images if you reconstruct with
noisy data. Are overshoots worse?

-   Extension: you could try to underestimate the PSF (edit `OSEMPSF.par`
and change the collimator modelling and re-run the reconstruction script).

Start spyder with the evaluation script
```
spyder evaluate_reconstruction_SPECT_PSF.py&
```
or if spyder is running, just open the file.

Appendices
==========


File extensions
---------------

- `.hv`: Interfile header for an image (volume)
- `.ahv`: (ignore) old-style Interfile header for an image
- `.v`: raw data of an image (in floats)
- `.hs`: Interfile header for projection data (sinograms)
- `.s`: raw data of projection data (in floats)
- `.par`: STIR parameter file
- `.sh`: Shell script (sequence of commands)
- `.bat`: Windows batch file
- `.log`: log file (used to record output of a command)
- `.py`: Python file

A note on keyboard short-cuts inside a VirtualBox VM
----------------------------------------------------

On Windows and Linux, VirtualBox sets the "host-key" by default to `Right-CTRL`, so
unless you change this, you have to use `Left-CTRL` to "send" the `CTRL`-keystroke
to the Virtual Machine. So, below we will always type `Left-CTRL`.

Linux Terminal
--------------

If you have never used a Linux/Unix terminal before, have a look at 
[a tutorial](https://help.ubuntu.com/community/UsingTheTerminal).

You can use `UPARROW` to go to previous commands, and use copy-paste shortcuts 
`Left-CTRL-SHIFT-C` and `Left-CTRL-SHIFT-V`.


Python
------
Here is some suggested material on Python (ordered from easy to quite time-consuming).

-   The official Python tutorial. Just read Section 1, 3, a bit of 4 and a tiny bit of 6.
    <https://docs.python.org/2/tutorial/>

-   Examples for matplotlib, the python module that allows you to make plots almost like in MATLAB
    <https://github.com/patvarilly/dihub-python-for-data-scientists-2015/blob/master/notebooks/02_Matplotlib.ipynb>

-   You could read bits and pieces of Python the Hard Way
    <http://learnpythonthehardway.org/book/index.html>

-   Google has an online class on Python for those who know some programming.
    This goes quite in depth and covers 2 days.
    <https://developers.google.com/edu/python/?csw=1>

One thing which might surprise you that in Python *indentation is important*. You would write for instance
```python
for z in range(0,image.shape[0]):
   plt.figure()
   plt.imshow(image[z,:,:])
# now do something else
```

Spyder
------
We use Spyder as a nice Integrated Development Environment (IDE) for Python
(or iPython which is a slightly friendlier version of Python). You need only
minimal knowledge of Python for this course, but it would be good to read-up a bit (see below).

You will normally work by loading an example script in Spyder in the editor, executing it
bit by bit, and then editing it to do some more work. Useful 
[shortcuts for in the editor](http://www.southampton.ac.uk/~fangohr/blog/spyder-the-python-ide.html)
(these are in Windows-style, including the usual copy-paste shortcuts `Left-CTRL-C`
and `Left-CTRL-V`):

-   `F9` executes the currently highlighted code.
-   `LEFT-CTRL + <RETURN>` executes the current cell (menu entry `Run -> Run cell`).
     A cell is defined as the code between two lines which start with the agreed tag `#%%`.
-   `SHIFT + <RETURN>` executes the current cell and advances the cursor to the next
     cell (menu entry `Run -> Run cell and advance`).
-   `TAB` tries to complete the word/command you have just typed.

The [Spyder Integrated Development Environment](https://pythonhosted.org/spyder/) 
(IDE) has of course lots of parameters which you can tune to your liking. The main
setting that you might want to change is if the graphics are generated "inline" in
the iPython console, or as separate windows. Go to `Tools` > `Preferences` > `Console`>
`Graphics` > `Graphics backend`. Change from "inline" to "automatic" if you prefer the separate windows.

iPython
-------
You might be able to convince spyder to run iPython.
And here are some useful iPython "magic" commands that you can use in the iPython
console on the right (but not in the scripts). Most of these are identical
to what you would use in the terminal. (*Note*: these commands do not work in a Python console.)

-   change to a new directory
```python
    cd some_dir/another_subdir
```
-   change back 2 levels up
```python
    cd ../..
```
-   print current working directory
```python
    pwd
```
-   edit a file
```python
    edit FBP.par
```
-   list files in current directory
```python
    ls *.hs
```
-   Running system commands from the iPython prompt can be done via an exclamation mark
```python
    !FBP2D FBP.par
```
-   Get rid of everything in memory
```python
    %reset
```

Image display without Python
----------------------------

Several display programs can be used. AMIDE reads the interfile volumes directly. ImageJ and others can use
import of raw floats (i.e. the `.v` file). Settings are for instance.
```
Image type: 32-bit Real
Width ?
Height: ?
Offset: 0
Number of images ?
Gap between images: 0
White is 0: Ticked
Little endian: Ticked
```
You will have to find the data sizes from the header (the `.hv` file), or by using the `list_image_info`
STIR command.

STIR commands for evaluation
----------------------------

These are a few STIR commands that can be used on the command prompt (not Python).
You normally don’t need to if you use the Python scripts though.

For nearly all of these, you can just type the command name without arguments for a usage message.

### Basic information about geometry
```
list_projdata_info projdata.hs
list_image_info image.hv
```
### Image reconstruction
```
OSMAPOSL someParameterFile.par
FBP2D somePparameterFile.par
OSSPS someParameterFile.par
```
These are the STIR executables used for reconstruction. In the text above, they are
called by the shells scripts.

### Profile extraction
```
list_image_values prof.txt input_image \
  min_plane max_plane min_row max_row min_col max_col
```
(note: the backslash `\` is used in shell scripts for "line continuation", i.e. when 
everything does not fit on one line. You can of course type it on one line instead.)

`list_image_values`writes values to a text file (for import in Excel et al).

Indices need to be in the STIR convention (plane starts from 0, col,row are
centred around 0). Use `list_image_info` to find ranges.

Note: there is currently a bug in `list_image_values` that row (*x*) and column (*y*)
have to be given in that order (i.e. it's *z,x,y* while should have been *z,y,x*)

### Conversion of projection data to an image for display
```
extract_segments projdata.hs
```
Converts projection data into an (Interfile) image (in fact a 3D volume) e.g.
for display via AMIDE (as no standard display program reads in sinogram data).
