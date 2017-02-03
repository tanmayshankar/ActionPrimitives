#!/usr/bin/env python
from headers import *

num_files = 31
num_can = 100

for i in range(num_files):
	seg_can = npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_can_ALL.npy".format(i))	
	traj_len = len(npy.load("Traj_{0}/Comp_Seg_Full/rh_roll_force.npy".format(i)))

	window = max(int(traj_len*0.08),40)
	print("_____________________________________________________________________________")
	print("INDEX:", i)
	print("Window:",window)	
	print("Traj Len:",traj_len)

	seg_indices = npy.array([])
	# seg_indices = npy.array(seg_can[0])
	# seg_indices = seg_indices.reshape(1,-1)

	# counter = 0
	for k in range(0,num_can):		
	
		if not((abs(seg_can[k]-seg_indices)<window).any())and(abs(seg_can[k])>window)and(abs(seg_can[k]-traj_len)>window):			
			seg_indices = npy.append(seg_indices,seg_can[k])		
			# counter += 1
	
	seg_indices = npy.sort(seg_indices)

	if not(seg_indices[0]==0):
		seg_indices = npy.append(0,seg_indices)

	seg_indices = npy.append(seg_indices,traj_len)
	print("Candidates:",seg_can)
	# print("Sorted Candidates:",npy.sort(seg_can))
	print("FINAL INDICES:",seg_indices)
	
	with file("rh_window_seg_ind.npy",'w') as outfile:		
		npy.save(outfile,seg_indices)

	# shutil.move("rh_window_seg_ind.npy","Traj_{0}/Comp_Seg_Full/rh_window_seg_ind.npy".format(i))
	shutil.move("rh_window_seg_ind.npy","Traj_{0}/Comp_Seg_Full/rh_seg_ind_ALL.npy".format(i))