# coding: utf-8
get_ipython().magic('ls ')
import numpy as npy
npy.save("Hello.npy",0)
get_ipython().magic('ls ')
x = Hello.npy
x = npy.load("Hello.npy")
x
get_ipython().magic('ls ')
get_ipython().magic('cd Data/')
get_ipython().magic('ls ')
get_ipython().magic('cd cls')
get_ipython().magic('cd Cornell_Data/Primitive_Library/Subject1/')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Meta_100/')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd Traj_1/Interp_100_Basis/')
get_ipython().magic('ls ')
get_ipython().magic('cd LH_Segment_0')
get_ipython().magic('ls ')
rp = npy.load("roll_pos.npy")
rp
rp[:,0]/rp[:,1]
rp.shape
rp[:,0]/rp[:,2]
lconsider = lhc
lhc = npy.load("Interp_Meta_100/LH_Consider.npy")
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
lhc = npy.load("Interp_Meta_100/LH_Consider.npy")
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
lhc = npy.load("Interp_Meta_100/LH_Consider.npy")
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
lhc = npy.load("Interp_Meta_100/LH_Consider.npy")
rhc = npy.load("Interp_Meta_100/RH_Consider.npy")
lconsider = lhc
rconsider = rhc
lh_meta_rollout = npy.zeros((177,500,3))
lh_meta_points = npy.zeros((177,500,3))
rh_meta_rollout = npy.zeros((121,500,3))
rh_meta_points = npy.zeros((121,500,3))
counter = 0
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_points[counter]=npy.load("Traj_{0}/Interp_100_Basis/LH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        lh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_100_Basis/LH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
lhns = npy.load("LH_Num_Seg_Interp.npy")
rhns = npy.load("RH_Num_Seg_Interp.npy")
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_points[counter]=npy.load("Traj_{0}/Interp_100_Basis/LH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        lh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_100_Basis/LH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
counter = 0
for i in rconsider:
    for j in range(rhns[i]):
        rh_meta_points[counter]=npy.load("Traj_{0}/Interp_100_Basis/RH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        rh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_100_Basis/RH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
get_ipython().magic('pwd ')
get_ipython().magic('cd Interp_Meta_100/')
get_ipython().magic('ls ')
npy.save("RH_Meta_Weights.npy",rh_meta_weights)
npy.save("RH_Meta_Rollout.npy",rh_meta_rollout)
npy.save("RH_Meta_Points.npy",rh_meta_points)
npy.save("LH_Meta_Rollout.npy",lh_meta_rollout)
npy.save("LH_Meta_Points.npy",lh_meta_points)
get_ipython().magic('ls ')
pls
get_ipython().magic('ls ')
lhew = npy.load("LH_embedded_weights.npy")
lhlabels = npy.load("LH_clustering_labels.npy")
plt.scatter(lhew[:,0],lhew[:,1],c=lhlabels,s=400)
import matplotlib.pyplot as plt
plt.scatter(lhew[:,0],lhew[:,1],c=lhlabels,s=400)
plt.colorbar()
plt.show()
get_ipython().magic('pinfo plt.colormaps')
get_ipython().magic('pinfo plt.show')
plt.show(colormap=jet)
plt.show(colormap='jet')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('cd ..')
l
get_ipython().magic('ls ')
import os
for i in range(31):
    os.mkdir("Traj_{0}/Interp_Oversegment".format(i))
    
get_ipython().magic('ls ')
lhns50 = []
get_ipython().magic('ls ')
for i in range(31):
    lhns50[i] = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i))
    
lhns = []
for i in range(31):
    lhns.extend(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
lhns
lhns = []
lhns = npy.array([[]])
for i in range(31):
    lhns.extend(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
for i in range(31):
    lhns.append(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
lhns
lhns = npy.array([[]])
for i in range(31):
    lhns[i]=(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
lhns
lhns = 
lhns = npy.array([[]])
lhns
get_ipython().magic('ls ')
npy.extend(lhns,x)
x
for i in range(31):
    npy.append(lhns[i],npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
lhns
for i in range(31):
    npy.append(lhns,npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
    
lhns
lhns = npy.array([[]])
for i in range(31):
    lhns=npy.append(lhns,npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
lhns
lhns = [[] for i in range(31)]
for i in range(31):
    lhns[i]=(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))
    
    
lhns
pw
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('mkdir Interp_Oversegment')
rhns = [[] for i in range(31)]
for i in range(31):
    rhns[i]=(npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_50.npy".format(i)))
    
    
rhns
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Oversegment/ls')
get_ipython().magic('cd Interp_Oversegment/')
get_ipython().magic('ls ')
npy.save("LH_Num_Seg_Over.npy",lhns)
npy.save("RH_Num_Seg_Over.npy",rhns)
get_ipython().magic('ls ')
get_ipython().magic('mv LH_Num_Seg_Over.npy LH_Seg_Ind.npy')
get_ipython().magic('mv RH_Num_Seg_Over.npy RH_Seg_Ind.npy')
get_ipython().magic('ls ')
lhns = [[] for i in range(31)]
lhns = npy.zeros(31)
rhns = npy.zeros(31)
for i in range(31):
    rhns[i]=len(npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_50.npy".format(i)))-1
    
    
get_ipython().magic('pwd ')
get_ipython().magic('cd ..')
for i in range(31):
    rhns[i]=len(npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_50.npy".format(i)))-1
    
    
rhns
for i in range(31):
    lhns[i]=len(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)))-1
    
    
ld
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Oversegment/')
get_ipython().magic('ls ')
npy.save("RH_Num_Seg_Over.npy",rhns)
npy.save("LH_Num_Seg_Over.npy",lhns)
get_ipython().magic('ls ')
get_ipython().magic('ls ')
rhns
rhns = rhns.astype(int)
npy.save("RH_Num_Seg_Over.npy",rhns)
lhns = lhns.astype(int)
npy.save("LH_Num_Seg_Over.npy",lhns)
get_ipython().magic('ls ')
rh_seg_ind = npy.load("RH_Num_Seg_Over.npy")
rh_seg_ind
rh_seg_ind = npy.load("RH_Seg_Ind.npy")
rh_seg_ind
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
rh_seg_ind = npy.load("RH_Seg_Inds.npy")
rh_seg_ind = npy.load("RH_Seg_Inds.npy",encoding='ascii')
rh_seg_ind = npy.load("RH_Seg_Inds.npy",encoding='bytes')
rh_seg_ind
get_ipython().magic('cd Interp_Oversegment/')
get_ipython().magic('ls ')
rh_seg_ind_over = npy.load("RH_Seg_Ind.npy")
rh_seg_ind_over
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
rh_seg_ind_over = rh_seg_ind_over.astype(int)
rh_seg_ind_over = npy.load("RH_Seg_Ind.npy")
rh_seg_ind_over
rh_seg_ind
rh_seg_ind_over
lh_seg_ind
lh_seg_ind_over = npy.load("LH_Num_Seg_Over.npy")
for i in range(31):
    lh_seg_ind_over[i] = lh_seg_ind_over.astype(int)
    rh_seg_ind_over[i] = rh_seg_inv_over.astype(int)
    
lh_seg_ind_over[0]
lh_seg_ind_over = npy.load("LH_Seg_Ind.npy")
lh_seg_ind_over
lh_seg_ind_over[0]
for i in range(31):
    lh_seg_ind_over[i] = lh_seg_ind_over.astype(int)
    rh_seg_ind_over[i] = rh_seg_inv_over.astype(int)
    
lh_seg_ind_over[i]
lh_seg_ind_over[i].astype(int)
lh_seg_ind = [[] for i in range(31)]
rh_seg_ind = [[] for i in range(31)]
for i in range(31):
    lh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i))
    rh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_50.npy".format(i))
    
for i in range(31):
    lh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i))
    rh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_50.npy".format(i))
    
get_ipython().magic('pwd ')
get_ipython().magic('cd ..')
for i in range(31):
    lh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_50.npy".format(i)).astype(int)
    rh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_50.npy".format(i)).astype(int)
    
lh_seg_ind
rh_seg_ind
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Oversegment/')
npy.save("LH_Seg_Ind.npy",lh_seg_ind)
npy.save("RH_Seg_Ind.npy",rh_seg_ind)
get_ipython().magic('ls ')
lh_seg_ind 
rh_seg_ind
lhns
rhns
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
rhns30 = npy.load("RH_Num_Seg_Interp.npy")
lhns30 = npy.load("LH_Num_Seg_Interp.npy")
lhns30
lhns
lhns-lhns30
npy.where(lhns-lhns30)
LH_DIFF = npy.where(lhns-lhns30)
RH_DIFF = npy.where(rhns-rhns30)
RH_DIFF
lhi30 = npy.load("LH_Seg_Inds.npy")
lhi30 = npy.load("LH_Seg_Inds.npy",encoding='bytes')
rhi30 = npy.load("RH_Seg_Inds.npy",encoding='bytes')
rhi30
rhi30 = npy.load("RH_Seg_Inds.npy",encoding='bytes').astype(int)
RH_DIFF
rhi30[RH_DIFF]
rh_seg_ind[RH_DIFF]
rh_seg_ind
rh_seg_ind[0]
LH_DIFF
lhns - lhns30
lhc
lhns[14]
lhns[13]
lhns30[13]
lh_seg_ind[13]
lhi30[13]
lhi30[13].astype(int)
lhi30[3]
lh_seg_ind[3]
lhi30[3].astype(int)
RH_DIFF
rh_seg_ind[13]
rhi[13]
rhi30[13]
rhi30[13].astype(int)
rh_seg_ind[13]
rhns - rhns30
npy.argmax(rhns - rhns30)
rh_seg_ind[14]
rhi30[13]
rhi30[14]
rh_seg_ind[14]
rhi30[14]
425/40
get_ipython().magic('ls ')
rh_seg_ind
lh_seg_ind
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
for i in range(31):
    os.mkdir("Traj_{0}/Interp_Segment_All".format(i))
    
get_ipython().magic('ls ')
get_ipython().magic('ls Traj_13')
get_ipython().magic('cd Interp_Oversegment/')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('cd ..')
l
get_ipython().magic('ls ')
lhns = npy.zeros(31)
rhns = npy.zeros(31)
lh_seg_ind = [[] for i in range(31)]
rh_seg_ind = [[] for i in range(31)]
for i in range(31):
    lh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_ALL.npy".format(i)).astype(int)
    rh_seg_ind[i] = npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_ALL.npy".format(i)).astype(int)
    
lh_seg_ind
rh_seg_ind
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
for i in range(31):
    lhns[i]=len(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_ALL.npy".format(i)))-1
    rhns[i]=len(npy.load("Traj_{0}/Comp_Seg/Full/rh_seg_ind_ALL.npy".format(i)))-1
    
    
for i in range(31):
    lhns[i]=len(npy.load("Traj_{0}/Comp_Seg_Full/lh_seg_ind_ALL.npy".format(i)))-1
    rhns[i]=len(npy.load("Traj_{0}/Comp_Seg_Full/rh_seg_ind_ALL.npy".format(i)))-1
    
    
    
rhns
lhns
get_ipython().magic('pwd ')
get_ipython().magic('mkdir Interp_Segment_All')
get_ipython().magic('cd Interp_Segment_All/')
get_ipython().magic('ls ')
npy.save("LH_Num_Seg.npy",lhns)
npy.save("RH_Num_Seg.npy",rhns)
npy.save("LH_Seg_Ind.npy",lh_seg_ind)
npy.save("RH_Seg_Ind.npy",rh_seg_ind)
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
l
get_ipython().magic('ls ')
lhns30
lhns - lhns30
(lhns - lhns30).max()
(lhns - lhns30).argmax()
lhns30
lhi30
lhi30[9]
rhi30[9]
rh_seg_ind[9]
rhi30[9].astype(ind)
rhi30[9].astype(int)
rh_seg_ind[9]
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
for i in range(31):
    for j in range(lhns[i]):
        os.mkdir("Traj_{0}/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        os.mkdir("Traj_{0}/RH_Segment_{1}/".format(i,j))
        
lhns[i]
lhns = lhns.astype(int)
rhns = rhns.astype(int)
for i in range(31):
    for j in range(lhns[i]):
        os.mkdir("Traj_{0}/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        os.mkdir("Traj_{0}/RH_Segment_{1}/".format(i,j))
        
for i in range(31):
    for j in range(lhns[i]):
        os.mkdir("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        os.mkdir("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/".format(i,j))
        
for i in range(31):
    for j in range(lhns[i]):
        print("LH",i,j)
        os.mkdir("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        print("RH",i,k)
        os.mkdir("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/".format(i,j))
        
for i in range(31):
    for j in range(lhns[i]):
        print("LH",i,j)
        os.mkdir("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        print("RH",i,k)
        os.mkdir("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/".format(i,j))
        
for i in range(31):
    for j in range(lhns[i]):
        print("LH",i,j)
        os.mkdir("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        print("RH",i,k)
        os.mkdir("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/".format(i,k))
        
for i in range(1,31):
    for j in range(lhns[i]):
        print("LH",i,j)
        os.mkdir("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        print("RH",i,k)
        os.mkdir("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/".format(i,k))
        
for i in range(1):
    for j in range(lhns[i]):
        print("LH",i,j)
        os.mkdir("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/".format(i,j))
    for k in range(rhns[i]):
        print("RH",i,k)
        os.mkdir("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/".format(i,k))
        
lhns
rhns
lh_seg_ind
lhns
lh_seg_ind
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Segment_All/')
get_ipython().magic('ls ')
lhnsall=npy.load("LH_Num_Seg.npy")
lhnsall
lhns
npy.save("LH_Num_Seg.npy",lhns)
npy.save("RH_Num_Seg.npy",rhns)
lhall = npy.load("LH_Seg_Ind.npy
lhall = npy.load("LH_Seg_Ind.npy")
lhall
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls Interp_Meta_100/')
get_ipython().magic('ls Interp_Oversegment/')
get_ipython().magic('cp Interp_Meta_100/LH_Consider.npy Interp_Segment_All/')
get_ipython().magic('cp Interp_Meta_100/RH_Consider.npy Interp_Segment_All/')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Segment_All/')
lconsider = npy.load("LH_Consider.npy")
rconsider = npy.load("RH_Consider.npy")
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Segment_All/')
get_ipython().magic('ls ')
get_ipython().magic('rm LH_Consider.npy')
get_ipython().magic('rm RH_Consider.npy')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
lhns
rhns
lhns - lhns30
get_ipython().magic('pwd ')
get_ipython().magic('cp Interp_Meta_100/RH_Consider.npy Interp_Segment_All/')
get_ipython().magic('cp Interp_Meta_100/LH_Consider.npy Interp_Segment_All/')
lhns.sum()
lhns[lconsider].sum()
rhns[rconsider].sum()
get_ipython().magic('ls ')
lh_meta_weights = npy.zeros((207,100,3))
rh_meta_weights = npy.zeros((140,100,3))
get_ipython().magic('ls ')
counter = 0
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_points[counter]=npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        lh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
lh_meta_points = npy.zeros((207,500,3))
rh_meta_points = npy.zeros((140,500,3))
lh_meta_rollout = npy.zeros((207,500,3))
rh_meta_rollout = npy.zeros((140,500,3))
get_ipython().magic('ls ')
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_points[counter]=npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        lh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
counter = 0
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_points[counter]=npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        lh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
counter = 0
for i in rconsider:
    for j in range(rhns[i]):
        rh_meta_points[counter]=npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/interp_demo_pos.npy".format(i,j))
        rh_meta_rollout[counter]=npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/roll_pos.npy".format(i,j))
        counter+=1
        
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
for i in rconsider:
    for j in range(rhns[i]):
        rh_meta_wedights[counter]=npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
counter = 0
for i in rconsider:
    for j in range(rhns[i]):
        rh_meta_weights[counter]=npy.load("Traj_{0}/Interp_Segment_All/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
counter = 0
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_weights[counter] = npy.load("Traj_{0}/Interp_Segment_All/LH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Segment_All/')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('rm -r Interp_Oversegment/')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd Subject1/')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Segment_All/')
get_ipython().magic('pwd ')
get_ipython().magic('ls ')
npy.save("LH_Meta_Weights.npy",lh_meta_weights)
npy.save("LH_Meta_Points.npy",lh_meta_points)
npy.save("LH_Meta_Rollout.npy",lh_meta_rollout)
npy.save("RH_Meta_Rollout.npy",rh_meta_rollout)
npy.save("RH_Meta_Points.npy",rh_meta_points)
npy.save("RH_Meta_Weights.npy",rh_meta_weights)
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Meta_100/')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('ls ')
get_ipython().magic('cd Interp_Segment_All/')
get_ipython().magic('ls ')
get_ipython().magic('pwd ')
get_ipython().magic('save META.py 1-440')
