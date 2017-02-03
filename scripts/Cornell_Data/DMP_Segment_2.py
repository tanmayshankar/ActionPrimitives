#!/usr/bin/env python
from headers import *

class DMP():
	
	def __init__(self,timesteps=100):

		self.alphaz = 25.0
		self.betaz = self.alphaz/4
		self.alpha = 1*self.alphaz/3    
        
		self.time_steps = timesteps
		self.tau = self.time_steps

		self.dimensions = 3
		self.number_kernels = 100
		self.gaussian_kernels = npy.zeros((self.number_kernels,2))

		self.weights = npy.zeros((self.number_kernels, self.dimensions))

		self.demo_pos = npy.zeros((self.time_steps, self.dimensions))
		self.demo_vel = npy.zeros((self.time_steps, self.dimensions))
		self.demo_acc = npy.zeros((self.time_steps, self.dimensions))

		self.target_forces = npy.zeros((self.time_steps, self.dimensions))        
		self.phi = npy.zeros((self.number_kernels, self.time_steps, self.time_steps))
		self.eta = npy.zeros((self.time_steps, self.dimensions))
		self.vector_phase = npy.zeros(self.time_steps)
        
# Defining Rollout variables.
# 		self.rollout_time = max(self.time_steps,200)
		self.rollout_time = self.time_steps    
		self.dt = 1./self.rollout_time
		self.pos_roll = npy.zeros((self.rollout_time,self.dimensions))
		self.vel_roll = npy.zeros((self.rollout_time,self.dimensions))
		self.acc_roll = npy.zeros((self.rollout_time,self.dimensions))
		self.force_roll = npy.zeros((self.rollout_time,self.dimensions))                
		self.goal = npy.zeros(self.dimensions)
		self.start = npy.zeros(self.dimensions)  
		self.initial_velocity = npy.zeros(self.dimensions)

	def load_trajectory(self,pos,vel,acc):
		self.demo_pos = copy.deepcopy(pos)
		self.demo_vel = copy.deepcopy(vel)
		self.demo_acc = copy.deepcopy(acc)

	def initialize_variables(self):	
		self.weights = npy.zeros((self.number_kernels, self.dimensions))
		self.target_forces = npy.zeros((self.time_steps, self.dimensions))
		self.phi = npy.zeros((self.number_kernels, self.time_steps, self.time_steps))
		self.eta = npy.zeros((self.time_steps, self.dimensions))

		t_range = npy.linspace(0,self.time_steps,self.number_kernels)
		self.vector_phase = self.calc_vector_phase(t_range)
		self.gaussian_kernels[:,0] = self.vector_phase        

# 		self.gaussian_kernels[:,1] = self.number_kernels/self.gaussian_kernels[:,0]       
# 		dummy = (npy.diff(self.gaussian_kernels[:,0]*2))**2        
		dummy = (npy.diff(self.gaussian_kernels[:,0]))**2      
# 		dummy = (npy.diff(self.gaussian_kernels[:,0]*0.55))**2            
		self.gaussian_kernels[:,1] = 1. / npy.append(dummy,dummy[-1])

	def calc_phase(self,time):
		return npy.exp(-self.alpha*float(time)/self.tau)
    
	def calc_vector_phase(self,time):
		return npy.exp(-self.alpha*time.astype(float)/self.tau)

	def basis(self,index,time):
		return npy.exp(-(self.gaussian_kernels[index,1])*((self.calc_phase(time)-self.gaussian_kernels[index,0])**2))

	def update_target_force(self):
		self.target_forces = self.demo_acc - self.alphaz*(self.betaz*(self.demo_pos[self.time_steps-1]-self.demo_pos)-self.demo_vel)
    
  	def update_target_force_itau(self):
		self.target_forces = (self.tau**2)*self.demo_acc - self.alphaz*(self.betaz*(self.demo_pos[self.time_steps-1]-self.demo_pos)-self.tau*self.demo_vel)
        
  	def update_target_force_dtau(self):
		self.target_forces = self.demo_acc/(self.tau**2) - self.alphaz*(self.betaz*(self.demo_pos[self.time_steps-1]-self.demo_pos)-self.demo_vel/self.tau)    

	def update_phi(self):		
		for i in range(self.number_kernels):
			for t in range(self.time_steps):
				self.phi[i,t,t] = self.basis(i,t)                
                
	def update_eta(self):        
		t_range = npy.linspace(0,self.time_steps,self.time_steps)        
		vector_phase = self.calc_vector_phase(t_range)        
        
		for k in range(self.dimensions):
			self.eta[:,k] = vector_phase*(self.demo_pos[-1,k]-self.demo_pos[0,k])

	def learn_DMP(self):	
		self.update_target_force_itau()        
		self.update_phi()
		self.update_eta()

		for j in range(self.dimensions):
			for i in range(self.number_kernels):
				self.weights[i,j] = npy.dot(self.eta[:,j],npy.dot(self.phi[i],self.target_forces[:,j]))
				self.weights[i,j] /= npy.dot(self.eta[:,j],npy.dot(self.phi[i],self.eta[:,j]))
            
	def shebang(self,pos,vel,acc):
		dmp.load_trajectory(pos,vel,acc)
		dmp.initialize_variables()
		dmp.learn_DMP() 
        
	def initialize_rollout(self,start,goal,init_vel):
		self.tau = self.rollout_time        
		self.pos_roll[0] = copy.deepcopy(start)        
		self.vel_roll[0] = copy.deepcopy(init_vel)
		self.goal = goal
		self.start = start
		self.dt = self.tau/self.rollout_time        
		print(self.dt)

	def calc_rollout_force(self,roll_time):
		den = 0        
		time = copy.deepcopy(roll_time)        
		for i in range(self.number_kernels):
			self.force_roll[roll_time] += self.basis(i,time)*self.weights[i]
			den += self.basis(i,time)
		self.force_roll[roll_time] *= (self.goal-self.start)*self.calc_phase(time)/den
            
	def calc_rollout_acceleration(self,time):        
		self.acc_roll[time] = (1./self.tau**2)*(self.alphaz * (self.betaz * (self.goal - self.pos_roll[time]) - self.tau*self.vel_roll[time]) + self.force_roll[time])    
        
	def calc_rollout_vel(self,time):
		self.vel_roll[time] = self.vel_roll[time-1] + self.acc_roll[time-1]*self.dt

	def calc_rollout_pos(self,time):
		self.pos_roll[time] = self.pos_roll[time-1] + self.vel_roll[time-1]*self.dt
    
	def rollout(self,start,goal,init_vel):

		self.initialize_rollout(start,goal,init_vel)        
		self.calc_rollout_force(0)
		self.calc_rollout_acceleration(0)  
		for i in range(1,self.rollout_time):        
			self.calc_rollout_force(i)     
			self.calc_rollout_vel(i)                     
			self.calc_rollout_pos(i)                                
			self.calc_rollout_acceleration(i) 

	def save_rollout(self):

		with file('roll_pos.npy','w') as outfile:
			npy.save(outfile,self.pos_roll)

		with file('roll_vel.npy','w') as outfile:
			npy.save(outfile,self.vel_roll)

		with file('roll_acc.npy','w') as outfile:
			npy.save(outfile,self.acc_roll)

		with file('roll_force.npy','w') as outfile:
			npy.save(outfile,self.force_roll)

		with file('force_weights.npy','w') as outfile:
			npy.save(outfile,self.weights)		

		with file('target_force.npy','w') as outfile:
			npy.save(outfile,self.target_forces)		

	def load_weights(self, weight):
		self.weights = copy.deepcopy(weight)	

def main(args):    

	pos = npy.load(str(sys.argv[1]))[:,:3]
	vel = npy.load(str(sys.argv[2]))[:,:3]
	acc = npy.load(str(sys.argv[3]))[:,:3]

	dmp = DMP(len(pos))

	dmp.load_trajectory(pos,vel,acc)		
	dmp.initialize_variables()
	dmp.learn_DMP()
		
	start = npy.zeros(dmp.dimensions)	
	goal = npy.ones(dmp.dimensions)
	norm_vector = pos[-1]-pos[0]
	init_vel = npy.divide(vel[0],norm_vector)	
	
	dmp.rollout(start, goal, init_vel)
	dmp.save_rollout()

if __name__ == '__main__':
    main(sys.argv)
