#!/usr/bin/env python
from headers import *

num_files = 31

def move_files(i):
	shutil.move("left_hand_pos_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("left_hand_vel_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("left_hand_acc_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("right_hand_pos_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("right_hand_vel_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("right_hand_acc_{0}.npy".format(i),"Traj_{0}".format(i))

for i in range(num_files):

	left_hand = npy.load("Traj_{0}/Original_Left_Hand_{0}.npy".format(i))
	right_hand = npy.load("Traj_{0}/Original_Right_Hand_{0}.npy".format(i))	

	left_hand_vel = npy.diff(left_hand,axis=0)
	left_hand_acc = npy.diff(left_hand,axis=0,n=2)

	time_steps = left_hand_acc.shape[0]

	right_hand_vel = npy.diff(right_hand,axis=0)
	right_hand_acc = npy.diff(right_hand,axis=0,n=2)

	left_hand_vel = left_hand_vel[:time_steps]
	right_hand_vel = left_hand_vel[:time_steps]
	left_hand_pos = left_hand[:time_steps]
	right_hand_pos = right_hand[:time_steps]

	with file("left_hand_pos_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand_pos)

	with file("left_hand_vel_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand_vel)

	with file("left_hand_acc_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand_acc)

	with file("right_hand_pos_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand_pos)

	with file("right_hand_vel_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand_vel)

	with file("right_hand_acc_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand_acc)

