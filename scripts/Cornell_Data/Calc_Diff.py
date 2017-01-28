#!/usr/bin/env python
from headers import *

num_files = 31

def move_files(i):
	

	shutil.move("lh_comp_pos_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("lh_comp_vel_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("lh_comp_acc_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("rh_comp_pos_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("rh_comp_vel_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("rh_comp_acc_{0}.npy".format(i),"Traj_{0}".format(i))

# for i in range(num_files):
for i in range(24,25):

	print(i)
	left_hand = npy.load("Traj_{0}/Left_Hand_Compensated_{0}.npy".format(i))
	right_hand = npy.load("Traj_{0}/Right_Hand_Compensated_{0}.npy".format(i))	

	left_hand_vel = npy.diff(left_hand,axis=0)
	left_hand_acc = npy.diff(left_hand,axis=0,n=2)

	time_steps = left_hand_acc.shape[0]

	right_hand_vel = npy.diff(right_hand,axis=0)
	right_hand_acc = npy.diff(right_hand,axis=0,n=2)

	left_hand_vel = left_hand_vel[:time_steps]
	right_hand_vel = right_hand_vel[:time_steps]

	left_hand_pos = left_hand[:time_steps]
	right_hand_pos = right_hand[:time_steps]

	with file("lh_comp_pos_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand_pos)

	with file("lh_comp_vel_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand_vel)

	with file("lh_comp_acc_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand_acc)

	with file("rh_comp_pos_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand_pos)

	with file("rh_comp_vel_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand_vel)

	with file("rh_comp_acc_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand_acc)

	move_files(i)