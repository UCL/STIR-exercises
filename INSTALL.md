Installation instructions
-------------------------
Author: Kris Thielemans

An easy way to run the exercises is to use the STIR Virtual Machine where
all of this has been done for you, but you can install all of this yourself
of course. Below are some brief instructions.



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
### Jupyter
If you want to sue the jupyter notebooks, you need to have a web-browser and jupyter.
Please check [the jupyter installation instructions](http://jupyter.org/install). We
have had luckk installing this via `pip`:
```
pip install jupyter
```
but [Anaconda](https://www.anaconda.com/what-is-anaconda/) should work as well of course.

### Spyder

We recommend that you run the exercises from in an interactive Python
IDE such as [Spyder](https://pythonhosted.org/spyder/), so you will need to install that.
On Ubuntu, the following should work
```
sudo apt-get update
sudo apt-get install spyder
```
We recommend to use iPython as it allows some "magic" commands making life easier. To get this
into spyder, try
```
sudo apt-get install ipython ipython-qtconsole python-zmq
```
Or when using [Anaconda](https://www.anaconda.com/what-is-anaconda/), check
[here for iPython](https://anaconda.org/anaconda/ipython) and
[here for Spyder](https://anaconda.org/anaconda/spyder).

### AMIDE

The STIR exercises currently run from Python. If you prefer, you can use the (somewhat out-dated)
command line scripts as well, for which you need to install [AMIDE](http://amide.sourceforge.net/)
for display. Check its website for installation instructions, but on Ubuntu etc, the following
might work
```
sudo apt-get install amide
```

On other systems, you might have to add it to your `PATH` if it hasn't been done yet by its installer.
Open a terminal and type something like this all on one line before you start the exercises
(adjust to where your files are)
```
PATH="/cygdrive/c/Program Files (x86)/amide/bin/:$PATH"
```
(the above line is for [Cygwin](http://cygwin.com]).
