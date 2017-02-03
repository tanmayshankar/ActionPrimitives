#!/usr/bin/env python
from headers import *
from DMP_Segment import *

class Sequence():

	def __init__(self,number_primitives,duration):

		self.number_primitives = number_primitives
		self.duration = duration
		self.primitives = [DMP(duration) for i in range(self.number_primitives)]

		self.overlap_fraction = 0.95
		self.total_time = (self.number_primitives-1)*self.duration*self.overlap_fraction + self.duration

		self.time_points = npy.zeros(self.number_primitives+1)
		self.time_points[-1] = self.total_time

		for i in range(self.number_primitives):
			self.time_points[i] = i*self.overlap_fraction*self.duration

		self.roll_pos = npy.zeros((self.total_time,3))
		self.roll_vel = npy.zeros((self.total_time,3))
		self.roll_acc = npy.zeros((self.total_time,3))

		self.start_seq = npy.zeros((number_primitives,3))
		self.goal_seq = npy.zeros((number_primitives,3))

		self.dt = 1.
		self.tau = self.primitives[0].tau
		self.alphaz = self.primitives[0].alphaz
		self.betaz = self.primitives[0].betaz
		self.blend = npy.zeros(int(self.duration*(1.-self.overlap_fraction)))

	def initialize_variables(self):
		self.blend_function()		

	def sigmoid(self,x):
		return 1./(1.+npy.exp(-x))

	def blend_function(self):		
		tr = npy.linspace(int(self.overlap_fraction*self.duration),self.duration-1,int(self.duration*(1-self.overlap_fraction)))

		for t in range(int(self.duration*(1-self.overlap_fraction))):
			self.blend[t] = self.sigmoid(0.5*(t-((self.overlap_fraction+1.)/2)*self.duration))

	def calc_rollout_acceleration(self,k,time,forcing_term):        
		self.roll_acc[time] = (1/self.tau**2)*(self.alphaz * (self.betaz * (self.goal_seq[k] - self.roll_pos[time]) - self.tau*self.roll_vel[time]) + forcing_term)
        
	def calc_rollout_vel(self,time):		
		self.roll_vel[time] = self.roll_vel[time-1] + self.roll_acc[time-1]*self.dt

	def calc_rollout_pos(self,time):
		self.roll_pos[time] = self.roll_pos[time-1] + self.roll_vel[time-1]*self.dt

	def initialize_meta_rollout(self):
		self.roll_pos[0] = self.start_seq[0]
		self.roll_vel[0] = self.init_vel		

	def meta_rollout(self):

		force = self.primitives[0].calc_rollout_force_time(0,self.roll_pos[0],self.goal_seq[0])
		self.calc_rollout_acceleration(0,0,force)

		for k in range(self.number_primitives):
			for t in range(self.time_points[k],self.time_points[k+1]):
				
				prev_force[:] = 0

				# FORCE BLENDING:
				if (k and (t-self.time_points[k])<((1-self.overlap_fraction)*self.duration)):				
					prev_force = self.primitives[k-1].calc_rollout_force_time(t-self.time_points[k-1],self.roll_pos[self.time_points[k-1]],self.goal_seq[k-1])					
				
				cur_force = self.primitives[k-1].calc_rollout_force_time(t-self.time_points[k],self.roll_pos[self.time_points[k]],self.goal_seq[k])	

				force = (1-self.blend[t-time_points[k]])*prev_force + self.blend[t-time_points[k]]*cur_force

				self.calc_rollout_vel(t)
				self.calc_rollout_pos(t)
				self.calc_rollout_acceleration(k,t,force)

	def save_rollout(self):

		with file('roll_pos.npy','w') as outfile:
			npy.save(outfile,self.roll_pos)

		with file('roll_vel.npy','w') as outfile:
			npy.save(outfile,self.roll_vel)

		with file('roll_acc.npy','w') as outfile:
			npy.save(outfile,self.roll_acc)

	def parse_trajectory(self,traj):
	
		# Must initialize start_sequence and goal_sequence. 

		self.
							




