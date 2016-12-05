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
		self.D = 2* sqrt(self.K)
		self.T = 20

		self.theta = 1
		self.alpha = 1

		self.number_kernels = 10
		self.gaussian_kernels = npy.zeros((number_kernels,2))

		self.force_weights = npy.zeros(number_kernels)

		self.pos = npy.zeros(self.T)
		self.vel = npy.zeros(self.T)
		self.acc = npy.zeros(self.T)

	def calc_phase(self,time):
		# Calculate Theta
		self.theta = npy.exp(-self.alpha*time/self.T)
		return self.theta

	def calc_target_force(self,time):
		# Calculate the target force at a particular time instant.
		return (1/(self.pos[self.T-1]-self.pos[0]))*(-self.K*self.pos[time] + self.D*self.vel[time] + self.T*self.acc[time])

	def gaussian_basis_function(self,index,time):
		# Calculate value of Gaussian basis function. 

		return npy.exp(-self.gaussian_kernels[index,0]*(self.calc_phase(time)-self.gaussian_kernels[index,1])**2)	

	def calc_force(self,time):

		ret = 0
		den = 0
		for i in range(0,self.number_kernels):
			ret += force_weights[i] * gaussian_basis_function(i,time) * calc_phase(time)
			den += gaussian_basis_function(i,time)
		ret /= den
		return ret

	def gradient_step(self,):
		# Update the weights of the Gaussian Combination

		grad = npy.zeros(self.number_kernels)
		
		for t in range(0,self.T):
			grad[i] += 2*(calc_target_force(t) - calc_force(t))*(grad_weight(t))



