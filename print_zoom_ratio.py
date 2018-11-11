#!/usr/bin/env python
# Simple script to print the ratio of the x voxel-sizes of 2 images
import stir
import sys

if (len(sys.argv) != 3):
   print('Usage: %s image1 image2' % sys.argv[0])
   sys.exit(1)
   
name1=sys.argv[1]
name2=sys.argv[2]
image1=stir.FloatVoxelsOnCartesianGrid.read_from_file(name1)
image2=stir.FloatVoxelsOnCartesianGrid.read_from_file(name2)
print(image1.get_voxel_size()[3]/image2.get_voxel_size()[3])

