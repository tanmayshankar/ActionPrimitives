#!/usr/bin/env python
from headers import *
# from DMP_Invariant import *

class DMP:
	def __init__(self):

		self.K = 100
		self.D = 2*npy.sqrt(self.K)
		self.T = 20

		self.theta = 1
		self.alpha = 8
		self.tau = self.T

		self.alphaz = 25
		self.betaz = self.alphaz/4

		self.number_kernels = 20
		self.dim = 2		
		self.gaussian_kernels = npy.zeros((self.number_kernels,2))	
		self.weights = npy.zeros((self.number_kernels,self.dim))

		# Assuming 2D data.
		self.pos = npy.zeros((self.T,self.dim))
		self.vel = npy.zeros((self.T,self.dim))
		self.acc = npy.zeros((self.T,self.dim))

		# self.phi = npy.zeros((self.T,self.number_kernels))
		self.target_forces = npy.zeros((self.T,self.dim))
		self.eta = npy.zeros((self.T, self.dim))
		self.phi = npy.zeros((self.number_kernels,self.T,self.T))		

		# Setting variables for Rollouts.	
		self.rollout_T = 30		
		self.pos_roll = npy.zeros((self.rollout_T,self.dim))
		self.vel_roll = npy.zeros((self.rollout_T,self.dim))
		self.acc_roll = npy.zeros((self.rollout_T,self.dim))		
		self.force_roll = npy.zeros((self.rollout_T, self.dim))
		self.goal = npy.zeros(self.dim)
		self.dt = 0.01

	def initialize_gaussian_kernels(self):				
		# t_space = npy.linspace(0,self.T-1,self.T)
		t_space = npy.linspace(0,self.T,self.number_kernels)
		
		# Setting the centers of the Gaussian Kernels. 
		self.gaussian_kernels[:,0] = npy.exp(-self.alpha*t_space/self.tau)
		# self.gaussian_kernels[:,0] = self.calc_phase(t_space)

		# Setting the variances of the Gaussian Kernels.
		self.gaussian_kernels[:,1] = self.number_kernels/self.gaussian_kernels[:,0]	

	def load_pos(self):
		self.pos = npy.load(str(sys.argv[1]))
		self.vel = npy.diff(self.pos,axis=0)
		self.acc = npy.diff(self.vel,axis=0)
		# self.tau = self.pos.shape[0]

	# def load_pos(self, pose):
	# 	self.pos = copy.deepcopy(pose)
	# 	self.vel = npy.diff(self.pos,axis=0)
	# 	self.acc = npy.diff(self.vel,axis=0)
	# 	self.T = self.pos.shape[0]

	def initialize_variables(self):
		self.initialize_gaussian_kernels()
		self.phi = npy.zeros((self.number_kernels,self.T,self.T))
		self.target_forces = npy.zeros((self.T,self.dim))
		self.weights[:,:]=0

	# def basis(self,index,time):
	# 	return npy.exp(-self.gaussian_kernels[index,0]*(self.calc_phase(time)-self.gaussian_kernels[index,1]))

	# def basis(self,index,time):
	# 	return npy.exp(-self.gaussian_kernels[index,0]*(time-self.gaussian_kernels[index,1])**2)

	def basis(self,index,time):
		return npy.exp(-self.gaussian_kernels[index,1]*(self.calc_phase(time)-self.gaussian_kernels[index,0])**2)

	def calc_phase(self ,time):
		# Calculate Theta
		# self.theta = npy.exp(-self.alpha*float(time)/self.T)
		self.theta = npy.exp(-self.alpha*float(time)/self.tau)
		return self.theta

	def calc_target_force_auke(self,time):
		return (self.tau**2)*self.acc[min(time,self.acc.shape[0]-1)] - self.alphaz*(self.betaz*(self.pos[self.T-1]-self.pos[time])-self.tau*self.vel[min(time,self.vel.shape[0]-1)])
		# return self.acc[min(time,self.acc.shape[0]-1)] - self.alphaz*(self.betaz*(self.pos[self.T-1]-self.pos[time])-self.vel[min(time,self.vel.shape[0]-1)])

	def update_target_force_auke(self):
		for t in range(0,self.T):
			self.target_forces[t,:]=self.calc_target_force_auke(t)

	def update_phi(self):
		self.phi = npy.zeros((self.number_kernels,self.T,self.T))		
		for i in range(0,self.number_kernels):
			for t in range(0,self.T):

				self.phi[i,t,t] = self.basis(i,t)			

	def update_eta(self):
		# self.eta[:,:] = 0
		for t in range(self.T):
			self.eta[t,:] = self.calc_phase(t)*(self.pos[self.T-1]-self.pos[0])

	def learn_DMP(self):            
		# print("POS:", self.pos,self.vel, self.acc)
		self.update_target_force_auke()
		# print("TARGET FORCE:",self.target_forces)
		self.update_phi()
		# print("PHI:",self.phi)
		self.update_eta()
		# print("ETA:",self.eta)

		for j in range(0,self.dim):
			for i in range(0,self.number_kernels):
				self.weights[i,j] = npy.dot(self.eta[:,j],npy.dot(self.phi[i],self.target_forces[:,j]))
				self.weights[i,j] /= npy.dot(self.eta[:,j],npy.dot(self.phi[i],self.eta[:,j]))

		print(self.weights)

	def save_DMP_parameters(self,file_suffix):

		with file("force_weights_{0}.npy".format(file_suffix),'w') as outfile:
			npy.save(outfile,self.weights)
	
		with file("position_{0}.npy".format(file_suffix),'w') as outfile:
			npy.save(outfile, self.pos)

	def calc_rollout_force(self,time):
		for i in range(self.number_kernels):
			self.force_roll[time,:] += self.basis(i,time)*self.weights[i,:]						

		self.force_roll[time,:] *= self.calc_phase(time)*(self.goal-self.pos_roll[0,:])

	def calc_rollout_acceleration(self,time):
		self.acc_roll[time,:] = (1/self.tau)*(self.alphaz * (self.betaz * (self.goal - self.pos_roll[time-1,:]) - self.tau*self.vel_roll[time-1,:]) + self.force_roll[time])

	def calc_rollout_vel(self,time):
		self.vel_roll[time,:] = self.vel_roll[time-1,:] + (1/self.tau)*self.acc_roll[time,:]*self.dt

	def calc_rollout_pos(self,time):
		self.pos_roll[time,:] = self.pos_roll[time-1,:] + self.vel_roll[time,:] * self.dt

	def DMP_Rollout(self):

		# For all time: 

		self.calc_rollout_force(roll_time)
		self.calc_rollout_acceleration(roll_time)
		self.calc_rollout_vel(roll_time)
		self.calc_rollout_pos(roll_time)

				
