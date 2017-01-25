#!/usr/bin/env python
from headers import *

number_trajectories = 31

def move_files(i,j):	
	shutil.move("force_weights.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_force_weights.npy".format(i))	
	shutil.move("roll_pos.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_roll_pos.npy".format(i))
	shutil.move("roll_vel.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_roll_vel.npy".format(i))	
	shutil.move("roll_acc.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_roll_acc.npy".format(i))
	shutil.move("roll_force.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_roll_force.npy".format(i))
	shutil.move("target_force.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_target_force.npy".format(i))
	shutil.move("seg_indices.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/lh_seg_indices.npy".format(i))	

for i in range(0,number_trajectories):	
	print("The Counter is LEFT:",i)
	command = "./scripts/Cornell_Data/DMP_Segment.py Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/lh_comp_pos_{0}.npy Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/lh_comp_vel_{0}.npy Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/lh_comp_acc_{0}.npy".format(i)
	subprocess.call(command.split(),shell=False)
	move_files(i,j)

def move_files(i,j):	
	shutil.move("force_weights.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_force_weights.npy".format(i))	
	shutil.move("roll_pos.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_roll_pos.npy".format(i))
	shutil.move("roll_vel.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_roll_vel.npy".format(i))	
	shutil.move("roll_acc.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_roll_acc.npy".format(i))
	shutil.move("roll_force.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_roll_force.npy".format(i))
	shutil.move("target_force.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_target_force.npy".format(i))
	shutil.move("seg_indices.npy","Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/Comp_Segment/rh_seg_indices.npy".format(i))	

for i in range(0,number_trajectories):	
	print("The Counter is RIGHT:",i)
	command = "./scripts/Cornell_Data/DMP_Segment.py Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/rh_comp_pos_{0}.npy Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/rh_comp_vel_{0}.npy Data/Cornell_Data/Primitive_Library/Subject1/Traj_{0}/rh_comp_acc_{0}.npy".format(i)
	subprocess.call(command.split(),shell=False)
	move_files(i,j)

