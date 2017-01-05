#!/usr/bin/env python
from headers import *
from Learn_DMP import *

class primitive_library():

	def __init__(self):

		self.number_segments = 19
		self.segment_length = 100
		self.overlap = 50

		self.trajectory_length = 100
		self.dim = 2
		# self.trajectory = npy.zeros((self.trajectory_length,self.dim))
		self.pos = npy.load(str(sys.argv[1]))
		self.vel = npy.load(str(sys.argv[2]))
		self.acc = npy.load(str(sys.argv[3]))

		self.segments = npy.zeros((self.number_segments, self.segment_length, self.dim))		
		self.primitives = [DMP() for i in range(self.number_segments)]

	# def load_trajectory(self):
	# 	# self.trajectory = npy.loadtxt(str(sys.argv[1]))
	# 	self.trajectory = npy.load(str(sys.argv[1]))

	def segment_trajectory(self):
		for i in range(0,self.number_segments):

			print(i)
			# self.segments[i,:,:] = self.trajectory[i*self.segment_length:(i+1)*self.segment_length,:]
			self.segments[i] = self.trajectory[i*(self.segment_length-self.overlap):(i+1)*self.segment_length-i*self.overlap]			

	def initialize_DMPs(self):
		for i in range(0,self.number_segments):
			# self.primitives[i].load_pos(self.segments[i])
			ind1 = i*(self.segment_length-self.overlap)
			ind2 = (i+1)*self.segment_length-i*self.overlap	

			self.primitives[i].load_trajectory(self.pos[ind1:ind2],self.vel[ind1:ind2],self.acc[ind1:ind2])
			self.primitives[i].initialize_variables()
			
	def learn_DMPs(self):
		for i in range(0,self.number_segments):
			self.primitives[i].learn_DMP()

	def save_DMPs(self):
		for i in range(0,self.number_segments):
			self.primitives[i].save_DMP_parameters(i)

def main(args):    

	library = primitive_library()
	# library.load_trajectory()
	# library.segment_trajectory()
	library.initialize_DMPs()
	library.learn_DMPs()
	library.save_DMPs()

if __name__ == '__main__':
    main(sys.argv)

