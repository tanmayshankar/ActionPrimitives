#!/usr/bin/env python
from headers import *
from DMP_Segment import *

num_files = 31

def move_files(i):		
	shutil.move("roll_pos.npy","Traj_{0}/Interp_Segment_All/LH_Seq_Recon_pos.npy".format(i))
	shutil.move("roll_vel.npy","Traj_{0}/Interp_Segment_All/LH_Seq_Recon_vel.npy".format(i))	
	shutil.move("roll_acc.npy","Traj_{0}/Interp_Segment_All/LH_Seq_Recon_acc.npy".format(i))
	
for i in range(0,num_files):	
	print("The Counter is L:",i)
	command = "./../../../../scripts/Sequence_Recon/DMP_Sequence.py Traj_{0}/Interp_Segment_All/LH_Primitive_Weights.npy Traj_{0}/Interp_Segment_All/LH_Start_Seq.npy Traj_{0}/Interp_Segment_All/LH_Goal_Seq.npy".format(i)
	subprocess.call(command.split(),shell=False)
	move_files(i)

def move_files(i):		
	shutil.move("roll_pos.npy","Traj_{0}/Interp_Segment_All/RH_Seq_Recon_pos.npy".format(i))
	shutil.move("roll_vel.npy","Traj_{0}/Interp_Segment_All/RH_Seq_Recon_vel.npy".format(i))	
	shutil.move("roll_acc.npy","Traj_{0}/Interp_Segment_All/RH_Seq_Recon_acc.npy".format(i))
	
for i in range(0,num_files):	
	print("The Counter is R:",i)
	command = "./../../../../scripts/Sequence_Recon/DMP_Sequence.py Traj_{0}/Interp_Segment_All/RH_Primitive_Weights.npy Traj_{0}/Interp_Segment_All/RH_Start_Seq.npy Traj_{0}/Interp_Segment_All/RH_Goal_Seq.npy".format(i)
	subprocess.call(command.split(),shell=False)
	move_files(i)
