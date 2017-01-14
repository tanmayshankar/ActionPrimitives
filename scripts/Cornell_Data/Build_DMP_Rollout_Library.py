#!/usr/bin/env python
from headers import *
# from DMP_Invariant import *
# from Learn_DMP import *
# from DMP_Library import * 

number_trajectories = 31
number_segments = npy.load("Number_Segments.npy")

# ORIGINAL BASIS, LEFT
def move_files(i,j):	
	os.mkdir("Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/OldBasis/")
	shutil.move("force_weights.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_target_force.npy".format(i,j))

for i in range(0,number_trajectories):
	for j in range(0,number_segments[i]):

		print("The Counter is :",i,j)
		command = "./scripts/DMP_Rollout/DMP_Rollout.py Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_pos.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_vel.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_acc.npy".format(i,j)
		subprocess.call(command.split(),shell=False)
		move_files(i,j)

# ORIGINAL BASIS, RIGHT
def move_files(i,j):	
	os.mkdir("Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/OldBasis/")
	shutil.move("force_weights.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_target_force.npy".format(i,j))

for i in range(0,number_trajectories):
	for j in range(0,number_segments[i]):

		print("The Counter is :",i,j)
		command = "./scripts/DMP_Rollout/DMP_Rollout.py Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_pos.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_vel.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_acc.npy".format(i,j)
		subprocess.call(command.split(),shell=False)
		move_files(i,j)

# NEW BASIS, LEFT
def move_files(i,j):	
	os.mkdir("Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/NewBasis/")
	shutil.move("force_weights.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_target_force.npy".format(i,j))

for i in range(0,number_trajectories):
	for j in range(0,number_segments[i]):

		print("The Counter is :",i,j)
		command = "./scripts/DMP_Rollout/DMP_Rollout_new_basis.py Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_pos.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_vel.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/lh_acc.npy".format(i,j)
		subprocess.call(command.split(),shell=False)
		move_files(i,j)

# ORIGINAL BASIS, RIGHT
def move_files(i,j):	
	os.mkdir("Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/NewBasis/")
	shutil.move("force_weights.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_target_force.npy".format(i,j))

for i in range(0,number_trajectories):
	for j in range(0,number_segments[i]):

		print("The Counter is :",i,j)
		command = "./scripts/DMP_Rollout/DMP_Rollout_new_basis.py Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_pos.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_vel.npy Data/Cornell_Data/Primitive_Library/Traj_{0}/Segment_{1}/rh_acc.npy".format(i,j)
		subprocess.call(command.split(),shell=False)
		move_files(i,j)
