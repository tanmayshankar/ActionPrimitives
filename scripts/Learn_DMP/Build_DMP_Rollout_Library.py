#!/usr/bin/env python
from headers import *
# from DMP_Invariant import *
# from Learn_DMP import *
# from DMP_Library import * 

number_trajectories = 20
number_segments = 37

def move_files(i,j):	
	shutil.move("force_weights.npy","Data/Mouse_Overlap/Traj_{0}/Segment_{1}/force_weights.npy".format(i,j))	
	shutil.move("roll_pos.npy","Data/Mouse_Overlap/Traj_{0}/Segment_{1}/roll_pos.npy".format(i,j))
	shutil.move("roll_vel.npy","Data/Mouse_Overlap/Traj_{0}/Segment_{1}/roll_vel.npy".format(i,j))	
	shutil.move("roll_acc.npy","Data/Mouse_Overlap/Traj_{0}/Segment_{1}/roll_acc.npy".format(i,j))
	shutil.move("roll_force.npy","Data/Mouse_Overlap/Traj_{0}/Segment_{1}/roll_force.npy".format(i,j))
	shutil.move("target_force.npy","Data/Mouse_Overlap/Traj_{0}/Segment_{1}/target_force.npy".format(i,j))

for i in range(0,number_trajectories):
	for j in range(0,number_segments):

		print("The Counter is :",i,j)
		# command = "./scripts/Learn_DMP/Rollout_Trajectories.py Data/Mouse_Overlap/Traj_{0}/Segment_{1}/position_{1}.npy Data/Mouse_Overlap/Traj_{0}/velocity_{1}.npy Data/Mouse_Overlap/Traj_{0}/acceleration_{1}.npy".format(i,j)
		command = "./scripts/DMP_Rollout/DMP_Rollout.py Data/Mouse_Overlap/Traj_{0}/Segment_{1}/pos.npy Data/Mouse_Overlap/Traj_{0}/Segment_{1}/vel.npy Data/Mouse_Overlap/Traj_{0}/Segment_{1}/acc.npy".format(i,j)
		# command = "./scripts/Learn_DMP/DMP_Library.py Data/Mouse_Data/Traj_{0}/pos_{0}.npy Data/Mouse_Data/Traj_{0}/vel_{0}.npy Data/Mouse_Data/Traj_{0}/acc_{0}.npy".format(i)	
		subprocess.call(command.split(),shell=False)
		move_files(i,j)

# def move_files(i):
# 	# shutil.move("force_weights_{0}.npy".format(r),"Data/Mouse_Data/Traj_{0}/".format(ind))	
# 	# shutil.move("position_{0}.npy".format(r),"Data/Mouse_Data/Traj_{0}/".format(ind))	

# 	shutil.move("roll_pos.npy","Data/Mouse_Data/roll_pos_{0}.npy".format(i))
# 	shutil.move("roll_vel.npy","Data/Mouse_Data/roll_vel_{0}.npy".format(i))	
# 	shutil.move("roll_acc.npy","Data/Mouse_Data/roll_acc_{0}.npy".format(i))
# 	shutil.move("roll_force.npy","Data/Mouse_Data/roll_force_{0}.npy".format(i))

# for i in range(0,number_trajectories):
# 	# for j in range(0,number_segments):

# 	print("The Counter is :",i)
# 	command = "./scripts/Learn_DMP/Rollout_Trajectories_1000.py Data/Mouse_Data/Traj_{0}/pos_{0}.npy Data/Mouse_Data/Traj_{0}/vel_{0}.npy Data/Mouse_Data/Traj_{0}/acc_{0}.npy".format(i)	
# 	# command = "./scripts/Learn_DMP/DMP_Library.py Data/Mouse_Data/Traj_{0}/pos_{0}.npy Data/Mouse_Data/Traj_{0}/vel_{0}.npy Data/Mouse_Data/Traj_{0}/acc_{0}.npy".format(i)	
# 	subprocess.call(command.split(),shell=False)
# 	move_files(i)

