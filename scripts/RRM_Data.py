#!/usr/bin/env python
# from RRM_MasterClass import *
from headers import *

class RRM_Data:

	def __init__(self):

		self.number_trajectories = 100
		self.trajectory_length = 100		#Should be same as the time limit?
		self.space_size = 50
		self.dimensions = 2
		self.current_pose = npy.zeros(2)		

		self.Trajectories = npy.zeros((self.number_trajectories,self.trajectory_length,self.dimensions))
		# self.Observations = npy.zeros((self.number_trajectories,self.trajectory_length))
		self.Actions_Taken = npy.zeros((self.number_trajectories,self.trajectory_length))			
		self.Action_Space = npy.array([[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]])
		self.Policy = npy.zeros((self.trajectory_length, self.space_size, self.space_size))

	def generate_trajectory(self, trajectory_index):

		self.Trajectories[trajectory_index, 0, 0] = random.randrange(0,self.space_size)
		self.Trajectories[trajectory_index, 0, 1] = random.randrange(0,self.space_size)
		
		for i in range(0,self.trajectory_length-1):
			# self.Trajectories()												
			self.Actions_Taken[trajectory_index, i] = self.Policy[i,self.Trajectories[trajectory_index, i, 0],self.Trajectories[trajectory_index, i, 1]]
			self.Trajectories[trajectory_index, i+1] = self.Trajectories[trajectory_index,i] + self.Action_Space[self.Actions_Taken[trajectory_index,i]]			

	def generate_trajectories(self):

		for k in range(0,self.number_trajectories):
			self.generate_trajectory(k)

	def load_policy(self):
		self.Policy = npy.reshape(npy.loadtxt(str(sys.argv[1])),(self.trajectory_length+10,self.space_size, self.space_size))

	def load_trajectories(self):
		self.Trajectories = npy.reshape(npy.loadtxt(str(sys.argv[1])),(self.number_trajectories,self.trajectory_length,self.dimensions))
		self.Actions_Taken = npy.reshape(npy.loadtxt(str(sys.argv[2])),(self.number_trajectories,self.trajectory_length))

	def load_trajectory_arg(self,traj,act):
		self.Trajectories = npy.reshape(traj,(self.number_trajectories,self.trajectory_length,self.dimensions))
		self.Actions_Taken = npy.reshape(act,(self.number_trajectories,self.trajectory_length))

	def save_trajectories(self):

		with file('Trajectories.txt','w') as outfile:
			outfile.write('# New slice\n')
			for data_slice in self.Trajectories:
				outfile.write('#Trajectory.\n')
				npy.savetxt(outfile,data_slice,fmt='%i')
			
		with file('Actions_Taken.txt','w') as outfile:
			for data_slice in self.Actions_Taken:
				outfile.write('#Actions Taken.\n')
				npy.savetxt(outfile,data_slice,fmt='%i')

def main(args):    
	# RRM_model = RRM_Model()
	RRM_data = RRM_Data()
	RRM_data.load_policy()
	RRM_data.generate_trajectories()
	RRM_data.save_trajectories()
	# RRM_model.recurrent_value_iteration()	


if __name__ == '__main__':
    main(sys.argv)
