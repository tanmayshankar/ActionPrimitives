#!/usr/bin/env python
from headers import *
from DMP_Invariant import *
from DMP_Library import * 

number_points = 20

def move_files(ind):
	for r in range(9):
		shutil.move("force_weights_{0}.npy".format(r),"Data/Mouse_Data/Points_{0}/".format(ind))	
		shutil.move("position_{0}.npy".format(r),"Data/Mouse_Data/Points_{0}/".format(ind))	
		shutil.move("phi_{0}.npy".format(r),"Data/Mouse_Data/Points_{0}/".format(ind))	

for i in range(0,number_points):
	print("The Counter is :",i)
	command = "./scripts/DMP_skills/DMP_Library.py Data/Mouse_Data/Points_{0}/points_{0}.npy".format(i)	
	subprocess.call(command.split(),shell=False)
	move_files(i)


