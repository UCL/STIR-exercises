Installation instructions
-------------------------
Author: Kris Thielemans

An easy way to run the exercises is to use the STIR Virtual Machine, but
you can install all of this yourself of course. Below are some brief instructions.



Installing STIR and the exercises
---------------------------------

You will need the updated STIR source made available on [GitHub](https://github.com/UCL/STIR)
for this course. Installation instructions are provided there.

To be able to run these exercises you need to 
- build STIR with its Python interface (via SWIG) enabled. 
- install STIR in your preferred location
- have the STIR utilities in your `PATH`
- add the STIR Python library to your `PYTHONPATH`
- set an environment variable `STIR_exercises_PATH` to where you installed the
STIR exercises (i.e. where this file is). However, this is only used at the
start of each script to go to the relevant directory.


On Linux/MacOS/cygwin using sh/bash, the last 3 items would 
correspond to something like
```sh
PATH=/wherever/you/installed/STIR/bin:$PATH
PYTHONPATH=/wherever/you/installed/STIR/python:$PYTHONPATH
export PYTHONPATH
STIR_exercises_PATH=~/STIR-exercises
export STIR_exercises_PATH
```
After installing, try to type in your terminal
```
forward_project
```
You should see a usage message. If you get an error, you probably didn’t
set-up your path correctly.

The STIR-exercises themselves don't need further installation. Just unpack them.

Other utilities
--------------
We recommend that you run the exercises from in an interactive Python
IDE such as spyder, so you will need to install that.

If you want to use AMIDE for display, it is convenient to add this to your
PATH if it hasn't been done yet by its installer.
Open a terminal and type something like this all on one line (adjust to where your files are).
For instance on Cygwin
```
PATH=/cygdrive/c/Program\\ Files\\ \\(x86\\)/amide/bin/:$PATH
```
