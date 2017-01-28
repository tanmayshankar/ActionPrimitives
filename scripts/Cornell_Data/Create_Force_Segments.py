#!/usr/bin/env python
from headers import *

num_files = 31

# for i in range(num_files):
for i in range(0,1):
	# FOR LEFT HAND:
	seg_ind = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_30.npy".format(i))
	pos = npy.load("Traj_{0}/lh_comp_pos_{0}.npy".format(i))
	vel = npy.load("Traj_{0}/lh_comp_vel_{0}.npy".format(i))
	acc = npy.load("Traj_{0}/lh_comp_acc_{0}.npy".format(i))

	for j in range(len(seg_ind)-1):
		print("INDEX: ",i,j)
		seg_pos = pos[seg_ind[j]:seg_ind[j+1]]
		seg_vel = vel[seg_ind[j]:seg_ind[j+1]]
		seg_acc = acc[seg_ind[j]:seg_ind[j+1]]		

		with file("Traj_{0}/Force_Segments/lh_seg_{1}_pos.npy".format(i,j),'w') as outfile:
			npy.save(outfile,seg_pos)

		with file("Traj_{0}/Force_Segments/lh_seg_{1}_vel.npy".format(i,j),'w') as outfile:
			npy.save(outfile,seg_vel)

		with file("Traj_{0}/Force_Segments/lh_seg_{1}_acc.npy".format(i,j),'w') as outfile:
			npy.save(outfile,seg_acc)



