#!/usr/bin/env python
from headers import *
# from Rollout_Centers import *
# from Rollout_Trajectories import *
from DMP_Rollout import *

number_kernels = 1000
number_trajectories = 20
dimensions = 2


def move_files(i):
	shutil.move("roll_pos.npy","Data/Mouse_Data_New/Trajectory_Rollouts/roll_pos_{0}.npy".format(i))
	shutil.move("roll_vel.npy","Data/Mouse_Data_New/Trajectory_Rollouts/roll_vel_{0}.npy".format(i))	
	shutil.move("roll_acc.npy","Data/Mouse_Data_New/Trajectory_Rollouts/roll_acc_{0}.npy".format(i))
	shutil.move("roll_force.npy","Data/Mouse_Data_New/Trajectory_Rollouts/roll_force_{0}.npy".format(i))
	shutil.move("force_weights.npy","Data/Mouse_Data_New/Trajectory_Rollouts/force_weights_{0}.npy".format(i))

# for i in range(number_trajectories):

# 	print("Index:",i)
# 	w = npy.reshape(cluster_centers[i],(number_kernels,dimensions))
# 	primitives[i].initialize_variables()
# 	primitives
# 	primitives[i].rollout(npy.zeros(dimensions),npy.ones(dimensions))
# 	primitives[i].save_rollout()
# 	move_files(i)

for i in range(0,number_trajectories):
	print("The Counter is :",i)
	command = "./scripts/DMP_Rollout/DMP_Rollout.py Data/Mouse_Data_New/Traj_{0}/pos_{0}.npy Data/Mouse_Data_New/Traj_{0}/vel_{0}.npy Data/Mouse_Data_New/Traj_{0}/acc_{0}.npy".format(i)	
	subprocess.call(command.split(),shell=False)
	move_files(i)
