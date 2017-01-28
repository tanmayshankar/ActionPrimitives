#!/usr/bin/env python
from headers import *
from variables import *

from mpl_toolkits.mplot3d import Axes3D

number_samples -= 4
plot_lim = 2

weights = npy.load("meta_weights.npy")
points = npy.load("meta_points.npy")
rollout = npy.load("meta_rollout.npy")
centers = npy.load("cluster_centers.npy")
labels = npy.load("clustering_labels.npy")

print(weights.shape)
print(number_samples)

for i in range(number_samples):
	points[i] -= points[i,0,:]
	points[i] /= points[i,points.shape[1]-1,:]	

# ROLLING OUT CLUSTER CENTERS. 
# for i in range(0,number_trajectories):
for i in range(number_clusters):

	print("Index",i)
	# dmp_pos = npy.load("Cluster_Center/roll_pos_{0}.npy".format(i))
	dmp_pos = npy.load("Center/lhob_roll_pos_{0}.npy".format(i))
	fig = plt.figure()
	ax = fig.gca(projection='3d')

	# x_min,y_min = npy.min(dmp_pos,axis=0)
	# x_max,y_max = npy.max(dmp_pos,axis=0)

	# xmin = -5
	# ymin = -5
	# xmax = 5
	# ymax = 5

	for j in range(number_samples):
		if (labels[j]==i):			
			ax.plot(rollout[j,:,0],rollout[j,:,1],rollout[j,:,1],'b')

			# dx_min,dy_min = npy.min(rollout[j,:],axis=0)
			# dx_max,dy_max = npy.max(rollout[j,:],axis=0)

			# xmin = min(dx_min,xmin)
			# ymin = min(dy_min,ymin)
			# xmax = max(dx_max,xmax)
			# ymax = max(dy_max,ymax)
	
	# plt.ylim((min(-plot_lim,y_min,dy_min),max(plot_lim,y_max,dy_max)))
	# plt.xlim((min(-plot_lim,x_min,dx_min),max(plot_lim,x_max,dx_max)))

	ax.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2],'r',linewidth=2)
	plt.title("Cluster {0}".format(i))
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())	
	# plt.show(block=False)	
	plt.show()
	# plt.savefig("Cluster_Center_{0}.png".format(i),bbox_inches='tight')
	# plt.close()





# # ROLLING OUT CLUSTER CENTERS TOGETHER. 
# xmin = -5
# ymin = -5
# xmax = 5
# ymax = 5

# for i in range(number_clusters):

# 	print("Index",i)
# 	dmp_pos = npy.load("Cluster_Center/roll_pos_{0}.npy".format(i))
# 	x_min,y_min = npy.min(dmp_pos,axis=0)
# 	x_max,y_max = npy.max(dmp_pos,axis=0)

# 	plt.plot(dmp_pos[:,0],dmp_pos[:,1],'r',linewidth=2)
	
# 	xmin = min(x_min,xmin)
# 	ymin = min(y_min,ymin)
# 	xmax = max(x_max,xmax)
# 	ymax = max(y_max,ymax)
	
# # plt.ylim((min(-plot_lim,ymin),max(plot_lim,ymax)))
# # plt.xlim((min(-plot_lim,xmin),max(plot_lim,xmax)))

# # plt.xlim(-5,5)
# # plt.ylim(-5,5)


# manager = plt.get_current_fig_manager()
# manager.resize(*manager.window.maxsize())	
# plt.show(block=False)	
# plt.savefig("All Cluster Centers.png".format(i),bbox_inches='tight')
# plt.close()


