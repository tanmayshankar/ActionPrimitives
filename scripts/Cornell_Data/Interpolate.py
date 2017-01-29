#!/usr/bin/env python
from headers import *

interp_time_points = 500
num_files = 31

rhns = npy.load("RH_Num_Seg_Interp.npy")
rhi = npy.load("RH_Seg_Inds.npy")

for i in range(num_files):
	for j in range(rhns[i]):
		print("Index: RIGHT:",i,j)
		ipos = npy.zeros((interp_time_points+2,3))
		ivel = npy.zeros((interp_time_points,3))
		iacc = npy.zeros((interp_time_points,3))

		pos = npy.load("Traj_{0}/Force_Win_Interp_Seg/RH_Segment_{1}/demo_pos.npy".format(i,j))

		dt_mul = float(len(pos))/interp_time_points

		tr = npy.linspace(0,len(pos)-1,len(pos))
		tr_new = npy.linspace(0,len(pos)-1,interp_time_points+2)

		for k in range(3):
			pos_f = interp1d(tr,pos[:,k],kind='linear')
    		ipos[:,k] = pos_f(tr_new)

		ivel = npy.diff(ipos,axis=0)[:interp_time_points]
		iacc = npy.diff(ipos,axis=0,n=2)[:interp_time_points]
		ipos = ipos[:interp_time_points]

		with file("Traj_{0}/Force_Win_Interp_Seg/RH_Segment_{1}/interp_demo_pos.npy".format(i,j),'w') as outfile:
			npy.save(outfile,ipos)

		with file("Traj_{0}/Force_Win_Interp_Seg/RH_Segment_{1}/interp_demo_vel.npy".format(i,j),'w') as outfile:
			npy.save(outfile,ivel)

		with file("Traj_{0}/Force_Win_Interp_Seg/RH_Segment_{1}/interp_demo_acc.npy".format(i,j),'w') as outfile:
			npy.save(outfile,iacc) 


lhns = npy.load("LH_Num_Seg_Interp.npy")		
lhi = npy.load("LH_Seg_Inds.npy")

for i in range(num_files):
	for j in range(lhns[i]):

		print("Index: LEFT:",i,j)

		ipos = npy.zeros((interp_time_points+2,3))
		ivel = npy.zeros((interp_time_points,3))
		iacc = npy.zeros((interp_time_points,3))

		pos = npy.load("Traj_{0}/Force_Win_Interp_Seg/LH_Segment_{1}/demo_pos.npy".format(i,j))

		dt_mul = float(len(pos))/interp_time_points

		tr = npy.linspace(0,len(pos)-1,len(pos))
		tr_new = npy.linspace(0,len(pos)-1,interp_time_points+2)

		for k in range(3):
			pos_f = interp1d(tr,pos[:,k],kind='linear')
    		ipos[:,k] = pos_f(tr_new)

		ivel = npy.diff(ipos,axis=0)[:interp_time_points]
		iacc = npy.diff(ipos,axis=0,n=2)[:interp_time_points]
		ipos = ipos[:interp_time_points]

		with file("Traj_{0}/Force_Win_Interp_Seg/LH_Segment_{1}/interp_demo_pos.npy".format(i,j),'w') as outfile:
			npy.save(outfile,ipos)

		with file("Traj_{0}/Force_Win_Interp_Seg/LH_Segment_{1}/interp_demo_vel.npy".format(i,j),'w') as outfile:
			npy.save(outfile,ivel)

		with file("Traj_{0}/Force_Win_Interp_Seg/LH_Segment_{1}/interp_demo_acc.npy".format(i,j),'w') as outfile:
			npy.save(outfile,iacc) 
