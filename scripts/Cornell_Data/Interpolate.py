#!/usr/bin/env python
from headers import *

interp_time_points = 500
num_files = 31

rhns = npy.load("Interp_Segment_All/RH_Num_Seg.npy")
rhi = npy.load("Interp_Segment_All/RH_Seg_Ind.npy")

def rh_move_files(i,j):
	shutil.move("interp_demo_pos.npy","Traj_{0}/Interp_Segment_All/RH_Segment_{1}/interp_demo_pos.npy".format(i,j))
	shutil.move("interp_demo_vel.npy","Traj_{0}/Interp_Segment_All/RH_Segment_{1}/interp_demo_vel.npy".format(i,j))
	shutil.move("interp_demo_acc.npy","Traj_{0}/Interp_Segment_All/RH_Segment_{1}/interp_demo_acc.npy".format(i,j))

def lh_move_files(i,j):
	shutil.move("interp_demo_pos.npy","Traj_{0}/Interp_Segment_All/LH_Segment_{1}/interp_demo_pos.npy".format(i,j))
	shutil.move("interp_demo_vel.npy","Traj_{0}/Interp_Segment_All/LH_Segment_{1}/interp_demo_vel.npy".format(i,j))
	shutil.move("interp_demo_acc.npy","Traj_{0}/Interp_Segment_All/LH_Segment_{1}/interp_demo_acc.npy".format(i,j))

for i in range(num_files):
	for j in range(rhns[i]):
		print("Index: RIGHT:",i,j)
		ipos = npy.zeros((interp_time_points+2,3))
		ivel = npy.zeros((interp_time_points,3))
		iacc = npy.zeros((interp_time_points,3))
		pos = []
		pos_fx = []
		pos_fy = []
		pos_fz = []

		pos = npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/demo_pos.npy".format(i,j))[:,:3]
		# print(pos)
		tr = npy.linspace(0,len(pos)-1,len(pos))
		tr_new = npy.linspace(0,len(pos)-1,interp_time_points+2)

		# for k in range(3):
		# 	pos_f = interp1d(tr,pos[:,k],kind='linear')
  #   		ipos[:,k] = pos_f(tr_new)

		pos_fx = interp1d(tr,pos[:,0],kind='linear')
		ipos[:,0] = pos_fx(tr_new)

		pos_fy = interp1d(tr,pos[:,1],kind='linear')
		ipos[:,1] = pos_fy(tr_new)

		pos_fz = interp1d(tr,pos[:,2],kind='linear')
		ipos[:,2] = pos_fz(tr_new)

		ivel = npy.diff(ipos,axis=0)[:interp_time_points]
		iacc = npy.diff(ipos,axis=0,n=2)[:interp_time_points]
		ipos = ipos[:interp_time_points]
		
		with file("interp_demo_pos.npy",'w') as outfile:
			npy.save(outfile,ipos)

		with file("interp_demo_vel.npy",'w') as outfile:
			npy.save(outfile,ivel)

		with file("interp_demo_acc.npy",'w') as outfile:
			npy.save(outfile,iacc) 

		rh_move_files(i,j)			

lhns = npy.load("Interp_Segment_All/LH_Num_Seg.npy")		
lhi = npy.load("Interp_Segment_All/LH_Seg_Ind.npy")

for i in range(num_files):
	for j in range(lhns[i]):	

		print("Index: LEFT:",i,j)

		ipos = npy.zeros((interp_time_points+2,3))
		ivel = npy.zeros((interp_time_points,3))
		iacc = npy.zeros((interp_time_points,3))
		pos = []
		pos_fx = []
		pos_fy = []
		pos_fz = []

		pos = npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/demo_pos.npy".format(i,j))[:,:3]
		print(len(pos),pos.shape)

		tr = npy.linspace(0,len(pos)-1,len(pos))
		tr_new = npy.linspace(0,len(pos)-1,interp_time_points+2)

		pos_fx = interp1d(tr,pos[:,0],kind='linear')
		ipos[:,0] = pos_fx(tr_new)

		pos_fy = interp1d(tr,pos[:,1],kind='linear')
		ipos[:,1] = pos_fy(tr_new)

		pos_fz = interp1d(tr,pos[:,2],kind='linear')
		ipos[:,2] = pos_fz(tr_new)

		ivel = npy.diff(ipos,axis=0)[:interp_time_points]
		iacc = npy.diff(ipos,axis=0,n=2)[:interp_time_points]
		ipos = ipos[:interp_time_points]

		with file("interp_demo_pos.npy",'w') as outfile:
			npy.save(outfile,ipos)

		with file("interp_demo_vel.npy",'w') as outfile:
			npy.save(outfile,ivel)

		with file("interp_demo_acc.npy",'w') as outfile:
			npy.save(outfile,iacc) 

		lh_move_files(i,j)