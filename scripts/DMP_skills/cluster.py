#!/usr/bin/env python
from headers import *
from DMP import *
from DMP_Library import *
import sklearn.manifold as skl_manifold

number_trajectories = 9
number_segments = 9
number_samples = number_segments*number_trajectories
number_kernels = 20
number_dimensions = 2

# This should be of the shape: Number_samples, Number_kernels, Number_Dimensions
weights = npy.load(str(sys.argv[1]))
weights_2d = weights.reshape((weights.shape[0]*weights.shape[1],weights.shape[2]))

number_clusters = 10
kmeans = KMeans(n_clusters = number_clusters, random_state=0).fit(weights.reshape(number_samples,number_kernels*number_dimensions))

cluster_labels = kmeans.labels_
# kmeans.cluster_centers_

points = npy.load(str(sys.argv[2]))
points_2d = points.reshape((points.shape[0]*points.shape[1],points.shape[2]))

labels = npy.zeros((number_samples, number_kernels))
point_labels = npy.zeros((number_samples, number_kernels))

for i in range(number_trajectories):
	for j in range(number_segments):
		point_labels[number_trajectories*i+j,:] = i
		labels[number_trajectories*i+j,:] = kmeans.labels_[number_trajectories*i+j]

point_labels = point_labels.reshape(number_samples*number_kernels,1)
labels = labels.reshape(number_samples*number_kernels,1)

model = skl_manifold.TSNE(n_components=2,random_state=0)
embedded_weights = model.fit_transform(weights.reshape(81,40))

plt.scatter(points_2d[:,0],points_2d[:,1],c=point_labels,s=400)
plt.title('Plot data points of each trajectory.')
plt.savefig('Original_Trajectories.png',bbox_inches='tight')
# plt.show()

plt.scatter(points_2d[:,0],points_2d[:,1],c=labels,s=400)
plt.title('Plot of clustered data points.')
plt.savefig('Clustered_Trajectories.png',bbox_inches='tight')
# plt.show()

plt.scatter(weights_2d[:,0],weights_2d[:,1],c=labels,s=400)
plt.title('Plot clustered weights of DMPs.')
plt.savefig('Clustered_Weights.png',bbox_inches='tight')
# plt.show()

plt.scatter(weights_2d[:,0],weights_2d[:,1],c=point_labels,s=400)
plt.title('Plot of Weights colored by Trajectory.')
plt.savefig('Trajectory_Weights.png',bbox_inches='tight')
# plt.show()

plt.scatter(embedded_weights[:,0],embedded_weights[:,1],c=kmeans.labels_,s=400)
plt.title('Plot Embedded Weights using TSNE.')
plt.savefig('Embedded_Weights.png')
# plt.show()

