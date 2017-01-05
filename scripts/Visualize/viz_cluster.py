# coding: utf-8
import numpy as npy
import matplotlib.pyplot as plt
import sys
import random
from scipy import signal
import copy
import os
from sklearn.cluster import KMeans
import shutil
import subprocess
x = npy.linspace(0,9,10)
c
x
x*=10
x
color = npy.zeros(100)
for i in range(20):
    ptx = npy.load("Points_{0}/points_{0}.npy".format(i))
    plt.scatter(ptx[:,0],ptx[:,1],s=200)
    plt.savefig("Trajectory_{0}.png".format(i),bbox_inches='tight')
    plt.close()
    
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
color
for i in range(0,9):
    color[x[i]:x[i+1]]=i
    
color
x.shape
x[9]
color[90]
color[89]
color[90:99]=9
color
for i in range(20):
    ptx = npy.load("Points_{0}/points_{0}.npy".format(i))
    plt.scatter(ptx[:,0],ptx[:,1],c=color,s=200)
    plt.savefig("Trajectory_{0}.png".format(i),bbox_inches='tight')
    plt.close()
    
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd Data/Mouse_Data/')
for i in range(20):
    ptx = npy.load("Points_{0}/points_{0}.npy".format(i))
    plt.scatter(ptx[:,0],ptx[:,1],c=color,s=200)
    plt.savefig("Trajectory_{0}.png".format(i),bbox_inches='tight')
    plt.close()
    
weights
for i in range(20):
    for j in range(9):
        meta_weights[9*i+j]=npy.load("Points_{0}/force_weights_{1}.npy".format(i,j))
        meta_points[9*i+j]=npy.load("Points_{0}/position_{1}.npy".format(i,j))
        
meta_weights = npy.zeros((180,20,2))
meta_points = npy.zeros((180,20,2))
for i in range(20):
    for j in range(9):
        meta_weights[9*i+j]=npy.load("Points_{0}/force_weights_{1}.npy".format(i,j))
        meta_points[9*i+j]=npy.load("Points_{0}/position_{1}.npy".format(i,j))
        
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,40))
import sklearn.manifold as skl_manifolrd
import sklearn.manifold as skl_manifold
number_samples = 180
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,40))
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(meta_weights.reshape(number_samples,40))
embedded_weights
number_trajectories = 20
number_segments = 9
number_samples = number_segments*number_trajectories
number_kernels = 20
number_dimensions = 2
number_clusters = 20
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))
weights = copy.deepcopy(meta_weights)
number_clusters = 20
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))
cluster_labels = kmeans.labels_

points = npy.load(str(sys.argv[2]))
points_2d = points.reshape((points.shape[0]*points.shape[1],points.shape[2]))

labels = npy.zeros((number_samples, number_kernels))
point_labels = npy.zeros((number_samples, number_kernels))

for i in range(number_trajectories):
	for j in range(number_segments):
		# point_labels[number_trajectories*i+j,:] = i
		point_labels[number_segments*i+j,:] = i
		# labels[number_trajectories*i+j,:] = kmeans.labels_[number_trajectories*i+j]
		labels[number_segments*i+j,:] = kmeans.labels_[number_segments*i+j]

point_labels = point_labels.reshape(number_samples*number_kernels,1)
labels = labels.reshape(number_samples*number_kernels,1)
points = copy.deepcopy(meta_points)
points_2d = points.reshape((points.shape[0]*points.shape[1],points.shape[2]))

labels = npy.zeros((number_samples, number_kernels))
point_labels = npy.zeros((number_samples, number_kernels))

for i in range(number_trajectories):
	for j in range(number_segments):
		# point_labels[number_trajectories*i+j,:] = i
		point_labels[number_segments*i+j,:] = i
		# labels[number_trajectories*i+j,:] = kmeans.labels_[number_trajectories*i+j]
		labels[number_segments*i+j,:] = kmeans.labels_[number_segments*i+j]

point_labels = point_labels.reshape(number_samples*number_kernels,1)
labels = labels.reshape(number_samples*number_kernels,1)
get_ipython().magic(u'ls ')
weights.max()
pos
points
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
embedded_weights.shape
labels
labels.shape
labels = kmeans.labels_
labels.shape
labels.max()
labels==0
(labels==0).astype(int)
for i in range(number_clusters):
    plt.scatter(embedded_weights[labels==i,0],embedded_weights[labels==i,1],c=labels[labels==i],s=200)
    plt.show()
    
plt.scatter(embedded_weights[:,0],embedded_weights[:,1],c=kmeans.labels_,s=200)
plt.title('Plot Embedded Weights using TSNE.')
plt.show()
get_ipython().magic(u'ls ')
plt.scatter(embedded_weights[:,0],embedded_weights[:,1],c=kmeans.labels_,s=200)
plt.title('Plot Embedded Weights using TSNE.')
plt.colorbar()
plt.savefig('Embedded_Weights.png')
plt.scatter(embedded_weights[:,0],embedded_weights[:,1],c=kmeans.labels_,s=200)
plt.title('Plot Embedded Weights using TSNE.')
plt.colorbar()
plt.show()
plt.scatter(embedded_weights[:,0],embedded_weights[:,1],c=kmeans.labels_,s=200)
plt.title('Plot Embedded Weights using TSNE.')
plt.colorbar()
plt.show()
plt.scatter(embedded_weights[:,0],embedded_weights[:,1],c=kmeans.labels_,s=200)
plt.title('Plot Embedded Weights using TSNE.')
plt.colorbar()
plt.show()
points.shape
model_points = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_points = model_points.fit_transform(points.reshape(180,40))
plt.scatter(embedded_points[:,0],embedded_points[:,1])
plt.show()
plt.scatter(embedded_points[:,0],embedded_points[:,1],c=kmeans.labels_,s=200))
plt.scatter(embedded_points[:,0],embedded_points[:,1],c=kmeans.labels_,s=200)
plt.show()
plt.scatter(embedded_points[:,0],embedded_points[:,1],c=kmeans.labels_,s=200)
plt.colorbar()
plt.title("Embedded Points from TSNE.")
plt.show()
plt.scatter(embedded_points[:,0],embedded_points[:,1],c=kmeans.labels_,s=200)
plt.colorbar()
plt.title("Embedded Points from TSNE.")
plt.savefig("Embedded_Points.png",bbox_inches='tight')
plt.scatter(embedded_points[:,0],embedded_points[:,1],c=kmeans.labels_,s=200)
plt.colorbar()
plt.title("Embedded Points from TSNE.")
plt.show()
plt.close9)
plt.close()
plt.scatter(embedded_points[:,0],embedded_points[:,1],c=kmeans.labels_,s=200)
plt.colorbar()
plt.title("Embedded Points from TSNE.")
plt.show()
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'save viz_cluster.py 1-94')
