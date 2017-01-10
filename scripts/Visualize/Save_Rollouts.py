#!/usr/bin/env python
from headers import *

number_trajectories = 20
number_clusters = 40
number_segments = 19
plot_lim = 5

# ROLLING OUT EVERY SEGMENT

# for i in range(0,number_trajectories):
# 	for j in range(0,number_segments):

# 		pos = npy.load("Data/Mouse_Data/Traj_{0}/roll_pos_{1}.npy".format(i,j))

# 		x_min,y_min = npy.min(pos,axis=0)
# 		x_max,y_max = npy.max(pos,axis=0)

# 		fig,ax = plt.subplots()

# 		plt.ylim((min(-plot_lim,y_min),max(plot_lim,y_max)))
# 		plt.xlim((min(-plot_lim,x_min),max(plot_lim,x_max)))
# 		# plt.ylim((-5,5))
# 		# plt.xlim((-5,5))

# 		plt.plot(pos[:,0],pos[:,1])
# 		plt.title("Trajectory {0} Segment {1}".format(i,j))
# 		manager = plt.get_current_fig_manager()
# 		manager.resize(*manager.window.maxsize())
# 		plt.show(block=False)
# 		plt.savefig("Traj_{0}_Segment_{1}.png".format(i,j),bbox_inches='tight')
# 		plt.close()



# # ROLLING OUT CLUSTER CENTERS. 
# # for i in range(0,number_trajectories):
# for i in range(number_clusters):

# 	print("Index",i)
# 	dmp_pos = npy.load("Center/roll_pos_{0}.npy".format(i))
# 	# pos = npy.load("Traj_{0}/pos_{0}.npy".format(i))

# 	# pos -= pos[0]
# 	# pos /= pos[pos.shape[0]-1]	

# 	# x_min,y_min = npy.min(pos,axis=0)
# 	# x_max,y_max = npy.max(pos,axis=0)

# 	dx_min,dy_min = npy.min(dmp_pos,axis=0)
# 	dx_max,dy_max = npy.max(dmp_pos,axis=0)

# 	fig,ax = plt.subplots()

# 	plt.ylim((min(-plot_lim,dy_min),max(plot_lim,dy_max)))
# 	plt.xlim((min(-plot_lim,dx_min),max(plot_lim,dx_max)))

# 	# plt.plot(pos[:,0],pos[:,1],'r')
# 	plt.plot(dmp_pos[:,0],dmp_pos[:,1],'b')
# 	plt.title("Cluster {0}".format(i))
# 	manager = plt.get_current_fig_manager()
# 	manager.resize(*manager.window.maxsize())	
# 	plt.show(block=False)
# 	# plt.draw()
# 	plt.savefig("Cluster_Center_{0}.png".format(i),bbox_inches='tight')
# 	plt.close()





# NORMALIZED ORIGINAL Trajectories

# for i in range(0,number_trajectories):
# 	for j in range(0,number_segments):
# 		pos = npy.load("Data/Mouse_Data/Traj_{0}/position_{1}.npy".format(i,j))

# 		pos -= pos[0]
# 		pos /= pos[pos.shape[0]-1]

# 		x_min,y_min = npy.min(pos,axis=0)
# 		x_max,y_max = npy.max(pos,axis=0)

# 		fig,ax = plt.subplots()

# 		plt.ylim((min(-plot_lim,y_min),max(plot_lim,y_max)))
# 		plt.xlim((min(-plot_lim,x_min),max(plot_lim,x_max)))
# 		# plt.ylim((-5,5))
# 		# plt.xlim((-5,5))

# 		plt.plot(pos[:,0],pos[:,1])
# 		plt.title("Original Trajectory {0} Segment {1}".format(i,j))
# 		manager = plt.get_current_fig_manager()
# 		manager.resize(*manager.window.maxsize())
# 		plt.show(block=False)
# 		plt.savefig("Original_Traj_{0}_Segment_{1}.png".format(i,j),bbox_inches='tight')
# 		plt.close()




# for i in range(0,number_trajectories):
# 	for j in range(0,number_segments):

# 		pos = npy.load("Data/Mouse_Data_New/Traj_{0}/position_{1}.npy".format(i,j))
# 		dmp_pos = npy.load("Data/Mouse_Data_New/Traj_{0}/roll_pos_{1}.npy".format(i,j))
	
# 		# a = (pos[pos.shape[0]-1,0]*pos[pos.shape[0]-1,1])/abs(pos[pos.shape[0]-1,0]*pos[pos.shape[0]-1,1])
# 		print(i,j)
# 		# dmp_pos[:,1] /= a

# 		pos -= pos[0]
# 		pos /= pos[pos.shape[0]-1]

# 		x_min,y_min = npy.min(pos,axis=0)
# 		x_max,y_max = npy.max(pos,axis=0)

# 		dx_min,dy_min = npy.min(dmp_pos,axis=0)
# 		dx_max,dy_max = npy.max(dmp_pos,axis=0)

# 		fig,ax = plt.subplots()

# 		plt.ylim((min(-plot_lim,y_min,dy_min),max(plot_lim,y_max,dy_max)))
# 		plt.xlim((min(-plot_lim,x_min,dx_min),max(plot_lim,x_max,dx_max)))
# 		# plt.ylim((-5,5))
# 		# plt.xlim((-5,5))

# 		plt.plot(pos[:,0],pos[:,1],'r')
# 		plt.plot(dmp_pos[:,0],dmp_pos[:,1],'b')
# 		plt.title("Trajectory {0} Segment {1}".format(i,j))
# 		manager = plt.get_current_fig_manager()
# 		manager.resize(*manager.window.maxsize())	
# 		plt.show(block=False)
# 		# plt.draw()
# 		plt.savefig("Traj_{0}_Segment_{1}.png".format(i,j),bbox_inches='tight')
# 		plt.close()


# PLOT FULL TRAJECTORIES AND ROLLOUTS

for i in range(0,number_trajectories):

	pos = npy.load("Data/Mouse_Data_New/Traj_{0}/pos_{0}.npy".format(i))
	dmp_pos = npy.load("Data/Mouse_Data_New/Trajectory_Rollouts/roll_pos_{0}.npy".format(i))

	# a = (pos[pos.shape[0]-1,0]*pos[pos.shape[0]-1,1])/abs(pos[pos.shape[0]-1,0]*pos[pos.shape[0]-1,1])
	print(i)
	# dmp_pos[:,1] /= a

	pos -= pos[0]
	pos /= pos[pos.shape[0]-1]

	x_min,y_min = npy.min(pos,axis=0)
	x_max,y_max = npy.max(pos,axis=0)

	dx_min,dy_min = npy.min(dmp_pos,axis=0)
	dx_max,dy_max = npy.max(dmp_pos,axis=0)

	fig,ax = plt.subplots()

	plt.ylim((min(-plot_lim,y_min,dy_min),max(plot_lim,y_max,dy_max)))
	plt.xlim((min(-plot_lim,x_min,dx_min),max(plot_lim,x_max,dx_max)))
	# plt.ylim((-5,5))
	# plt.xlim((-5,5))

	plt.plot(pos[:,0],pos[:,1],'r')
	plt.plot(dmp_pos[:,0],dmp_pos[:,1],'b')
	plt.title("Trajectory {0}".format(i))
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())	
	plt.show(block=False)
	# plt.show()
	# plt.draw()
	plt.savefig("Trajectory_{0}.png".format(i),bbox_inches='tight')
	plt.close()


