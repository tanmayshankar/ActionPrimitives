#!/usr/bin/env python
from headers import *
from variables import *

lhw = npy.load("LH_Meta_Weights.npy")
lhpoints = npy.load("LH_Meta_Points.npy")
lhrollout = npy.load("LH_Meta_Rollout.npy")

rhw = npy.load("RH_Meta_Weights.npy")
rhpoints = npy.load("RH_Meta_Points.npy")
rhrollout = npy.load("RH_Meta_Rollout.npy")

lhlabels = npy.load("LH_clustering_labels.npy")
rhlabels = npy.load("RH_clustering_labels.npy")

lhcenters = npy.load("LH_cluster_centers.npy")
rhcenters = npy.load("RH_cluster_centers.npy")

lh_samples = lhw.shape[0]
rh_samples = rhw.shape[0]

lh_num_clusters = 40
rh_num_clusters = 40

for j in range(lh_samples):
	lhpoints[j] -= lhpoints[j,0]
	lhpoints[j] /= lhpoints[j,-1]

for j in range(rh_samples):
	rhpoints[j] -= rhpoints[j,0]
	rhpoints[j] /= rhpoints[j,-1]

# for i in range(number_clusters):

# 	# ind = npy.where(labels==i)
	
# 	# plt.plot(points[ind,:,0],points[ind,:,1],'r')
# 	# plt.plot(rollout[ind,:,0],rollout[ind,:,1],'b')
# 	# plt.show()

# 	xmin = -2
# 	ymin = -2
# 	xmax = 2
# 	ymax = 2

# 	for j in range(number_samples):
# 		if (labels[j]==i):
# 			plt.plot(points[j,:,0],points[j,:,1],'r',linewidth=1.5)
# 			plt.plot(rollout[j,:,0],rollout[j,:,1],'b',linewidth=1.5)

# 			x_min,y_min = npy.min(points[j,:],axis=0)
# 			x_max,y_max = npy.max(points[j,:],axis=0)

# 			dx_min,dy_min = npy.min(rollout[j,:],axis=0)
# 			dx_max,dy_max = npy.max(rollout[j,:],axis=0)

# 			xmin = min(x_min,xmin,dx_min)
# 			ymin = min(y_min,ymin,dy_min)
# 			xmax = max(x_max,xmax,dx_max)
# 			ymax = max(y_max,ymax,dy_max)

# 	# fig,ax = plt.subplots()
# 	# plt.ylim((min(-plot_lim,ymin),max(plot_lim,ymax)))
# 	# plt.xlim((min(-plot_lim,xmin),max(plot_lim,xmax)))

# 	manager = plt.get_current_fig_manager()	
# 	manager.resize(*manager.window.maxsize())			
# 	plt.title("Cluster {0}".format(i))
# 	plt.show(block=False)
# 	plt.savefig("Cluster_{0}.png".format(i),bbox_inches='tight')		
# 	plt.close()			

# ROLLING OUT CLUSTER CENTERS. 
# for i in range(0,number_trajectories):

for i in range(lh_num_clusters):

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	print("Index",i)	

	dmp_pos = npy.load("Center_Rollouts/LH_roll_pos_{0}.npy".format(i))

	for j in range(lh_samples):
		if (lhlabels[j]==i):			
			ax.plot(lhrollout[j,:,0],lhrollout[j,:,1],lhrollout[j,:,2],'b')

	ax.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2],'r',linewidth=2)
	ax.set_title("LH_Cluster {0}".format(i))
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())	
	plt.show(block=False)	
	plt.savefig("LH_Cluster_Center_{0}.png".format(i),bbox_inches='tight')
	plt.close()

for i in range(rh_num_clusters):

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	print("Index",i)	

	dmp_pos = npy.load("Center_Rollouts/RH_roll_pos_{0}.npy".format(i))

	for j in range(rh_samples):
		if (rhlabels[j]==i):			
			ax.plot(rhrollout[j,:,0],rhrollout[j,:,1],rhrollout[j,:,2],'b')

	ax.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2],'r',linewidth=2)
	ax.set_title("RH_Cluster {0}".format(i))
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())	
	plt.show(block=False)	
	plt.savefig("RH_Cluster_Center_{0}.png".format(i),bbox_inches='tight')
	plt.close()
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


