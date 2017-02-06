#!/usr/bin/env python
from headers import *
from DMP_Segment import *

num_files = 31
num_ker = 100

for i in range(num_files):

	# Load Trajectory.
	# Load Segmentation Indices.
	# Extract Start and goal locations. 

	print("RH",i)

	rh_pos = npy.load("Traj_{0}/rh_comp_pos_{0}.npy".format(i))[:,:3]
	rh_seg_ind = npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_Ind.npy".format(i))

	num_prim = len(rh_seg_ind)-1

	start_seq = npy.zeros((num_prim,3))
	goal_seq = npy.zeros((num_prim,3))
	meta_weights = npy.zeros((num_prim,num_ker,3))
	# start_seq = [[] for k in range(len(rh_seg_ind)-1)]
	# goal_seq = [[] for k in range(len(rh_seg_ind)-1)]
	# meta_weights = [[] for k in range(len)]

	for j in range(len(rh_seg_ind)-1):

		start_seq[j] = rh_pos[rh_seg_ind[j]]
		goal_seq[j] = rh_pos[rh_seg_ind[j+1]-1]
		meta_weights[j] = npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/force_weights.npy".format(i,j))		

	npy.save("Traj_{0}/Interp_Segment_All/RH_Start_Seq.npy".format(i),start_seq)
	npy.save("Traj_{0}/Interp_Segment_All/RH_Goal_Seq.npy".format(i),goal_seq)
	npy.save("Traj_{0}/Interp_Segment_All/RH_Primitive_Weights.npy".format(i),meta_weights)


	print("LH",i)
	
	lh_pos = npy.load("Traj_{0}/lh_comp_pos_{0}.npy".format(i))[:,:3]
	lh_seg_ind = npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_Ind.npy".format(i))

	num_prim = len(lh_seg_ind)-1

	start_seq = npy.zeros((num_prim,3))
	goal_seq = npy.zeros((num_prim,3))
	meta_weights = npy.zeros((num_prim,num_ker,3))
	# start_seq = [[] for k in range(len(lh_seg_ind)-1)]
	# goal_seq = [[] for k in range(len(lh_seg_ind)-1)]

	for j in range(len(lh_seg_ind)-1):

		start_seq[j] = lh_pos[lh_seg_ind[j]]
		goal_seq[j] = lh_pos[lh_seg_ind[j+1]-1]
		meta_weights[j] = npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/force_weights.npy".format(i,j))

	npy.save("Traj_{0}/Interp_Segment_All/LH_Start_Seq.npy".format(i),start_seq)
	npy.save("Traj_{0}/Interp_Segment_All/LH_Goal_Seq.npy".format(i),goal_seq)
	npy.save("Traj_{0}/Interp_Segment_All/LH_Primitive_Weights.npy".format(i),meta_weights)

