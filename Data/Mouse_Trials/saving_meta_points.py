# coding: utf-8
import numpy as npy
import matplotlib.pyplot as plt
import sys
import random
from scipy import signal
import copy

reward = npy.load("Learnt_Reward.npy")
trans = npy.load("Transition_Model.npy")

temporal_policy = npy.zeros((100,20,50,50))
temporal_value = npy.zeros((100,20,50,50))
temporal_Qvalue = npy.zeros((100,20,8,50,50))

policy = npy.zeros((100,50,50))
value = npy.zeros((100,50,50))
Qvalue = npy.zeros((100,8,50,50))

IS_value = npy.zeros((100,50,50))
# IS_policy = npy.zeros((100,50,50))
IS_Qvalue = npy.zeros((100,8,50,50))

Traj = npy.loadtxt("Trajectories_SQ.txt").reshape(100,100,2)
traj = Traj[0]

Actions_Taken = npy.loadtxt("Actions_Taken_SQ.txt").reshape(100,100)
acts = Actions_Taken[0]

observation_model = npy.array([[0.,0.05,0.],[0.05,0.8,0.05],[0.,0.05,0.]])
w=1

loss_values = npy.zeros((100,20))
number_actions =4 


def show_image(image_arg):		
	plt.imshow(image_arg, interpolation='nearest', origin='lower', extent=[0,50,0,50], aspect='auto')		
	plt.colorbar()
	plt.show() 

def IS_convolution_layer(time_index):

	for act in range(0,number_actions):
		IS_Qvalue[time_index, act] = signal.convolve2d(IS_value[time_index],trans[act],'same')

def IS_action_pooling(time_index):
	IS_value[time_index] = npy.max(IS_Qvalue[time_index],axis=0)	

def IS_reward_bias(time_index):
	IS_Qvalue[time_index] += reward[time_index]

def IS_value_iteration():
	
	for t in range(0,100):
		print(t)
		for k in range(0,50):
			IS_convolution_layer(t)
			IS_reward_bias(t)
			IS_action_pooling(t)

def convolution_layer(time_index, m_index):	
	for act in range(0,number_actions):			
		temporal_Qvalue[time_index,m_index,act] = signal.convolve2d(temporal_value[time_index,m_index-1],trans[act],'same','fill',0)

def action_pooling(time_index,m_index):
	temporal_value[time_index,m_index]  = npy.max(temporal_Qvalue[time_index, m_index],axis=0)

def reward_bias(time_index, m_index):		
	temporal_Qvalue[time_index,m_index] += reward[min(99,time_index+m_index)]		

def recurrent_value_iteration():

	for t in range(0,100):
		print(t)
		for k in range(0,20):
	
			m = 20-k-1
			convolution_layer(t,m)	
			reward_bias(t, m)
			action_pooling(t, m)

		policy[t] = temporal_policy[t, 0]		
		value[t] = temporal_value[t, 0]
		Qvalue[t] = temporal_Qvalue[t, 0]


IS_value_iteration()
recurrent_value_iteration()

def temporal_QMDP_actions(time_index,m_index):
	IS_net_act = npy.zeros(number_actions)
	for act in range(0,number_actions):
		# IS_net_act[act] = npy.sum(IS_Qvalue[time_index,act] * belief)

		IS_net_act[act] = npy.sum(IS_Qvalue[min(99,time_index+m_index),act] * belief)
		
	IS_net_act = npy.exp(IS_net_act)/npy.sum(npy.exp(IS_net_act))


	print("Time Index", time_index, IS_net_act, acts[time_index])
	return IS_net_act


# def QMDP_action_selection(time_index):	
# 	for act in range(0,number_actions):


# 		self.network_actions[act] = npy.sum(self.Qvalue[time_index, act] * self.belief)

# 	#IMPLEMENT THE DAMN SOFTMAX!
# 	sfmx_den = npy.sum(npy.exp(self.network_actions[:]))		

# 	for act in range(0,self.action_size):
# 		self.network_actions[act] = npy.exp(self.network_actions[act])/sfmx_den			

# def loss_function(time_index, m_index):
	
# 	return -npy.sum()

# 	return -npy.sum(self.belief_target_actions*npy.log(self.network_actions))		

belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(0,100):
	belief[:,:]=0
	belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions(t,m)
		loss_values[t,m] = -npy.log(x[acts[t]])

temporal_policy = npy.zeros((100,20,50,50))
temporal_value = npy.zeros((100,20,50,50))
temporal_Qvalue = npy.zeros((100,20,8,50,50))

policy = npy.zeros((100,50,50))
value = npy.zeros((100,50,50))
Qvalue = npy.zeros((100,8,50,50))

IS_value = npy.zeros((100,50,50))
# IS_policy = npy.zeros((100,50,50))
IS_Qvalue = npy.zeros((100,8,50,50))

Traj = npy.loadtxt("Trajectories_SQ.txt").reshape(100,100,2)
traj = Traj[0]

Actions_Taken = npy.loadtxt("Actions_Taken_SQ.txt").reshape(100,100)
acts = Actions_Taken[0]

observation_model = npy.array([[0.,0.05,0.],[0.05,0.8,0.05],[0.,0.05,0.]])
w=1

ax_ch = npy.zeros((100,20,4))

loss_values = npy.zeros((100,20))
number_actions =4 


def show_image(image_arg):		
	plt.imshow(image_arg, interpolation='nearest', origin='lower', extent=[0,50,0,50], aspect='auto')		
	plt.colorbar()
	plt.show() 

def IS_convolution_layer(time_index):

	for act in range(0,number_actions):
		IS_Qvalue[time_index, act] = signal.convolve2d(IS_value[time_index],trans[act],'same')

def IS_action_pooling(time_index):
	IS_value[time_index] = npy.max(IS_Qvalue[time_index],axis=0)	

def IS_reward_bias(time_index):
	IS_Qvalue[time_index] += reward[time_index]

def IS_value_iteration():
	
	for t in range(0,100):
		print(t)
		for k in range(0,50):
			IS_convolution_layer(t)
			IS_reward_bias(t)
			IS_action_pooling(t)

def convolution_layer(time_index, m_index):	
	for act in range(0,number_actions):			
		temporal_Qvalue[time_index,m_index,act] = signal.convolve2d(temporal_value[time_index,m_index-1],trans[act],'same','fill',0)

def action_pooling(time_index,m_index):
	temporal_value[time_index,m_index]  = npy.max(temporal_Qvalue[time_index, m_index],axis=0)

def reward_bias(time_index, m_index):		
	temporal_Qvalue[time_index,m_index] += reward[min(99,time_index+m_index)]		

def recurrent_value_iteration():

	for t in range(0,100):
		print(t)
		for k in range(0,20):
	
			m = 20-k-1
			convolution_layer(t,m)	
			reward_bias(t, m)
			action_pooling(t, m)

		policy[t] = temporal_policy[t, 0]		
		value[t] = temporal_value[t, 0]
		Qvalue[t] = temporal_Qvalue[t, 0]


IS_value_iteration()
recurrent_value_iteration()

def temporal_QMDP_actions(time_index,m_index):
	IS_net_act = npy.zeros(number_actions)
	for act in range(0,number_actions):
		# IS_net_act[act] = npy.sum(IS_Qvalue[time_index,act] * belief)

		IS_net_act[act] = npy.sum(IS_Qvalue[min(99,time_index+m_index),act] * belief)
		
	IS_net_act = npy.exp(IS_net_act)/npy.sum(npy.exp(IS_net_act))


	print("Time Index", time_index, IS_net_act, acts[time_index])
	return IS_net_act


# def QMDP_action_selection(time_index):	
# 	for act in range(0,number_actions):


# 		self.network_actions[act] = npy.sum(self.Qvalue[time_index, act] * self.belief)

# 	#IMPLEMENT THE DAMN SOFTMAX!
# 	sfmx_den = npy.sum(npy.exp(self.network_actions[:]))		

# 	for act in range(0,self.action_size):
# 		self.network_actions[act] = npy.exp(self.network_actions[act])/sfmx_den			

# def loss_function(time_index, m_index):
	
# 	return -npy.sum()

# 	return -npy.sum(self.belief_target_actions*npy.log(self.network_actions))		

belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(0,100):
	belief[:,:]=0
	belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions(t,m)
		ax_ch[t,m,:] = x
		loss_values[t,m] = -npy.log(x[acts[t]])
ax_c
ax_ch
npy.max(ax_ch)
npy.max(ax_ch,axis=2)
npy.max(ax_ch,axis=2).shape
for t in range(0,100):
    print(t)
    plt.bar(npy.linspace(0,19,20),npy.max(ax_ch,axis=2))
    plt.show()
for t in range(0,100):
    print(t)
    x = npy.max(ax_ch,axis=2)
    plt.bar(npy.linspace(0,19,20),x[t])
    plt.show()
for t in range(90,100):
    print(t)
    x = npy.max(ax_ch,axis=2)
    plt.bar(npy.linspace(0,19,20),x[t])
    plt.show()
traj
acts
for t in range(0,20):
    plt.plot(IS_Qvalue[5*t,0])
    plt.show9)
for t in range(0,20):
    plt.plot(IS_Qvalue[5*t,0])
    plt.show()
    
for t in range(0,20):
    plt.imshow(IS_Qvalue[5*t,0])
    plt.show()
    
for t in range(0,20):
    print(5*t)
    plt.imshow(IS_Qvalue[5*t,0])
    plt.show()
    
for t in range(0,20):
    print(5*t)
    show_image(IS_Qvalue[5*t,0])
      
for t in range(0,20):
    print(5*t)
    show_image(IS_Qvalue[5*t,0])
      
ax_ch
x
ax_ch.shape
for i in range(0,100):
    plt.imshow(ax_ch[i])
    plt.show()
    
def show_image(image_arg):		
	plt.imshow(image_arg, interpolation='nearest', origin='lower', aspect='auto')		
	plt.colorbar()
	plt.show() 
 
for i in range(0,100):
    show_image(ax_ch[i])
    
for i in range(0,100):
    print(t)
    show_image(ax_ch[i])
    
for t in range(0,100):
    print(t)
    show_image(ax_ch[t])
    
for t in range(0,20):
    print(t*5)
    show_image(IS_Qvalue[5*t,0])
    show_image(IS_Qvalue[5*t,1])
    
for t in range(0,20):
    print(t*5)
    show_image(IS_Qvalue[5*t,0])
    show_image(IS_Qvalue[5*t,1])
    
npy.argmax(ax_ch,axis=2)
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
def temporal_QMDP_actions_show(time_index,m_index):
	IS_net_act = npy.zeros(number_actions)
	
	for act in range(0,number_actions):		
		IS_net_act[act] = npy.sum(IS_Qvalue[min(99,time_index+m_index),act] * belief)
		
	IS_net_act = npy.exp(IS_net_act)/npy.sum(npy.exp(IS_net_act))
    show_image(belief)
	show_image(IS_Qvalue[time_index,npy.argmax(IS_net_act)])

	print("Time Index", time_index, IS_net_act, acts[time_index])
	return IS_net_act
def temporal_QMDP_actions_show(time_index,m_index):
    IS_net_act = npy.zeros(number_actions)
    for act in range(0,number_actions):
        IS_net_act[act] = npy.sum(IS_Qvalue[min(99,time_index+m_index),act] * belief)

    IS_net_act = npy.exp(IS_net_act)/npy.sum(npy.exp(IS_net_act))
    show_image(belief)
    show_image(IS_Qvalue[time_index,npy.argmax(IS_net_act)])

    print("Time Index", time_index, IS_net_act, acts[time_index])
    return IS_net_act
belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(0,100):
	belief[:,:]=0
	belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions_show(t,m)
		ax_ch[t,m,:] = x
		loss_values[t,m] = -npy.log(x[acts[t]])
belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(0,100):
	print(t)
	belief[:,:]=0
	belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions_show(t,m)
		ax_ch[t,m,:] = x
		loss_values[t,m] = -npy.log(x[acts[t]])
  
for t in range(0,100):
    print(t)
    show_image(reward[t,0])
    show_image(reward[t,1])
    
belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(0,99):
	print(t)
	belief[:,:]=0
	belief[traj[t+1,0]-w:traj[t+1,0]+w+1,traj[t+1,1]-w:traj[t+1,1]+w+1] = observation_model
	# belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions_show(t,m)
		ax_ch[t,m,:] = x
		loss_values[t,m] = -npy.log(x[acts[t]])
belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(0,99):
	print(t)
	belief[:,:]=0
	belief[traj[t+1,0]-w:traj[t+1,0]+w+1,traj[t+1,1]-w:traj[t+1,1]+w+1] = observation_model
	# belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions(t,m)
		ax_ch[t,m,:] = x
		loss_values[t,m] = -npy.log(x[acts[t]])
belief = npy.zeros((50,50))
loss_values = npy.zeros((100,20))
for t in range(1,100):
	print(t)
	belief[:,:]=0
	belief[traj[t-1,0]-w:traj[t-1,0]+w+1,traj[t-1,1]-w:traj[t-1,1]+w+1] = observation_model
	# belief[traj[t+1,0]-w:traj[t+1,0]+w+1,traj[t+1,1]-w:traj[t+1,1]+w+1] = observation_model
	# belief[traj[t,0]-w:traj[t,0]+w+1,traj[t,1]-w:traj[t,1]+w+1] = observation_model

	for m in range(0,20):
		x = temporal_QMDP_actions(t,m)
		ax_ch[t,m,:] = x
		loss_values[t,m] = -npy.log(x[acts[t]])
get_ipython().magic(u'ls ')
for i in range(0,10):
    print(i*(10),(i+1)*20-i*10)
    
import pygame
import matplotlib.pyplot as plt

def onclick(event):
    print(event.xdata, event.ydata)
    
fig,ax = plt.subplots()
ax.plot(range(10))
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

class LineBuilder:
    def __init__(self, line,ax,color):
        self.line = line
        self.ax = ax
        self.color = color
        self.xs = []
        self.ys = []
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.counter = 0
        self.shape_counter = 0
        self.shape = {}
        self.precision = 10

    def __call__(self, event):
        if event.inaxes!=self.line.axes: return
        if self.counter == 0:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
        if np.abs(event.xdata-self.xs[0])<=self.precision and np.abs(event.ydata-self.ys[0])<=self.precision and self.counter != 0:
            self.xs.append(self.xs[0])
            self.ys.append(self.ys[0])
            self.ax.scatter(self.xs,self.ys,s=120,color=self.color)
            self.ax.scatter(self.xs[0],self.ys[0],s=80,color='blue')
            self.ax.plot(self.xs,self.ys,color=self.color)
            self.line.figure.canvas.draw()
            self.shape[self.shape_counter] = [self.xs,self.ys]
            self.shape_counter = self.shape_counter + 1
            self.xs = []
            self.ys = []
            self.counter = 0
        else:
            if self.counter != 0:
                self.xs.append(event.xdata)
                self.ys.append(event.ydata)
            self.ax.scatter(self.xs,self.ys,s=120,color=self.color)
            self.ax.plot(self.xs,self.ys,color=self.color)
            self.line.figure.canvas.draw()
            self.counter = self.counter + 1

def create_shape_on_image(data,cmap='jet'):
    def change_shapes(shapes):
        new_shapes = {}
        for i in range(len(shapes)):
            l = len(shapes[i][1])
            new_shapes[i] = np.zeros((l,2),dtype='int')
            for j in range(l):
                new_shapes[i][j,0] = shapes[i][0][j]
                new_shapes[i][j,1] = shapes[i][1][j]
        return new_shapes
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('click to include shape markers (10 pixel precision to close the shape)')
    line = ax.imshow(data) 
    ax.set_xlim(0,data[:,:,0].shape[1])
    ax.set_ylim(0,data[:,:,0].shape[0])
    linebuilder = LineBuilder(line,ax,'red')
    plt.gca().invert_yaxis()
    plt.show()
    new_shapes = change_shapes(linebuilder.shape)
    return new_shapes

img = np.zeros((100,100,3),dtype='uint')
shapes = create_shape_on_image(img)[0]
print(shapes)
import numpy as np
import matplotlib.pyplot as plt

class LineBuilder:
    def __init__(self, line,ax,color):
        self.line = line
        self.ax = ax
        self.color = color
        self.xs = []
        self.ys = []
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.counter = 0
        self.shape_counter = 0
        self.shape = {}
        self.precision = 10

    def __call__(self, event):
        if event.inaxes!=self.line.axes: return
        if self.counter == 0:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
        if np.abs(event.xdata-self.xs[0])<=self.precision and np.abs(event.ydata-self.ys[0])<=self.precision and self.counter != 0:
            self.xs.append(self.xs[0])
            self.ys.append(self.ys[0])
            self.ax.scatter(self.xs,self.ys,s=120,color=self.color)
            self.ax.scatter(self.xs[0],self.ys[0],s=80,color='blue')
            self.ax.plot(self.xs,self.ys,color=self.color)
            self.line.figure.canvas.draw()
            self.shape[self.shape_counter] = [self.xs,self.ys]
            self.shape_counter = self.shape_counter + 1
            self.xs = []
            self.ys = []
            self.counter = 0
        else:
            if self.counter != 0:
                self.xs.append(event.xdata)
                self.ys.append(event.ydata)
            self.ax.scatter(self.xs,self.ys,s=120,color=self.color)
            self.ax.plot(self.xs,self.ys,color=self.color)
            self.line.figure.canvas.draw()
            self.counter = self.counter + 1

def create_shape_on_image(data,cmap='jet'):
    def change_shapes(shapes):
        new_shapes = {}
        for i in range(len(shapes)):
            l = len(shapes[i][1])
            new_shapes[i] = np.zeros((l,2),dtype='int')
            for j in range(l):
                new_shapes[i][j,0] = shapes[i][0][j]
                new_shapes[i][j,1] = shapes[i][1][j]
        return new_shapes
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('click to include shape markers (10 pixel precision to close the shape)')
    line = ax.imshow(data) 
    ax.set_xlim(0,data[:,:,0].shape[1])
    ax.set_ylim(0,data[:,:,0].shape[0])
    linebuilder = LineBuilder(line,ax,'red')
    plt.gca().invert_yaxis()
    plt.show()
    new_shapes = change_shapes(linebuilder.shape)
    return new_shapes

img = np.zeros((100,100,3),dtype='uint')
shapes = create_shape_on_image(img)[0]
print(shapes)
import matplotlib.pyplot as plt

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	
	counter +=1

	points[counter,0] = event.xdata
	points[counter,1] = event.ydata


print(points)

fig,ax = plt.subplots()
ax.plot(range(10))
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

print(points)

import matplotlib.pyplot as plt

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	global counter, points

	counter +=1

	points[counter,0] = event.xdata
	points[counter,1] = event.ydata

fig,ax = plt.subplots()
ax.plot(range(10))
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

print(points)
points
num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	global counter, points

	counter +=1

	points[counter,0] = event.xdata
	points[counter,1] = event.ydata

fig,ax = plt.subplots()
# ax.plot(range(50))
ax.plot()
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
points
num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	global counter, points

	counter +=1

	points[counter,0] = event.xdata
	points[counter,1] = event.ydata

fig,ax = plt.subplots()
ax.plot(range(50))
# ax.plot()
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
points

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	global counter, points
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata	
	counter+=1

fig,ax = plt.subplots()
ax.plot(range(50))
# ax.plot()
plt.plot(points[:,0],points[:,1])
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
import matplotlib.pyplot as plt

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	global counter, points
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata	
	plt.plot(points[counter,0],points[counter,1])
	counter+=1
	
fig,ax = plt.subplots()
ax.plot(range(50))
# ax.plot()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
import matplotlib.pyplot as plt

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

def onclick(event): 
	global counter, points
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata	
	plt.plot(points[counter,0],points[counter,1])
	plt.show()
	counter+=1
	
fig,ax = plt.subplots()
ax.plot(range(50))
# ax.plot()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
import matplotlib.pyplot as plt
import numpy as npy
import sys

num_points = 100
num_points = 100
points = npy.zeros((num_points,2))
counter = 0
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd ActionPrimitives/')
get_ipython().magic(u'ls ')
def onclick(event): 
	global counter, points
	print(counter)
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata		
	counter+=1

fig,ax = plt.subplots()
ax.plot(range(50))
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
points
with file("points_{0}.npy".format(sys.argv[1]),'w') as outfile:
	npy.save(outfile,points)
 
get_ipython().magic(u'pinfo plt.close')
num_points = 100
points = npy.zeros((num_points,2))
counter = 0

fig,ax = plt.subplots()
ax.plot(range(50))

def onclick(event): 
	global counter, points
	print(counter)
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata		
	counter+=1

	if (counter==99)
		plt.close()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

fig,ax = plt.subplots()
ax.plot(range(50))

def onclick(event): 
	global counter, points
	print(counter)
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata		
	counter+=1

	if (counter==99):
		plt.close()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
points
pxs = npy.load("points_0.npy")
pxs
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd Data/Mouse_Trials/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls points_0/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd .')
get_ipython().magic(u'cd Mouse_Trials/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd points_0/')
get_ipython().magic(u'ls ')
w = npy.load("force_weights_0.npy")
w.shape
get_ipython().magic(u'ls ')
weights
weights = npy.zeros((81,20,2))
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'ls ')
for i in range(0,9):
    for j in range(0,9):
        weights[9*i+j] = npy.load("points_{0}/force_weights_{1}.npy".format(i,j))
        
weights
weights.shape
get_ipython().magic(u'ls ')
with file("meta_weight_file.npy",'w') as outfile:
    npy.save(outfile,weights)
    
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls ')
