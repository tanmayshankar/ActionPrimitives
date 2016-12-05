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

	def calc_target_force(self):




		

