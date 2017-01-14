#!/usr/bin/env python

from headers import *

number_trajectories = 31
number_segments = npy.load("Number_Segments.npy")
number_samples = number_segments.sum()

# number_samples = 34
number_kernels = 100
number_dimensions = 3
segment_length = 100

# NBL
meta_weights = npy.zeros((number_samples,number_kernels,number_dimensions))
meta_points = npy.zeros((number_samples,segment_length,number_dimensions))
meta_rollout = npy.zeros((number_samples,segment_length,number_dimensions))

for i in range(number_trajectories):
	for j in range(number_segments[i]):

		meta_weights[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/NewBasis/lh_force_weights.npy".format(i,j))
		meta_points[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/lh_pos.npy".format(i,j))
		meta_rollout[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/NewBasis/lh_roll_pos.npy".format(i,j))		

with file("lh_nb_meta_weight_file.npy",'w') as outfile:
	npy.save(outfile,meta_weights)

with file("lh_nb_meta_point_file.npy",'w') as outfile:
	npy.save(outfile,meta_points)

with file("lh_nb_meta_rollout_file.npy",'w') as outfile:
	npy.save(outfile,meta_rollout)

# NBR
meta_weights = npy.zeros((number_samples,number_kernels,number_dimensions))
meta_points = npy.zeros((number_samples,segment_length,number_dimensions))
meta_rollout = npy.zeros((number_samples,segment_length,number_dimensions))

for i in range(number_trajectories):
	for j in range(number_segments[i]):

		meta_weights[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/NewBasis/rh_force_weights.npy".format(i,j))
		meta_points[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/rh_pos.npy".format(i,j))
		meta_rollout[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/NewBasis/rh_roll_pos.npy".format(i,j))		

with file("rh_nb_meta_weight_file.npy",'w') as outfile:
	npy.save(outfile,meta_weights)

with file("rh_nb_meta_point_file.npy",'w') as outfile:
	npy.save(outfile,meta_points)

with file("rh_nb_meta_rollout_file.npy",'w') as outfile:
	npy.save(outfile,meta_rollout)


# OBL
meta_weights = npy.zeros((number_samples,number_kernels,number_dimensions))
meta_points = npy.zeros((number_samples,segment_length,number_dimensions))
meta_rollout = npy.zeros((number_samples,segment_length,number_dimensions))

for i in range(number_trajectories):
	for j in range(number_segments[i]):

		meta_weights[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/OldBasis/lh_force_weights.npy".format(i,j))
		meta_points[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/lh_pos.npy".format(i,j))
		meta_rollout[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/OldBasis/lh_roll_pos.npy".format(i,j))		

with file("lh_ob_meta_weight_file.npy",'w') as outfile:
	npy.save(outfile,meta_weights)

with file("lh_ob_meta_point_file.npy",'w') as outfile:
	npy.save(outfile,meta_points)

with file("lh_ob_meta_rollout_file.npy",'w') as outfile:
	npy.save(outfile,meta_rollout)

# OBR
meta_weights = npy.zeros((number_samples,number_kernels,number_dimensions))
meta_points = npy.zeros((number_samples,segment_length,number_dimensions))
meta_rollout = npy.zeros((number_samples,segment_length,number_dimensions))

for i in range(number_trajectories):
	for j in range(number_segments[i]):

		meta_weights[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/OldBasis/rh_force_weights.npy".format(i,j))
		meta_points[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/rh_pos.npy".format(i,j))
		meta_rollout[number_segments[:i].sum()+j] = npy.load("Traj_{0}/Segment_{1}/OldBasis/rh_roll_pos.npy".format(i,j))		

with file("rh_ob_meta_weight_file.npy",'w') as outfile:
	npy.save(outfile,meta_weights)

with file("rh_ob_meta_point_file.npy",'w') as outfile:
	npy.save(outfile,meta_points)

with file("rh_ob_meta_rollout_file.npy",'w') as outfile:
	npy.save(outfile,meta_rollout)