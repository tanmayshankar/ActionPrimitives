#!/usr/bin/env python
from headers import *
# from DMP_Invariant import *
from Learn_DMP import *
from DMP_Library import * 

# number_points = 20
number_trajectories = 20

def move_files(ind):
	for r in range(19):
		# shutil.move("force_weights_{0}.npy".format(r),"Data/Mouse_Data/Traj_{0}/".format(ind))	
		# shutil.move("position_{0}.npy".format(r),"Data/Mouse_Data/Traj_{0}/".format(ind))	
		shutil.move("velocity_{0}.npy".format(r),"Data/Mouse_Data/Traj_{0}/".format(ind))
		shutil.move("acceleration_{0}.npy".format(r),"Data/Mouse_Data/Traj_{0}/".format(ind))				
		# shutil.move("phi_{0}.npy".format(r),"Data/Mouse_Data/Points_{0}/".format(ind))	

for i in range(0,number_trajectories):
# for i in range(0,1):	
	print("The Counter is :",i)
	command = "./scripts/Learn_DMP/DMP_Library.py Data/Mouse_Data/Traj_{0}/pos_{0}.npy Data/Mouse_Data/Traj_{0}/vel_{0}.npy Data/Mouse_Data/Traj_{0}/acc_{0}.npy".format(i)	
	subprocess.call(command.split(),shell=False)
	move_files(i)


