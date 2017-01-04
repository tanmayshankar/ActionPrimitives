#!/usr/bin/env python
from headers import *
# from DMP import *
# from DMP_Library import *
import sklearn.manifold as skl_manifold
weights = npy.load(str(sys.argv[1]))
points = npy.load(str(sys.argv[2]))


number_trajectories = 20
number_segments = 9
number_samples = number_segments*number_trajectories

number_samples = 34
number_kernels = 20
number_dimensions = 2
segment_length = 20 

# This should be of the shape: Number_samples, Number_kernels, Number_Dimensions

weights_2d = weights.reshape((weights.shape[0]*weights.shape[1],weights.shape[2]))

number_clusters = 5
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

# cluster_labels = kmeans.labels_
# kmeans.cluster_centers_


points_2d = points.reshape((points.shape[0]*points.shape[1],points.shape[2]))

# labels = npy.zeros((number_samples, number_kernels))
# point_labels = npy.zeros((number_samples, number_kernels))

labels = npy.zeros((number_samples, segment_length))
point_labels = npy.zeros((number_samples, segment_length))

for i in range(number_trajectories):
	for j in range(number_segments):
		# point_labels[number_trajectories*i+j,:] = i
		point_labels[number_segments*i+j,:] = i
		# labels[number_trajectories*i+j,:] = kmeans.labels_[number_trajectories*i+j]
		labels[number_segments*i+j,:] = kmeans.labels_[number_segments*i+j]

point_labels = point_labels.reshape(number_samples*segment_length,1)
labels = labels.reshape(number_samples*segment_length,1)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,40))

def plot_and_save(to_plot,color,title,name):
	plt.scatter(to_plot[:,0],to_plot[:,1],c=color,s=400)
	plt.title(str(title))
	plt.colorbar()
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())
	plt.show(block=False)
	plt.savefig(str(name),bbox_inches='tight')
	plt.close()

def jplot(to_plot,color,title):
	plt.scatter(to_plot[:,0],to_plot[:,1],c=color,s=400)
	plt.title(str(title))
	plt.colorbar()
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())
	plt.show()	

def ALL_plot_and_save():
	plot_and_save(points_2d, point_labels, "Trajectory Data Points.", "Original_Trajectories.png")
	plot_and_save(points_2d, labels, "Clustered Data Points.", "Clustered_Trajectories.png")
	plot_and_save(weights_2d, labels, "Clustered DMP Weights.", "Clustered_Weights.png")
	plot_and_save(weights_2d, point_labels, "Weights by Segment.", "Segment_Weights.png")
	plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights.png")	

def ALL_plot():
	jplot(points_2d, point_labels, "Trajectory Data Points.")
	jplot(points_2d, labels, "Clustered Data Points.")
	jplot(weights_2d, labels, "Clustered DMP Weights.")
	jplot(weights_2d, point_labels, "Weights by Segment.")
	jplot(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.")

ALL_plot_and_save()

# for i in range(0,number_trajectories):
# 	for j in range(number_segments):

# 		fig,ax = plt.subplots()		
# 		plt.ylim((0,50))
# 		plt.xlim((0,50))
# 		plt.scatter(points[9*i+j,:,0],points[9*i+j,:,1],s=100)
# 		plt.title("Trajectory {0}, Segment {1}.".format(i,j))
# 		# manager = plt.get_current_fig_manager()
# 		# manager.resize(*manager.window.maxsize())
# 		# plt.show(block=False)
# 		plt.savefig("Traj_{0}_Seg_{1}.png".format(i,j),bbox_inches='tight')
# 		plt.close()

# for i in range(number_trajectories):				
# 	for j in range(number_clusters):    

# 		fig,ax = plt.subplots()		
# 		plt.ylim((0,50))
# 		plt.xlim((0,50))

# 		ind = npy.zeros(number_samples)
# 		ind[9*i:9*(i+1)]=1
# 		ind *= (kmeans.labels_==j).astype(int)	

# 		ind[npy.where(kmeans.labels_==j)[0]]

# 		ind = npy.where(ind)
				
# 		plt.scatter(points[ind,:,0],points[ind,:,1],s=100)
# 		plt.title("Trajectory {0}, Cluster {1}.".format(i,j))		
# 	# manager = plt.get_current_fig_manager()	
# 	# manager.resize(*manager.window.maxsize())
# 		plt.show()
# 	# plt.savefig("Traj_{0}_Cluster_{1}.png".format(i,j),bbox_inches='tight')		
# 		plt.close()

for j in range(0,number_clusters):
	fig,ax = plt.subplots()
	plt.ylim((0,50))
	plt.xlim((0,50))
	plt.scatter(points_2d[npy.where(labels==j)[0],0],points_2d[npy.where(labels==j)[0],1],c=point_labels[npy.where(labels==j)[0]],s=400)
	# plt.scatter(points_2d[n_componentsy.where(labels==j)[0],0],points_2d[npy.where(labels==j)[0],1],s=200)
	plt.title("Cluster {0}.".format(j))
	manager = plt.get_current_fig_manager()	
	manager.resize(*manager.window.maxsize())
	plt.colorbar()
	plt.show(block=False)
	plt.savefig("Cluster_{0}.png".format(j),bbox_inches='tight')		
	plt.close()



# npy.where(y)[0,npy.where((9*i)<npy.where(y)[0]<(9*(i+1)))]


