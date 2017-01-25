#!/usr/bin/env python
from headers import *

num_files = 31
num_can = 30 

for i in range(num_files):
	seg_can = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_can_30.npy".format(i))	
	traj_len = len(npy.load("Traj_{0}/Comp_Seg_Full/lh_roll_force.npy".format(i)))

	window = int(traj_len*0.08)
	# print("INDEX: _____________________", i)
	# print("Window:",window)	
	seg_indices = npy.array(seg_can[0])
	seg_indices = seg_indices.reshape(1,-1)

	counter = 0
	for k in range(1,num_can):		
	
		if not((abs(seg_can[k]-seg_indices)<window).any())and(abs(seg_can[k])>window)and(abs(seg_can[k]-traj_len)>window):
			counter += 1
			seg_indices = npy.append(seg_indices,seg_can[k])		
	
	seg_indices = npy.sort(seg_indices)

	if not(seg_indices[0]==0):
		seg_indices = npy.append(0,seg_indices)

	seg_indices = npy.append(seg_indices,traj_len)
	# print("Candidates:",seg_can)
	# print("Sorted Candidates:",npy.sort(seg_can))
	print("FINAL INDICES:",seg_indices)
	
	with file("lh_seg_ind_30.npy",'w') as outfile:		
		npy.save(outfile,seg_indices)

	shutil.move("lh_seg_ind_30.npy","Traj_{0}/Comp_Seg_Full/lh_seg_ind_30.npy".format(i))


