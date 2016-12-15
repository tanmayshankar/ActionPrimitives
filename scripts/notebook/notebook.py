#!/usr/bin/env python
import numpy as npy
import matplotlib.pyplot as plt
import sys
import random
from scipy import signal
import copy

K = 100
D = 20
T = 20

theta = 1
alpha = 1

number_kernels = 20
number_dimensions = 2
gaussian_kernels = npy.zeros((number_kernels,2))
force_weights = npy.zeros((number_kernels,2))

pos = npy.zeros((T,number_dimensions))
vel = npy.zeros((T,number_dimensions))
acc = npy.zeros((T,number_dimensions))

phi = npy.zeros((T,number_kernels))

gaussian_ker = npy.zeros((20,2))
gaussian_ker[:,0]=0.1
gaussian_ker[:,1]=npy.array(range(20)).astype(float)/20

# def gaussian(x, mu, sig):
#     return npy.exp(-npy.power(x - mu, 2.) / (2 * npy.power(sig, 2.)))

pos = npy.loadtxt("pos_line1.txt")
import numpy as npy
import matplotlib.pyplot as plt
import sys
import random
from scipy import signal
import copy

K = 100
D = 20
T = 20

theta = 1
alpha = 1

number_kernels = 20
number_dimensions = 2
gaussian_kernels = npy.zeros((number_kernels,2))
force_weights = npy.zeros((number_kernels,2))

pos = npy.zeros((T,number_dimensions))
vel = npy.zeros((T,number_dimensions))
acc = npy.zeros((T,number_dimensions))

phi = npy.zeros((T,number_kernels))

gaussian_ker = npy.zeros((20,2))
gaussian_ker[:,0]=0.1
gaussian_ker[:,1]=npy.array(range(20)).astype(float)/20

# def gaussian(x, mu, sig):
#     return npy.exp(-npy.power(x - mu, 2.) / (2 * npy.power(sig, 2.)))

pos = npy.loadtxt("pos_line1.txt")
vel = npy.diff(pos,axis=0)
acc = npy.diff(vel,axis=0)

weights = npy.zeros((20,2))
target_forces = npy.zeros((20,2))

alphaz = 1
betaz = 0.25

def load_pos(line):

	pos = npy.loadtxt("pos_line{0}.txt".format(line))
	vel = npy.diff(pos,axis=0)
	acc = npy.diff(vel,axis=0)

load_pos(1)

def calc_phase(time):
    return npy.exp(-float(time)/T)

def basis(index,time):
	return npy.exp(- gaussian_ker[index,0]*(calc_phase(time)-gaussian_ker[index,1]))

def calc_target_force_vanilla(time):
	return (1./(pos[T-1]-pos[0]))*(-K*pos[time]+D*vel[min(time,vel.shape[0]-1)]+T*acc[min(time,acc.shape[0]-1)])    

def calc_target_force_pastor(time):
	return -(pos[T-1]-pos[time])+(pos[T-1]-pos[0])*calc_phase(time)+(T*acc[min(time,acc.shape[0]-1)]-D*vel[min(time,vel.shape[0]-1)])/K

def calc_target_force_auke(time):
	return (T**2)*acc[min(time,acc.shape[0]-1)] - alphaz*(betaz*(pos[T-1]-pos[time])-T*vel[min(time,vel.shape[0]-1)])

def update_target_force_vanilla():
	for t in range(0,20):
		target_forces[t,:]=calc_target_force_vanilla(t)

def update_target_force_auke():
	for t in range(0,20):
		target_forces[t,:]=calc_target_force_auke(t)/(pos[T-1]-pos[0])

def update_target_force_pastor():
	for t in range(0,20):
		target_forces[t,:]=calc_target_force_pastor(t)

def update_phi():

	for i in range(0,20):
	    for t in range(0,20):
	        det = 0
	        for j in range(0,20):
	            det += basis(j,t)
	        phi[i,t] = basis(i,t)*calc_phase(t)/det

def learn_DMP():            
	update_target_force_pastor()
	update_phi()
	weights = npy.dot(npy.linalg.pinv(phi),target_forces) 

learn_DMP()
