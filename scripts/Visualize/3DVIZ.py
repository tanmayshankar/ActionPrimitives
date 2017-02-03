# coding: utf-8
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd Data/Cornell_Data/Primitive_Library/Subject1/')
get_ipython().magic(u'ls ')
x= npy.load("lh_nb_meta_weight_file.npy")
from ../../../../scripts/Learn_DMP/headers.py import *
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ../../scripts/Learn_DMP/')
from headers import *
get_ipython().magic(u'cd ../../Data/Cornell_Data/Primitive_Library/Subject1/')
get_ipython().magic(u'ls ')
lh = npy.load("lh_nb_meta_weight_file.npy")
npy.where(npy.isnan(lh),axis=1)
npy.where(npy.isnan(lh))
npy.where(npy.isnan(lh))[0]
lh.shape
get_ipython().magic(u'pinfo npy.where')
npy.where(npy.isnan(lh))
npy.where(npy.isnan(lh))[0]
npy.argwhere(npy.isnan(lh))
npy.argwhere(npy.isnan(lh))[0]
npy.argwhere(npy.isnan(lh))[1]
lh.shape
npy.where(npy.isnan(lh[:,0,:]))
npy.where(npy.isnan(lh[:,0,:]))[0]
a = npy.where(npy.isnan(lh[:,0,:]))[0]
for i in range(500):
    if i in a:
        print(i)
        
rh = npy.load("rh_nb_meta_weight_file.npy")
npy.where(npy.isnan(rh))
get_ipython().magic(u'ls ')
a = npy.where(npy.isnan(lh[:,0,:]))[0]
a
len(a)
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Meta/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ls')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
plt
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
npy.load("oblh_cluster_centers.npy","oblh_clustering_labels.npy")
a,b=npy.load("oblh_cluster_centers.npy","oblh_clustering_labels.npy")
cluster_centers = npy.load("nblh_cluster_centers.npy")
centers = npy.load("nblh_cluster_centers.npy")
labels = npy.load("nblh_clustering_labels.npy")
labels
get_ipython().magic(u'pwd ')
labels.shape
embed = npy.load("nblh_embedded_weights.npy")
embed.shape
plt.scatter(embed[:,0],embed[:,1],s=400,c=labels)
plt.show())
plt.show()
centers = npy.load("oblh_cluster_centers.npy")
labels = npy.load("oblh_clustering_labels.npy")
embed = npy.load("oblh_embedded_weights.npy")
plt.scatter(embed[:,0],embed[:,1],s=400,c=labels)
plt.show()
plt.scatter(embed[:,0],embed[:,1],s=400,c=labels)
plt.title("Embedded Weights: Old Bases, Left Hand.")
plt.show()
plt.title("Embedded Weights: Old Bases, Left Hand.")
plt.show(block=False)
plt.scatter(embed[:,0],embed[:,1],s=400,c=labels)
plt.title("Embedded Weights: Old Bases, Left Hand.")
plt.show(block=False)
plt.savefig("Embedded_Weights_LH_OB.png",bbox_inches='tight')
get_ipython().magic(u'ls ')
centers = npy.load("obrh_cluster_centers.npy")
embed = npy.load("obrh_embedded_weights.npy")
labels = npy.load("obrh_clustering_labels.npy")
plt.scatter(embed[:,0],embed[:,1],s=400,c=labels)
plt.title("Embedded Weights: Old Bases, Right Hand.")
plt.show(block=False)
plt.scatter(embed[:,0],embed[:,1],s=400,c=labels)
plt.title("Embedded Weights: Old Bases, Right Hand.")
plt.show(block=False)
plt.savefig("Embedded_Weights_RH_OB.png",bbox_inches='tight')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pinfo os.path.split')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Clusters/')
get_ipython().magic(u'ls ')
os.path.split("nblh_cluster_centers.npy")
os.path.split("/nblh_cluster_centers.npy")
get_ipython().magic(u'cd ..')
os.path.split("Clusters/nblh_cluster_centers.npy")
get_ipython().magic(u'pinfo os.pathsep')
get_ipython().magic(u'pinfo os.path.sep')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Clusters/')
get_ipython().magic(u'ls ')
centers = npy.load("oblh_cluster_centers.npy")
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Meta/')
get_ipython().magic(u'ls ')
rollout = npy.load("lh_ob_meta_rollout.npy")
rollout.shape
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd Clusters/')
get_ipython().magic(u'ls ')
labels = npy.load("oblh_clustering_labels.npy")
labels.shape
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls Center/')
number_clusters = 40
number_samples
number_samples = labels.shape[0]
number_samples
for i in range(number_clusters):

	print("Index",i)
	# dmp_pos = npy.load("Cluster_Center/roll_pos_{0}.npy".format(i))
	dmp_pos = npy.load("Center/lhob_roll_pos_{0}.npy".format(i))
	x_min,y_min = npy.min(dmp_pos,axis=0)
	x_max,y_max = npy.max(dmp_pos,axis=0)

	xmin = -5
	ymin = -5
	xmax = 5
	ymax = 5

	for j in range(number_samples):
		if (labels[j]==i):			
			plt.plot(rollout[j,:,0],rollout[j,:,1],'b')

			dx_min,dy_min = npy.min(rollout[j,:],axis=0)
			dx_max,dy_max = npy.max(rollout[j,:],axis=0)

			xmin = min(dx_min,xmin)
			ymin = min(dy_min,ymin)
			xmax = max(dx_max,xmax)
			ymax = max(dy_max,ymax)
	
	plt.ylim((min(-plot_lim,y_min,dy_min),max(plot_lim,y_max,dy_max)))
	plt.xlim((min(-plot_lim,x_min,dx_min),max(plot_lim,x_max,dx_max)))

	plt.plot(dmp_pos[:,0],dmp_pos[:,1],'r',linewidth=2)
	plt.title("Cluster {0}".format(i))
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())	
	plt.show(block=False)	
	plt.savefig("Cluster_Center_{0}.png".format(i),bbox_inches='tight')
	plt.close()
dmp_pos
plt.plot(dmp_pos)
plt.show()
plt.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2])
plt.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2])
fig = plt.figure()
ax = fig.gca(projection='3d)
ax = fig.gca(projection='3d')
from mpl_toolkits.mplot3d import Axes3D
ax = fig.gca(projection='3d')
ax.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2])
plt.show()
plt.plot(dmp_pos[:,0],dmp_pos[:,1],dmp_pos[:,2])
ax.plt(dmp_pos)
ax.plot(dmp_pos)
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
	plt.show(block=False)	
	plt.savefig("Cluster_Center_{0}.png".format(i),bbox_inches='tight')
	plt.close()
get_ipython().magic(u'ls ')
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
 
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ')
get_ipython().magic(u'cd Research/Code/ActionPrimitives/')
get_ipython().magic(u'save 3DVIZ.py 1-150')
