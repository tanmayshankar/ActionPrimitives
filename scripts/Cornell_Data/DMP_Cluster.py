#!/usr/bin/env python
from headers import *
import sklearn.manifold as skl_manifold

def plot_and_save(to_plot,color,title,name):
	plt.scatter(to_plot[:,0],to_plot[:,1],c=color,s=400)
	plt.title(str(title))
	plt.colorbar()
	# manager = plt.get_current_fig_manager()
	# manager.resize(*manager.window.maxsize())
	# plt.show(block=False)
	plt.savefig(str(name),bbox_inches='tight')
	plt.close()

number_trajectories = 31
number_kernels = 100
number_dimensions = 3
segment_length = 100
number_clusters = 40

lh_nb_weights = npy.load("Meta/lh_nb_meta_weights.npy")
lh_ob_weights = npy.load("Meta/lh_ob_meta_weights.npy")
rh_nb_weights = npy.load("Meta/rh_nb_meta_weights.npy")
rh_ob_weights = npy.load("Meta/rh_ob_meta_weights.npy")


# NBL
weights = copy.deepcopy(lh_nb_weights)

number_samples = weights.shape[0]
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

with file("nblh_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("nblh_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights_NBL.png")	


# NBR
weights = copy.deepcopy(rh_nb_weights)

number_samples = weights.shape[0]
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

with file("nbrh_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("nbrh_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights_NBR.png")	

# OBL
weights = copy.deepcopy(lh_ob_weights)

number_samples = weights.shape[0]
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

with file("oblh_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("oblh_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights_OBL.png")	


# OBR
weights = copy.deepcopy(rh_ob_weights)

number_samples = weights.shape[0]
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

with file("obrh_clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)
with file("obrh_cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights_OBR.png")	
