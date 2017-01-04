#!/usr/bin/env python
from headers import *

number_trajectories = 40
# number_segments = 19

# for i in range(0,number_trajectories):
# 	for j in range(0,number_segments):

# 		pos = npy.load("Data/Mouse_Data/Traj_{0}/roll_pos_{1}.npy".format(i,j))

# 		fig,ax = plt.subplots()
# 		plt.ylim((-5,5))
# 		plt.xlim((-5,5))

# 		plt.plot(pos[:,0],pos[:,1])
# 		plt.title("Trajectory {0} Segment {1}".format(i,j))
# 		manager = plt.get_current_fig_manager()
# 		manager.resize(*manager.window.maxsize())
# 		plt.show(block=False)
# 		plt.savefig("Traj_{0}_Segment_{1}.png".format(i,j),bbox_inches='tight')
# 		plt.close()


for i in range(0,number_trajectories):
	pos = npy.load("Center_Rollouts/roll_pos_{0}.npy".format(i))
	# pos = npy.load("roll_pos_{0}.npy".format(i))

	# fig,ax = plt.subplots()
	# plt.ylim((-5,5))
	# plt.xlim((-5,5))

	plt.plot(pos[:,0],pos[:,1])
	plt.title("Trajectory {0}".format(i))
	manager = plt.get_current_fig_manager()
	manager.resize(*manager.window.maxsize())
	plt.show(block=False)
	plt.savefig("Cluster_{0}.png".format(i),bbox_inches='tight')
	plt.close()