#!/usr/bin/env python
from headers import *
# from DMP_Rollout_3D import *
from DMP_Segment import *

number_kernels = 100
dimensions = 3

cluster_centers = npy.load("LH_cluster_centers.npy")
primitives = [DMP() for i in range(cluster_centers.shape[0])]

# ONLY FOR OLD BASIS FUNCTIONS:
def move_files(i):
	shutil.move("roll_pos.npy","Center_Rollouts/LH_roll_pos_{0}.npy".format(i))
	shutil.move("roll_vel.npy","Center_Rollouts/LH_roll_vel_{0}.npy".format(i))	
	shutil.move("roll_acc.npy","Center_Rollouts/LH_roll_acc_{0}.npy".format(i))
	shutil.move("roll_force.npy","Center_Rollouts/LH_roll_force_{0}.npy".format(i))
	shutil.move("target_force.npy","Center_Rollouts/LH_target_force_{0}.npy".format(i))

for i in range(cluster_centers.shape[0]):
	print("Index:",i)
	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
	primitives[i].initialize_variables()
	primitives[i].load_weights(w)
	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions),npy.zeros(dimensions))
	primitives[i].save_rollout()
	move_files(i)

# RH
cluster_centers = npy.load("RH_cluster_centers.npy")
primitives = [DMP() for i in range(cluster_centers.shape[0])]

# ONLY FOR OLD BASIS FUNCTIONS:
def move_files(i):
	shutil.move("roll_pos.npy","Center_Rollouts/RH_roll_pos_{0}.npy".format(i))
	shutil.move("roll_vel.npy","Center_Rollouts/RH_roll_vel_{0}.npy".format(i))	
	shutil.move("roll_acc.npy","Center_Rollouts/RH_roll_acc_{0}.npy".format(i))
	shutil.move("roll_force.npy","Center_Rollouts/RH_roll_force_{0}.npy".format(i))
	shutil.move("target_force.npy","Center_Rollouts/RH_target_force_{0}.npy".format(i))

for i in range(cluster_centers.shape[0]):
	print("Index:",i)
	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
	primitives[i].initialize_variables()
	primitives[i].load_weights(w)
	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions),npy.zeros(dimensions))
	primitives[i].save_rollout()
	move_files(i)
