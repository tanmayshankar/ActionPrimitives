#!/usr/bin/env python
import numpy as npy
import matplotlib.pyplot as plt
import sys
import random
from scipy import signal
import copy
import os

class DMP:
	def __init__(self):

		self.K = 100
		self.D = 2*npy.sqrt(self.K)
		self.T = 20

		self.theta = 1
		self.alpha = 1

		self.alphaz = 1
		self.betaz = 0.25

		self.number_kernels = 20
		self.dim = 2
		self.gaussian_kernels = npy.zeros((self.number_kernels,self.dim))
		self.gaussian_kernels[:,0] = 0.1
		# Setting mean. 
		self.gaussian_kernels[:,1] = npy.array(range(self.number_kernels)).astype(float)/self.number_kernels
		self.weights = npy.zeros((self.number_kernels,self.dim))

		# Assuming 2D data.
		self.pos = npy.zeros((self.T,self.dim))
		self.vel = npy.zeros((self.T,self.dim))
		self.acc = npy.zeros((self.T,self.dim))

		# self.phi = npy.zeros((self.T,self.number_kernels))
		self.target_forces = npy.zeros((self.T,self.dim))
		self.eta = npy.zeros((self.T, self.dim))
		self.phi = npy.zeros((self.number_kernels,self.T, self.T))

	def load_pos(self, pose):
		self.pos = copy.deepcopy(pose)
		self.vel = npy.diff(self.pos,axis=0)
		self.acc = npy.diff(self.vel,axis=0)
		self.T = self.pos.shape[0]

	def initialize_variables(self):
		self.phi = npy.zeros((self.T,self.number_kernels))
		self.target_forces = npy.zeros((self.T,self.dim))
		self.weights[:,:]=0

	def basis(self,index,time):
		return npy.exp(-self.gaussian_kernels[index,0]*(self.calc_phase(time)-self.gaussian_kernels[index,1]))

	def calc_phase(self,time):
		# Calculate Theta
		self.theta = npy.exp(-self.alpha*float(time)/self.T)
		return self.theta

	def calc_target_force_auke(self,time):
		return (self.T**2)*self.acc[min(time,self.acc.shape[0]-1)] - self.alphaz*(self.betaz*(self.pos[self.T-1]-self.pos[time])-self.T*self.vel[min(time,self.vel.shape[0]-1)])

	def update_target_force_auke(self):
		for t in range(0,self.T):
			self.target_forces[t,:]=self.calc_target_force_auke(t)

	def update_phi(self):
		self.phi[:,:,:] = 0
		for i in range(0,self.number_kernels):
			for t in range(0,self.T):
				self.phi[i,t,t] = self.basis(i,t)			

	# def update_phi(self):

	# 	for i in range(0,self.number_kernels):
	# 	    for t in range(0,self.T):
	# 	        det = 0
	# 	        for j in range(0,20):		        	
	# 	        	det += self.basis(j,t)
	# 	        self.phi[i,t] = self.basis(i,t)*self.calc_phase(t)/det		

	def update_eta(self):
		self.eta[:,:] = 0
		for t in range(self.T):
			self.eta[t,:] = self.calc_phase(t)*(self.pos[self.T-1]-self.pos[0])

	def learn_DMP(self):            
		self.update_target_force_auke()
		self.update_phi()
		self.update_eta()

		for j in range(0,self.dim):
			for i in range(0,self.number_kernels):
				self.weights[i,j] = npy.transpose(self.eta[:,j])*(self.phi[i]*self.target_forces[:,j])
				self.weights[i,j] /= npy.transpose(self.eta[:,j])*(self.phi[i]*self.eta[:,j])	

		print(self.weights)

	def save_DMP_parameters(self,file_suffix):

		with file("force_weights_{0}.npy".format(file_suffix),'w') as outfile:
			npy.save(outfile,self.weights)
	
		with file("position_{0}.npy".format(file_suffix),'w') as outfile:
			npy.save(outfile, self.pos)

		with file("phi_{0}.npy".format(file_suffix),'w') as outfile:
			npy.save(outfile, self.phi)			

def main(args):    

	dmp = DMP()
	# dmp.initialize_gaussian_kernels()	
	# dmp.load_pos()
	dmp.initialize_variables()
	dmp.learn_DMP()

if __name__ == '__main__':
    main(sys.argv)
