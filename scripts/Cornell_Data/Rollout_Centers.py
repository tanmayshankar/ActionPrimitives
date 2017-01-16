#!/usr/bin/env python
from headers import *
from DMP_Rollout_3D import *

number_kernels = 100
dimensions = 3

# cluster_centers = npy.load("obrh_cluster_centers.npy")
# primitives = [DMP() for i in range(cluster_centers.shape[0])]

# # ONLY FOR OLD BASIS FUNCTIONS:
# def move_files(i):
# 	shutil.move("roll_pos.npy","Center/rhob_roll_pos_{0}.npy".format(i))
# 	shutil.move("roll_vel.npy","Center/rhob_roll_vel_{0}.npy".format(i))	
# 	shutil.move("roll_acc.npy","Center/rhob_roll_acc_{0}.npy".format(i))
# 	shutil.move("roll_force.npy","Center/rhob_roll_force_{0}.npy".format(i))

# for i in range(cluster_centers.shape[0]):
# 	print("Index:",i)

# 	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
# 	primitives[i].initialize_variables()
# 	primitives[i].load_weights(w)
# 	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions))
# 	primitives[i].save_rollout()
# 	move_files(i)

# cluster_centers = npy.load("oblh_cluster_centers.npy")
# primitives = [DMP() for i in range(cluster_centers.shape[0])]

# # ONLY FOR OLD BASIS FUNCTIONS:
# def move_files(i):
# 	shutil.move("roll_pos.npy","Center/lhob_roll_pos_{0}.npy".format(i))
# 	shutil.move("roll_vel.npy","Center/lhob_roll_vel_{0}.npy".format(i))	
# 	shutil.move("roll_acc.npy","Center/lhob_roll_acc_{0}.npy".format(i))
# 	shutil.move("roll_force.npy","Center/lhob_roll_force_{0}.npy".format(i))

# for i in range(cluster_centers.shape[0]):
# 	print("Index:",i)

# 	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
# 	primitives[i].initialize_variables()
# 	primitives[i].load_weights(w)
# 	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions))
# 	primitives[i].save_rollout()
# 	move_files(i)

cluster_centers = npy.load("nbrh_cluster_centers.npy")
primitives = [DMP() for i in range(cluster_centers.shape[0])]

# ONLY FOR OLD BASIS FUNCTIONS:
def move_files(i):
	shutil.move("roll_pos.npy","Center/rhnb_roll_pos_{0}.npy".format(i))
	shutil.move("roll_vel.npy","Center/rhnb_roll_vel_{0}.npy".format(i))	
	shutil.move("roll_acc.npy","Center/rhnb_roll_acc_{0}.npy".format(i))
	shutil.move("roll_force.npy","Center/rhnb_roll_force_{0}.npy".format(i))

for i in range(cluster_centers.shape[0]):
	print("Index:",i)

	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
	primitives[i].initialize_variables()
	primitives[i].load_weights(w)
	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions))
	primitives[i].save_rollout()
	move_files(i)

cluster_centers = npy.load("nblh_cluster_centers.npy")
primitives = [DMP() for i in range(cluster_centers.shape[0])]

# ONLY FOR OLD BASIS FUNCTIONS:
def move_files(i):
	shutil.move("roll_pos.npy","Center/lhnb_roll_pos_{0}.npy".format(i))
	shutil.move("roll_vel.npy","Center/lhnb_roll_vel_{0}.npy".format(i))	
	shutil.move("roll_acc.npy","Center/lhnb_roll_acc_{0}.npy".format(i))
	shutil.move("roll_force.npy","Center/lhnb_roll_force_{0}.npy".format(i))

for i in range(cluster_centers.shape[0]):
	print("Index:",i)

	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
	primitives[i].initialize_variables()
	primitives[i].load_weights(w)
	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions))
	primitives[i].save_rollout()
	move_files(i)
