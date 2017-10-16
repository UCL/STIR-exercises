To be able to run these exercises you need to 
- build STIR with its Python interface (via SWIG) enabled. 
- install STIR in your preferred location
- have the STIR utilities in your `PATH`
- add the STIR Python library to your `PYTHONPATH`
- set an environment variable `STIR_exercises_PATH` to where you installed the
STIR exercises (i.e. where this file is). However, this is only used at the
start of each script to go to the relevant directory.


On Linux/MacOS using sh/bash, the last 3 items would 
correspond to something like
```sh
PATH=/wherever/you/installed/STIR/bin:$PATH
PYTHONPATH=/wherever/you/installed/STIR/python:$PYTHONPATH
export PYTHONPATH
STIR_exercises_PATH=~/STIR-exercises
export STIR_exercises_PATH
```

We recommend that you run the exercises from in an interactive Python
IDE such as spyder, so you will need to install that.

An easy way to run the exercises is to use the STIR Virtual Machine, but
you can install all of this yourself of course.


Kris Thielemans
