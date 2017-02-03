#!/usr/bin/env python
from headers import *
from DMP_Rollout import *

number_kernels = 100
dimensions = 3
cluster_centers = npy.load("cluster_centers.npy")

primitives = [DMP() for i in range(cluster_centers.shape[0])]

# ONLY FOR OLD BASIS FUNCTIONS:

def move_files(i):
	shutil.move("roll_pos.npy","Center/roll_pos_{0}.npy".format(i))
	shutil.move("roll_vel.npy","Center/roll_vel_{0}.npy".format(i))	
	shutil.move("roll_acc.npy","Center/roll_acc_{0}.npy".format(i))
	shutil.move("roll_force.npy","Center/roll_force_{0}.npy".format(i))

	# shutil.move("roll_pos.npy","Data/Mouse_Data/roll_pos_{0}.npy".format(i))
	# shutil.move("roll_vel.npy","Data/Mouse_Data/roll_vel_{0}.npy".format(i))	
	# shutil.move("roll_acc.npy","Data/Mouse_Data/roll_acc_{0}.npy".format(i))
	# shutil.move("roll_force.npy","Data/Mouse_Data/roll_force_{0}.npy".format(i))

for i in range(cluster_centers.shape[0]):
	print("Index:",i)
	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
	primitives[i].initialize_variables()
	primitives[i].load_weights(w)
	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions))
	primitives[i].save_rollout()
	move_files(i)

