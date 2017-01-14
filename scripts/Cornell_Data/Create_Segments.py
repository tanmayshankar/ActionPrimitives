#!/usr/bin/env python
from headers import *

num_files = 31
segment_length = 100
overlap = 25

def move_files(i):
	shutil.move("left_hand_pos_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("left_hand_vel_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("left_hand_acc_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("right_hand_pos_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("right_hand_vel_{0}.npy".format(i),"Traj_{0}".format(i))
	shutil.move("right_hand_acc_{0}.npy".format(i),"Traj_{0}".format(i))

def move_files_2(i,j):
	shutil.move("lh_pos.npy".format(i),"Traj_{0}/Segment_{1}/".format(i,j))
	shutil.move("lh_vel.npy".format(i),"Traj_{0}/Segment_{1}/".format(i,j))
	shutil.move("lh_acc.npy".format(i),"Traj_{0}/Segment_{1}/".format(i,j))
	shutil.move("rh_pos.npy".format(i),"Traj_{0}/Segment_{1}/".format(i,j))
	shutil.move("rh_vel.npy".format(i),"Traj_{0}/Segment_{1}/".format(i,j))
	shutil.move("rh_acc.npy".format(i),"Traj_{0}/Segment_{1}/".format(i,j))

for i in range(num_files):


	left_hand_pos = npy.load("Traj_{0}/left_hand_pos_{0}.npy".format(i))
	right_hand_pos = npy.load("Traj_{0}/right_hand_pos_{0}.npy".format(i))	

	left_hand_vel = npy.load("Traj_{0}/left_hand_vel_{0}.npy".format(i))
	right_hand_vel = npy.load("Traj_{0}/right_hand_vel_{0}.npy".format(i))	

	left_hand_acc = npy.load("Traj_{0}/left_hand_acc_{0}.npy".format(i))
	right_hand_acc = npy.load("Traj_{0}/right_hand_acc_{0}.npy".format(i))	

	lens = left_hand_pos.shape[0]
	ranges = range(0,lens-segment_length,overlap)
	print(ranges)

	for j in range(len(ranges)):

		print(i,j)

		os.mkdir("Traj_{0}/Segment_{1}".format(i,j))

		lh_seg_pos = left_hand_pos[ranges[j]:ranges[j]+segment_length]
		lh_seg_vel = left_hand_vel[ranges[j]:ranges[j]+segment_length]
		lh_seg_acc = left_hand_acc[ranges[j]:ranges[j]+segment_length]

		rh_seg_pos = right_hand_pos[ranges[j]:ranges[j]+segment_length]
		rh_seg_vel = right_hand_vel[ranges[j]:ranges[j]+segment_length]
		rh_seg_acc = right_hand_acc[ranges[j]:ranges[j]+segment_length]

		with file("lh_pos.npy".format(i),'w') as outfile:
			npy.save(outfile,lh_seg_pos)

		with file("lh_vel.npy".format(i),'w') as outfile:
			npy.save(outfile,lh_seg_vel)

		with file("lh_acc.npy".format(i),'w') as outfile:
			npy.save(outfile,lh_seg_acc)

		with file("rh_pos.npy".format(i),'w') as outfile:
			npy.save(outfile,rh_seg_pos)

		with file("rh_vel.npy".format(i),'w') as outfile:
			npy.save(outfile,rh_seg_vel)

		with file("rh_acc.npy".format(i),'w') as outfile:
			npy.save(outfile,rh_seg_acc)

		move_files_2(i,j)