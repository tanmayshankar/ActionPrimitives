# coding: utf-8
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Cornell_Data/')
from headers import *
get_ipython().magic(u'ls ')
import sklearn.manifold as skl_manifold
from sklearn.decomposition import PCA
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ActionPrimitives/Data/Cornell_Data/Primitive_Library/Subject1/Interp_Meta/')
get_ipython().magic(u'ls ')
lw = npy.load("LH_Meta_Weights.npy")
pca = PCA().fig(lw)
pca = PCA().fit(lw)
lw.shape
lwr = lw.reshape(177,1500)
pca = PCA().fit(lwr)
pca
pca.components_
pca.components_.shape
lwr
pca = PCA(n_components=100).fit(lwr)
pca.components_.shape
pca = PCA(n_components=100).fit(npy.transpose(lwr))
pca.components_.shape
get_ipython().magic(u'ls ')
lh_pcaw = npy.transpose(pca.components_)
lh_pcaw.shape
import sklearn.manifold as skl_manifold
kmeans = KMeans(n_clusters = 20,random_state=0).fit(lha_pcaw))
kmeans = KMeans(n_clusters = 20,random_state=0).fit(lha_pcaw)
kmeans = KMeans(n_clusters = 20,random_state=0).fit(lh_pcaw)
kmeans.labels_
moswl = skl_manifold.TSNE(n_components=2,random_state=0)
model = skl_manifold.TSNE(n_components=2,random_state=0)
lh_embed_pca = model.fit_transform(lh_pcaw)
lh_embed_pca
import matplotlib.pyplot as plt
plt.scatter(lh_embed_pca[:,0],lh_embed_pca[:,1])
plt.show()
plt.scatter(lh_embed_pca[:,0],lh_embed_pca[:,1],c=kmeans.labels_,s=400)
plt.colorbar()
plt.show()
xr3
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
lh_pca
lh_pcaw
lh_pcaw.shape
kmeans.labels_.shape
kmeans.labels_
lh
lhw
lhw = npy.load("LH_Meta_Weights.npy")
lhw.shape
lw.shape
lrwls
lwr
lwr.shape
kmeans = KMeans(n_clusters = 20,random_state=0).fit(lwr)
model = skl_manifold.TSNE(n_components=2,random_state=0)
lh_orig_embed = model.fit_transform(lwr)
lh_orig_embed.shape
plt.scatter(lh_orig_embed[:,0],lh_orig_embed[:,1],c=kmeans.labels_,s=400)
plt.colorbar()
plt.show()
kmeans.labels_
pca = PCA(n_components=10).fit(npy.transpose(lwr)) 
lh_pcaw = npy.transpose(pca.components_)
lh_pcaw.shape
kmeans_low_pca = KMeans(n_clusters=20,random_state=0).fit(lwr)
kmeans_low_pca.labels_
pca = PCA(n_components=500).fit(npy.transpose(lwr)) 
lwr
lwr.shape
pca = PCA(n_components=500).fit(lwr)
pca = PCA(n_components=10).fit(lwr)
lh_low_pca = pca.components_
lh_low_pca.shape
get_ipython().magic(u'pinfo pca')
get_ipython().magic(u'pinfo pca.fit')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Traj_0/Force_Win_Interp_Seg/LH_Segment_0/ls')
get_ipython().magic(u'cd Traj_0/Force_Win_Interp_Seg/LH_Segment_0/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
rf = npy.load("roll_force.npy")
rf
rf.shape
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ..')
l
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls Traj_13')
import os
import shutil
get_ipython().magic(u'pinfo shutil.copy')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
for i in range(31):
    os.mkdir("Traj_{0}/Interp_100B/".format(i))
    
get_ipython().magic(u'ls Traj_13/Force_Win_Interp_Seg/')
get_ipython().magic(u'ls Traj_13/Force_Win_Interp_Seg/LH_Segment_0/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Subject1/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pinfo shutil.copytree')
get_ipython().magic(u'ls ')
for i in range(31):
    shutil.copytree("Traj_{0}/Force_Win_Interp_Seg/".format(i),"Traj_{0}/Interp_100_Basis/".format(i))
    
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls Traj_13/ls')
get_ipython().magic(u'ls Traj_13/')
for i in range(31):
    os.rmdir("Traj_{0}/Interp_100B/".format(i))
    
    
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls Traj_13/')
get_ipython().magic(u'ls Traj_13/Interp_100_Basis/')
get_ipython().magic(u'ls Traj_13/Interp_100_Basis/*/*')
get_ipython().magic(u'ls Traj_13/Interp_100_Basis/*')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
LS
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls Traj_13/')
get_ipython().magic(u'ls Traj_13/Interp_100_Basis/')
get_ipython().magic(u'ls ')
lhns = npy.load("LH_Num_Seg_Interp.npy")
rhns = npy.load("RH_Num_Seg_Interp.npy")
lhi = npy.load("LH_Seg_Inds.npy")
lhoi
lhi
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cp Interp_Meta_500l')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
lhc = npy.load("Interp_Meta_100/LH_Consider.npy")
rhc = npy.load("Interp_Meta_100/RH_Consider.npy")
rhc
lhc
lhns = npy.load("LH_Num_Seg_Interp.npy")
rhns = npy.load("RH_Num_Seg_Interp.npy")
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls Interp_Meta_100/ls')
get_ipython().magic(u'ls Interp_Meta_100/')
for i in rhc:
    for j in range(rhns[i]):
        rh_meta_weights[counter]=npy.load("Traj_{0}/Interp_100_Basis/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
get_ipython().magic(u'ls Traj_0/')
rh_meta_weights = npy.zeros((121,500,3))
lh_meta_weights = npy.zeros((177,500,3))
for i in rhc:
    for j in range(rhns[i]):
        rh_meta_weights[counter]=npy.load("Traj_{0}/Interp_100_Basis/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
counter = 0
for i in rhc:
    for j in range(rhns[i]):
        rh_meta_weights[counter]=npy.load("Traj_{0}/Interp_100_Basis/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
lh_meta_weights = npy.zeros((177,100,3))
rh_meta_weights = npy.zeros((121,100,3))
for i in rhc:
    for j in range(rhns[i]):
        rh_meta_weights[counter]=npy.load("Traj_{0}/Interp_100_Basis/RH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
counter = 0
for i in lhc:
    for j in range(rhns[i]):
        lh_meta_weights[counter]=npy.load("Traj_{0}/Interp_100_Basis/LH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
counter = 0
for i in lhc:
    for j in range(lhns[i]):
        lh_meta_weights[counter]=npy.load("Traj_{0}/Interp_100_Basis/LH_Segment_{1}/force_weights.npy".format(i,j))
        counter+=1
        
with file("LH_Meta_Weights.npy",'w') as outfile:
    npy.save(outfile,lh_meta_weights)
    
with file("RH_Meta_Weights.npy",'w') as outfile:
    npy.save(outfile,rh_meta_weights)
    
get_ipython().magic(u'ls ')
get_ipython().magic(u'mv RH_Meta_Weights.npy Interp_Meta_100/')
get_ipython().magic(u'mv LH_Meta_Weights.npy Interp_Meta_100/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
la
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Interp_Meta_100/')
get_ipython().magic(u'ls ')
lhlabel = npy.load("LH_clustering_labels.npy")
lhew = npy.load("LH_embedded_weights.npy")
lhew.shape
plt
plt.scatter(lhew[:,0],lhew[:,1],c=lhlabel,s=400)
plt.colorbar()
plt.show()
get_ipython().magic(u'ls ')
lhlabel
lhlabelzls
pw
l
pw
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
lh_orig_embed
lh_orig_embed.shape
plt.scatter(lh_orig_embed[:,0],lh_orig_embed[:,1])
plt.show9)
plt.show()
plt.scatter(lh_orig_embed[:,0],lh_orig_embed[:,1],s=400)
plt.show()
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
lhw = npy.load("LH_Meta_Weights.npy")
lhwr = lhw.reshape(177,300)
lh_embed = model.fit_transform(lhwr) 
plt.scatter(lh_embed[:,0],lh_embed[:,1],s=400)
plt.show()
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
rhw = npy.load("RH_Meta_Weights.npy")
rhwr = rhw.reshape(121,300)
rh_embed = model.fit_transform(rhwr)
plt.scatter(rh_embed[:,0],rh_embed[:,1],s=400)
plt.show()
lhw
lhw.max()
lhw.min()
abs(lhw).min()
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'save CLUSTER.py 1-237')
