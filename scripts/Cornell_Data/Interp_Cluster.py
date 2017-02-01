#!/usr/bin/env python
from headers import *
import sklearn.manifold as skl_manifold

number_trajectories = 31
number_kernels = 500
number_dimensions = 3
segment_length = 500
number_clusters = 40

lh_number_samples = 177
rh_number_samples = 121

lh_meta_weights = npy.load("LH_Meta_Weights.npy")
rh_meta_weights = npy.load("RH_Meta_Weights.npy")

kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(lh_meta_weights.reshape(lh_number_samples,number_kernels*number_dimensions))
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(lh_meta_weights.reshape(lh_number_samples,number_kernels*number_dimensions))

with file("LH_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("LH_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)
with file("LH_embedded_weights.npy",'w') as outfile:
	npy.save(outfile,embedded_weights)

kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(rh_meta_weights.reshape(rh_number_samples,number_kernels*number_dimensions))
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(rh_meta_weights.reshape(rh_number_samples,number_kernels*number_dimensions))

with file("RH_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("RH_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)
with file("RH_embedded_weights.npy",'w') as outfile:
	npy.save(outfile,embedded_weights)
