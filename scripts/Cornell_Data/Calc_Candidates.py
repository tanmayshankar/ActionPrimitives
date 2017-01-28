#!/usr/bin/env python
from headers import *

num_files = 31
num_can = 30

for i in range(num_files):

	print(i)
	# LEFT:
	lforce = npy.load("Traj_{0}/Comp_Seg_Full/lh_roll_force.npy".format(i))

	force_norm = npy.linalg.norm(lforce,axis=1)
	normalized_forces = copy.deepcopy(lforce)
	
	for k in range(3):
	    normalized_forces[:,k] /= force_norm

	force_dot_prod = npy.zeros(len(lforce)-1)

	for t in range(len(lforce)-1):
	    force_dot_prod[t] = npy.dot(normalized_forces[t],normalized_forces[t+1])		    

	seg_can = npy.argsort(force_dot_prod)[0:num_can]

	with file("Traj_{0}/Comp_Seg_Full/lh_seg_can_30.npy".format(i),'w') as outfile:
		npy.save(outfile,seg_can)


	# NOW FOR RIGHT:
	rforce = npy.load("Traj_{0}/Comp_Seg_Full/rh_roll_force.npy".format(i))

	force_norm = npy.linalg.norm(rforce,axis=1)
	normalized_forces = copy.deepcopy(rforce)
	
	for k in range(3):
	    normalized_forces[:,k] /= force_norm

	force_dot_prod = npy.zeros(len(rforce)-1)

	for t in range(len(rforce)-1):
	    force_dot_prod[t] = npy.dot(normalized_forces[t],normalized_forces[t+1])		    

	seg_can = npy.argsort(force_dot_prod)[0:num_can]

	with file("Traj_{0}/Comp_Seg_Full/rh_seg_can_30.npy".format(i),'w') as outfile:
		npy.save(outfile,seg_can)

