# coding: utf-8
get_ipython().magic(u'cd ')
get_ipython().magic(u'cd Research/Code/ActionPrimitives/')
s
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Data/Cornell_Data/Primitive_Library/Subject1/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mkdir Interp_Meta')
lhns
lhns = npy.load("LH_Num_Seg_Interp.npy") 
import numpy as npy
get_ipython().magic(u'ls ')
lhns = npy.load("LH_Num_Seg_Interp.npy") 
lhns
lind = npy.load("LH_Seg_Inds.npy")
lhns = npy.load("LH_Num_Seg_Interp.npy")
lignore = npy.array([9,10,11,29])
rignore = npy.array([0,1,4,6,7,8,12,14,20,22,27,30])
lignore
lhns.sum()
lhns[lignore].sum()
get_ipython().magic(u'ls ')
meta_weights = npy.zeros((177,500,3))
lh_meta_weights = npy.zeros((177,500,3))
rh_meta_weights = npy.zeros((177,500,3))
counter = 0 
x = [i for i in range(10)]
x
x = [i for i in range(31) if i not in lignore]
x
lconsider = [i for i in range(31) if i not in lignore]
lconsider
for i in lconsider:
    for j in range(lhns[i]):
        lh_meta_weights[counter] = npy.load("Traj_{0}/Force_Win_Interp_Seg/LH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
lh_meta_weights[176]
lh_meta_weights[175]
counter
rconsider = [i for i in range(31) if i not in rignore]
rconsider
rhns
rhns = npy.load("RH_Num_Seg_Interp.npy")
rhns
rhns.sum()
rhns[rignore].sum()
rh_meta_weights = npy.zeros((121,500,3))
counter = 0
for i in rconsider:
    for j in range(rhns[i]):
        rh_meta_weights[counter]=npy.load("Traj_{0}/Force_Win_Interp_Seg/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
counter
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Interp_Meta/')
get_ipython().magic(u'ls ')
with file("RH_Consider.npy",'w') as outfile:
    npy.save(outfile,rconsider)
    
with file("LH_Consider.npy",'w') as outfile:
    npy.save(outfile,lconsider)
    
with file("LH_Meta_Weights.npy",'w') as outfile:
    npy.save(outfile,lh_meta_weights)
    
with file("RH_Meta_Weights.npy",'w') as outfile:
    npy.save(outfile,rh_meta_weights)
    
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
pps
get_ipython().magic(u'ls ')
get_ipython().magic(u'cp LH_Num_Seg_Interp.npy Interp_Meta/')
get_ipython().magic(u'cp RH_Num_Seg_Interp.npy Interp_Meta/')
get_ipython().magic(u'cd Interp_Meta/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'save Meta_Weights.py 1-609')
