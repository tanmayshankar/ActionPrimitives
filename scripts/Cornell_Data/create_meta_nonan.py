#!/usr/bin/env python

from headers import *

number_trajectories = 31
number_segments = npy.load("Number_Segments.npy").astype(int)
number_samples = number_segments.sum()

# number_samples = 34
number_kernels = 100
number_dimensions = 3
segment_length = 100

lh_nb_meta_weights_file = npy.load("lh_nb_meta_weight_file.npy")
lh_nb_meta_points_file = npy.load("lh_nb_meta_point_file.npy")
lh_nb_meta_rollout_file = npy.load("lh_nb_meta_rollout_file.npy")
lh_ob_meta_weights_file = npy.load("lh_ob_meta_weight_file.npy")
lh_ob_meta_points_file = npy.load("lh_ob_meta_point_file.npy")
lh_ob_meta_rollout_file = npy.load("lh_ob_meta_rollout_file.npy")

rh_nb_meta_weights_file = npy.load("rh_nb_meta_weight_file.npy")
rh_nb_meta_points_file = npy.load("rh_nb_meta_point_file.npy")
rh_nb_meta_rollout_file = npy.load("rh_nb_meta_rollout_file.npy")
rh_ob_meta_weights_file = npy.load("rh_ob_meta_weight_file.npy")
rh_ob_meta_points_file = npy.load("rh_ob_meta_point_file.npy")
rh_ob_meta_rollout_file = npy.load("rh_ob_meta_rollout_file.npy")

# NBL
lh_nan_index = npy.where(npy.isnan(lh_nb_meta_weights_file[:,0,:]))[0]
rh_nan_index = npy.where(npy.isnan(rh_nb_meta_weights_file[:,0,:]))[0]

lh_nb_meta_weights = npy.zeros((number_samples-int(len(lh_nan_index)),number_kernels,number_dimensions))
lh_nb_meta_points = npy.zeros((number_samples-int(len(lh_nan_index)),segment_length,number_dimensions))
lh_nb_meta_rollout = npy.zeros((number_samples-int(len(lh_nan_index)),segment_length,number_dimensions))
lh_ob_meta_weights = npy.zeros((number_samples-int(len(lh_nan_index)),number_kernels,number_dimensions))
lh_ob_meta_points = npy.zeros((number_samples-int(len(lh_nan_index)),segment_length,number_dimensions))
lh_ob_meta_rollout = npy.zeros((number_samples-int(len(lh_nan_index)),segment_length,number_dimensions))

rh_nb_meta_weights = npy.zeros((number_samples-int(len(rh_nan_index)),number_kernels,number_dimensions))
rh_nb_meta_points = npy.zeros((number_samples-int(len(rh_nan_index)),segment_length,number_dimensions))
rh_nb_meta_rollout = npy.zeros((number_samples-int(len(rh_nan_index)),segment_length,number_dimensions))
rh_ob_meta_weights = npy.zeros((number_samples-int(len(rh_nan_index)),number_kernels,number_dimensions))
rh_ob_meta_points = npy.zeros((number_samples-int(len(rh_nan_index)),segment_length,number_dimensions))
rh_ob_meta_rollout = npy.zeros((number_samples-int(len(rh_nan_index)),segment_length,number_dimensions))

# LH
counter = 0
for i in range(number_samples):
	if not(i in lh_nan_index):
		lh_nb_meta_weights[counter] = lh_nb_meta_weights_file[i]
		lh_nb_meta_points[counter] = lh_nb_meta_points_file[i]
		lh_nb_meta_rollout[counter] = lh_nb_meta_rollout_file[i]
		lh_ob_meta_weights[counter] = lh_ob_meta_weights_file[i]
		lh_ob_meta_points[counter] = lh_ob_meta_points_file[i]
		lh_ob_meta_rollout[counter] = lh_ob_meta_rollout_file[i]		
		counter += 1

with file("lh_nb_meta_weights.npy",'w') as outfile:
	npy.save(outfile,lh_nb_meta_weights)
with file("lh_nb_meta_points.npy",'w') as outfile:
	npy.save(outfile,lh_nb_meta_points)
with file("lh_nb_meta_rollout.npy",'w') as outfile:
	npy.save(outfile,lh_nb_meta_rollout)

with file("lh_ob_meta_weights.npy",'w') as outfile:
	npy.save(outfile,lh_ob_meta_weights)
with file("lh_ob_meta_points.npy",'w') as outfile:
	npy.save(outfile,lh_ob_meta_points)
with file("lh_ob_meta_rollout.npy",'w') as outfile:
	npy.save(outfile,lh_ob_meta_rollout)


# RH
counter = 0
for i in range(number_samples):
	if not(i in lh_nan_index):
		rh_nb_meta_weights[counter] = rh_nb_meta_weights_file[i]
		rh_nb_meta_points[counter] = rh_nb_meta_points_file[i]
		rh_nb_meta_rollout[counter] = rh_nb_meta_rollout_file[i]
		rh_ob_meta_weights[counter] = rh_ob_meta_weights_file[i]
		rh_ob_meta_points[counter] = rh_ob_meta_points_file[i]
		rh_ob_meta_rollout[counter] = rh_ob_meta_rollout_file[i]		
		counter += 1

with file("rh_nb_meta_weights.npy",'w') as outfile:
	npy.save(outfile,rh_nb_meta_weights)
with file("rh_nb_meta_points.npy",'w') as outfile:
	npy.save(outfile,rh_nb_meta_points)
with file("rh_nb_meta_rollout.npy",'w') as outfile:
	npy.save(outfile,rh_nb_meta_rollout)

with file("rh_ob_meta_weights.npy",'w') as outfile:
	npy.save(outfile,rh_ob_meta_weights)
with file("rh_ob_meta_points.npy",'w') as outfile:
	npy.save(outfile,rh_ob_meta_points)
with file("rh_ob_meta_rollout.npy",'w') as outfile:
	npy.save(outfile,rh_ob_meta_rollout)



