# -*- coding: utf-8 -*-
"""
Example script to forward/back-project some data.

In this example, we will create projection data and images purely
from within Python.
    
Note that the code that use geometric shapes below needs a version of STIR
later than 3Nov2018.

Author: Kris Thielemans
"""

#%% Initial imports
import stir
import stirextra
#import numpy
import matplotlib.pyplot as plt
#%% We first need to define a scanner
# STIR has multiple scanners predefined.
print(stir.Scanner.list_all_names())
#%% Let's use an old scanner that doesn't have too many detectors (for speed)
scanner=stir.Scanner.get_scanner_from_name("ECAT 931")
print(scanner.parameter_info())
#%% Now we need to describe the actual size of the projection data
# We call this the `projection data information`.
#
# We will use a 2D PET acquisition in this example.
# This corresponds to `span=3`, with only 1 "segment".
# You can ignore this terminology now, or check it out at
# http://stir.sourceforge.net/documentation/STIR-glossary.pdf

span=3;
max_ring_diff=1;
# use default number of "views" (or "azimutal angles")
num_views=scanner.get_num_detectors_per_ring()/2;
proj_data_info=stir.ProjDataInfo.ProjDataInfoCTI(scanner,
                                                 span, max_ring_diff,
                                                 num_views, scanner.get_default_num_arccorrected_bins());

#%% Create an empty image with suitable voxel sizes
# use smaller voxels than the default
zoom=1.2;
target=stir.FloatVoxelsOnCartesianGrid(proj_data_info, zoom);
#%% initialise a projection matrix 
# Using ray-tracing here
# Note that the default is to restrict the projection to a cylindrical FOV
projmatrix=stir.ProjMatrixByBinUsingRayTracing();
projmatrix.set_up(proj_data_info, target);
#%% construct projectors
forwardprojector=stir.ForwardProjectorByBinUsingProjMatrixByBin(projmatrix);
forwardprojector.set_up(proj_data_info, target);

backprojector=stir.BackProjectorByBinUsingProjMatrixByBin(projmatrix);
backprojector.set_up(proj_data_info, target);
#%% create projection data for output of forward projection
# We'll just create the data in memory here
exam_info=stir.ExamInfo();
projdataout=stir.ProjDataInMemory(exam_info, proj_data_info);
# Note: we could write to file, but it is right now a bit complicated to open a
#  projection data file for read/write:
#  inout=stir.ios.trunc|stir.ios.ios_base_in|stir.ios.out;
#  projdataout=stir.ProjDataInterfile(projdata.get_exam_info(), proj_data_info, 'my_test_python_projection.hs',inout);
#%% forward project an image.
# As a first example, we will just some uniform data.
# (Remember that although we fill the whole image, the projector will only use
# the inner cylinder.)
target.fill(2);
forwardprojector.forward_project(projdataout, target);
#%% display the output
# There will be only a single segment, corresponding to LORs orthogonal
# to the scanner axis.
# We'll display a single sinogram and a horizontal profile (i.e. projections
# for a single "view")
seg=projdataout.get_segment_by_sinogram(0);
seg_array=stirextra.to_numpy(seg);
plt.figure();
plt.subplot(1,2,1)
plt.imshow(seg_array[10,:,:]);
plt.title('Forward projection')
plt.subplot(1,2,2)
plt.plot(seg_array[10,0,:])
plt.title('Horizontal profile')

#%% backproject this projection data
# we need to set the target to zero first, otherwise it will add to existing numbers.
target.fill(0)
backprojector.back_project(target, projdataout);
#%% display
# This shows a beautiful pattern, a well-known feature of a ray-tracing matrix
target_array=stirextra.to_numpy(target);
plt.figure();
plt.subplot(1,2,1)
plt.imshow(target_array[10,:,:]);
plt.title('Back-projection')
plt.subplot(1,2,2)
plt.plot(target_array[10,80,:])
#%% Let's use more LORs per sinogram bin (which will be a bit slower of course)
projmatrix.set_num_tangential_LORs(10);
# Need to call set_up again
projmatrix.set_up(proj_data_info, target);
#%% You could re-run the forward projection, but we'll skip that for now
# forwardprojector.forward_project(projdataout, target);
#%% Run another backprojection and display
target.fill(0)
backprojector.back_project(target, projdataout);
new_target_array=stirextra.to_numpy(target);
plt.figure();
plt.subplot(1,2,1)
plt.imshow(new_target_array[10,:,:]);
plt.title('Back-projection with 10 LORs per bin')
plt.subplot(1,2,2)
plt.plot(new_target_array[10,80,:])
#%% compare profiles to check if overall features are fine
plt.figure()
plt.plot(target_array[10,80,:])
plt.plot(new_target_array[10,80,:])
plt.title('comparing both profiles')


#%% Let's now create an image with some geometric shapes
target.fill(0)
#%% create a cylinder (note: units are in mm)
length=70
radius=40
z_centre=(target.get_max_z()+target.get_min_z())/2
centre=stir.FloatCartesianCoordinate3D(z_centre,4,4)
shape=stir.EllipsoidalCylinder(length, radius, radius,
                               centre)
#%% we set the image to a discretised version of this shape
shape.construct_volume(target, stir.IntCartesianCoordinate3D(1,1,1))
#%% Let's add another translated cylinder
# The way to do this is currently still awkward. Apologies.
shape.translate(stir.FloatCartesianCoordinate3D(40,70,40))
# make a clone and fill that one with the second shape
target2=target.clone()
shape.construct_volume(target2, stir.IntCartesianCoordinate3D(1,1,1))
# now add that to the previous one (by passing through numpy, sorry)
target_array=stirextra.to_numpy(target);
target_array+=stirextra.to_numpy(target2);
target.fill(target_array.flat)
#%% display
plt.figure()
target_array=stirextra.to_numpy(target);
middle_plane=target_array.shape[0]/2
plt.imshow(target_array[middle_plane,:,:])
#%% forward project this
forwardprojector.forward_project(projdataout, target);
#%% display
seg=projdataout.get_segment_by_sinogram(0);
seg_array=stirextra.to_numpy(seg);
plt.figure();
plt.subplot(1,2,1)
plt.imshow(seg_array[middle_plane,:,:]);
plt.title('Forward projection')
plt.subplot(1,2,2)
plt.plot(seg_array[middle_plane,0,:])
#%% display all slices in a (repeated) loop
import matplotlib.animation as animation
bitmaps=[]
fig=plt.figure()
for plane in range(seg_array.shape[0]):
    bitmap=plt.imshow(seg_array[plane,:,:]);
    plt.clim(0,seg_array.max())
    plt.axis('off');
    bitmaps.append([bitmap])

ani = animation.ArtistAnimation(fig, bitmaps, interval=100, blit=True, repeat_delay=1000)


#%% What now?
# You have all the basic tools to do a simple analytic PET simulation
# (no attenuation etc here yet though).
# You can also add other shapes (stir.Ellipsoid etc), or just make them yourself
# using numpy commands