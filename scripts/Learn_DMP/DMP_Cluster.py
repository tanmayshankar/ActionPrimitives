#!/usr/bin/env python
from headers import *
import sklearn.manifold as skl_manifold

weights1 = npy.load(str(sys.argv[1]))
points1 = npy.load(str(sys.argv[2]))
rollout1 = npy.load(str(sys.argv[3]))

number_trajectories = 20
number_segments = 37
number_samples = number_segments*number_trajectories
number_kernels = 100
number_dimensions = 2
segment_length = 100
number_clusters = 40

weights = npy.zeros((number_samples-2,number_kernels,number_dimensions))
points = npy.zeros((number_samples-2,segment_length,number_dimensions))
rollout = npy.zeros((number_samples-2,segment_length,number_dimensions))

counter = 0
for i in range(number_samples):
    if (i!=153)and(i!=244):
    # if (i!=153)and(i!=294):
        weights[counter]=weights1[i]
        points[counter]=points1[i]
        rollout[counter]=rollout1[i]
        counter += 1
        
number_samples -= 2
weights_2d = weights.reshape(number_samples*number_kernels,2)
points_2d = points.reshape((points.shape[0]*points.shape[1],points.shape[2]))

kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

point_labels = npy.zeros((number_samples+2, segment_length))
for i in range(number_trajectories):
	for j in range(number_segments):    
		point_labels[number_segments*i+j,:] = i		
point_labels = point_labels.reshape((number_samples+2)*segment_length,1)

print(npy.where(point_labels))

# for i in range(number_samples):
# 	print(point_labels[i])

with file("meta_weights.npy",'w') as outfile:
	npy.save(outfile,weights)

with file("meta_points.npy",'w') as outfile:
	npy.save(outfile,points)

with file("meta_rollout.npy",'w') as outfile:
	npy.save(outfile,rollout)


with file("clustering_labels.npy",'w') as outfile:
	npy.save(outfile,kmeans.labels_)

with file("cluster_centers.npy",'w') as outfile:
	npy.save(outfile,kmeans.cluster_centers_)

plabels = npy.zeros(number_samples*segment_length)
counter = 0
for i in range(number_samples+2):
    if (i!=153)and(i!=244):
        plabels[counter] = point_labels[i]
        counter += 1

labels = npy.zeros((number_samples, segment_length))
for i in range(number_samples):
    labels[i,:] = kmeans.labels_[i]
labels = labels.reshape(number_samples*segment_length,1)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(number_samples,number_kernels*number_dimensions))

embedded_points = model.fit_transform(points.reshape(number_samples,segment_length*number_dimensions))


def plot_and_save(to_plot,color,title,name):
	plt.scatter(to_plot[:,0],to_plot[:,1],c=color,s=400)
	plt.title(str(title))g
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
	plot_and_save(points_2d, plabels, "Trajectory Data Points.", "Original_Trajectories.png")
	plot_and_save(points_2d, labels, "Clustered Data Points.", "Clustered_Trajectories.png")
	plot_and_save(weights_2d, labels, "Clustered DMP Weights.", "Clustered_Weights.png")
	plot_and_save(weights_2d, plabels, "Weights by Segment.", "Segment_Weights.png")
	plot_and_save(embedded_weights, kmeans.labels_, "Embedded Weights using TSNE.", "Embedded_Weights.png")	
	plot_and_save(embedded_points,kmeans.labels_, "Embedded Points using TSNE.", "Embedded_Points.png")

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




# RUN THIS:
for j in range(0,number_clusters):
	fig,ax = plt.subplots()
	plt.ylim((-50,1500))
	plt.xlim((-100,2700))
	plt.scatter(points_2d[npy.where(labels==j)[0],0],points_2d[npy.where(labels==j)[0],1],c=point_labels[npy.where(labels==j)[0]],s=400,vmin=0,vmax=number_trajectories)
	# plt.scatter(points_2d[n_componentsy.where(labels==j)[0],0],points_2d[npy.where(labels==j)[0],1],s=200)
	plt.title("Cluster {0}.".format(j))
	manager = plt.get_current_fig_manager()	
	manager.resize(*manager.window.maxsize())
	plt.colorbar()
	plt.show(block=False)
	plt.savefig("Trajectory_Colored_Cluster_{0}.png".format(j),bbox_inches='tight')		
	plt.close()

for j in range(0,number_clusters):
	fig,ax = plt.subplots()
	plt.ylim((-50,1500))
	plt.xlim((-100,2700))
	plt.scatter(points_2d[npy.where(labels==j)[0],0],points_2d[npy.where(labels==j)[0],1],c=labels[npy.where(labels==j)[0]],s=400,vmin=0,vmax=number_clusters)
	# plt.scatter(points_2d[n_componentsy.where(labels==j)[0],0],points_2d[npy.where(labels==j)[0],1],s=200)
	plt.title("Cluster_{0}.".format(j))
	manager = plt.get_current_fig_manager()	
	manager.resize(*manager.window.maxsize())
	plt.colorbar()
	plt.show(block=False)
	plt.savefig("Index_Colored_Cluster_{0}.png".format(j),bbox_inches='tight')		
	plt.close()


