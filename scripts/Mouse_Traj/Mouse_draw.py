#!/usr/bin/env python
import numpy as npy
import Tkinter as tk
import time
import sys
import os

root = tk.Tk()
prev = 0

# Since the event.time counter runs in Miliseconds. 
time_scale = 1000

# Number of time steps in a trajectory
time_steps = 500
dim = 2

pos1 = npy.zeros((time_steps+2,dim))
time = npy.zeros((time_steps+2))
# vel = npy.zeros((time_steps,dim))
# acc = npy.zeros((time_steps,dim))

counter = 0

def motion(event):
	global prev, counter, root
	
	pos1[counter,0] = event.x
	pos1[counter,1] = event.y
	time[counter] = event.time
	counter +=1 
	print(counter)

root.bind('<Motion>',motion)

while (counter<time_steps+2):
	root.update()
root.destroy()

# pos = npy.zeros((time_steps,dim))
# vel = npy.zeros((time_steps,dim))
# acc = npy.zeros((time_steps,dim))

# FOR MILLISECONDS
time_scale = 1

# # FOR SECONDS
# time_scale = 1000

# DEFINE POSITION
pos = pos1[0:time_steps]

# CALCULATE VELOCITY
vel1 = npy.diff(pos1,axis=0)
dt = npy.diff(time,axis=0)
dt /= time_scale

# DEFINE VELOCITY
vel1[:,0] = vel1[:,0]/dt
vel1[:,1] = vel1[:,1]/dt
vel = vel1[0:time_steps]

# CALCULATE ACCELERATION
acc = npy.diff(vel1,axis=0)
dta = npy.diff(time[1:],axis=0)
dta /= time_scale

acc[:,0] = acc[:,0]/dta
acc[:,1] = acc[:,1]/dta

# pos = pos1[1:1001]

# vel1 = npy.diff(pos1.astype(float),axis=0)
# dt = npy.diff(time)

# for i in range(dim):
# 	vel1[:,i] = vel1[:,i]/dt

# vel = vel1[0:1000]
# dt = dt[0:1000]
# acc1 = npy.diff(pos1.astype(float),axis=0,n=2)
# for i in range(dim):
# 	acc1[:,i] = acc1[:,i]/(dt**2)

# acc = acc1

with file("pos_{0}.npy".format(sys.argv[1]),'w') as outfile:
	npy.save(outfile,pos)

with file("vel_{0}.npy".format(sys.argv[1]),'w') as outfile:
	npy.save(outfile,vel)

with file("acc_{0}.npy".format(sys.argv[1]),'w') as outfile:
	npy.save(outfile,acc)

with file("time_{0}.npy".format(sys.argv[1]),'w') as outfile:
	npy.save(outfile,time)
