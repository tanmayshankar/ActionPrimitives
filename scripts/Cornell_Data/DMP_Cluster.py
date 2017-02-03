#!/usr/bin/env python
from headers import *
import sklearn.manifold as skl_manifold

number_trajectories = 31
number_kernels = 100
number_dimensions = 3
segment_length = 100
number_clusters = 40

lh_nb_weights = npy.load("Meta/lh_nb_meta_weights.npy")
# lh_ob_weights = npy.load("Meta/lh_ob_meta_weights.npy")
rh_nb_weights = npy.load("Meta/rh_nb_meta_weights.npy")
# rh_ob_weights = npy.load("Meta/rh_ob_meta_weights.npy")

# NBL
weights = copy.deepcopy(lh_nb_weights)
print("NBL")
if (npy.isnan(weights).any()):
	print("BAD NBL")

number_samples = weights.shape[0]
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

with file("nblh_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("nblh_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)
with file("nblh_embedded_weights.npy",'w') as outfile:
	npy.save(outfile,embedded_weights)
# plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights_NBL.png")	


# NBR
weights = copy.deepcopy(rh_nb_weights)
print("NBR")
if (npy.isnan(weights).any()):
	print("BAD NBR")

number_samples = weights.shape[0]
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))
model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

with file("nbrh_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("nbrh_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)
with file("nbrh_embedded_weights.npy",'w') as outfile:
	npy.save(outfile,embedded_weights)

# # OBL
# weights = copy.deepcopy(lh_ob_weights)
# print("OBL")
# if (npy.isnan(weights).any()):
# 	print("BAD OBL")

# number_samples = weights.shape[0]
# kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))
# model = skl_manifold.TSNE(n_components=2,random_state=0)
# embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

# with file("oblh_clustering_labels.npy",'w') as outfile:
# 	npy.save(outfile,kmeans.labels_)
# with file("oblh_cluster_centers.npy",'w') as outfile:
# 	npy.save(outfile,kmeans.cluster_centers_)
# with file("oblh_embedded_weights.npy",'w') as outfile:
# 	npy.save(outfile,embedded_weights)


# # OBR
# weights = copy.deepcopy(rh_ob_weights)
# print("OBR")
# if (npy.isnan(weights).any()):
# 	print("BAD OBR")

# number_samples = weights.shape[0]
# kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))
# model = skl_manifold.TSNE(n_components=2,random_state=0)
# embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

# with file("obrh_clustering_labels.npy",'w') as outfile:
# 	npy.save(outfile,kmeans.labels_)
# with file("obrh_cluster_centers.npy",'w') as outfile:
# 	npy.save(outfile,kmeans.cluster_centers_)
# with file("obrh_embedded_weights.npy",'w') as outfile:
# 	npy.save(outfile,embedded_weights)

