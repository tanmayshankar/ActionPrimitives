#!/usr/bin/env python

from headers import *

number_trajectories = 20
number_segments = 19
number_samples = number_segments*number_trajectories
# number_samples = 34
number_kernels = 100
number_dimensions = 2
segment_length = 100

meta_weights = npy.zeros((number_samples,number_kernels,number_dimensions))
meta_points = npy.zeros((number_samples,segment_length,number_dimensions))
meta_rollout = npy.zeros((number_samples,segment_length,number_dimensions))

for i in range(number_trajectories):
	for j in range(number_segments):
		meta_weights[number_segments*i+j] = npy.load("Traj_{0}/force_weights_{1}.npy".format(i,j))
		meta_points[number_segments*i+j] = npy.load("Traj_{0}/position_{1}.npy".format(i,j))
		meta_rollout[number_segments*i+j] = npy.load("Traj_{0}/roll_pos_{1}.npy".format(i,j))		

with file("meta_weight_file.npy",'w') as outfile:
	npy.save(outfile,meta_weights)

with file("meta_point_file.npy",'w') as outfile:
	npy.save(outfile,meta_points)

with file("meta_rollout_points.npy",'w') as outfile:
	npy.save(outfile,meta_rollout)