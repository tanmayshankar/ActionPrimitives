#!/usr/bin/env python
from headers import *

number_trajectories = 31
# lhns = npy.load(" LH_Number_Force_Segments.npy")
# rhns = npy.load(" RH_Number_Force_Segments.npy")

lhns = npy.load("Interp_Segment_All_2/LH_Num_Seg.npy")
rhns = npy.load("Interp_Segment_All_2/RH_Num_Seg.npy")

# NEW BASIS, LEFT
def move_files(i,j):	
	shutil.move("force_weights.npy","Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/target_force.npy".format(i,j))

for i in range(0,number_trajectories):	
	for j in range(lhns[i]):	
		print("The Counter is L:",i,j)
		command = "./../../../../scripts/Cornell_Data/DMP_Segment.py Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/interp_demo_pos.npy Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/interp_demo_vel.npy Traj_{0}/Interp_Segment_All_2/LH_Segment_{1}/interp_demo_acc.npy".format(i,j)
		subprocess.call(command.split(),shell=False)
		move_files(i,j)

# NEW BASIS, RIGHT
def move_files(i,j):	
	# os.mkdir(" Traj_{0}/Segment_{1}/NewBasis/".format(i,j))
	shutil.move("force_weights.npy","Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/target_force.npy".format(i,j))

for i in range(0,number_trajectories):
	for j in range(rhns[i]):
		print("The Counter is R:",i,j)
		command = "./../../../../scripts/Cornell_Data/DMP_Segment.py Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/interp_demo_pos.npy Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/interp_demo_vel.npy Traj_{0}/Interp_Segment_All_2/RH_Segment_{1}/interp_demo_acc.npy".format(i,j)
		subprocess.call(command.split(),shell=False)
		move_files(i,j)

