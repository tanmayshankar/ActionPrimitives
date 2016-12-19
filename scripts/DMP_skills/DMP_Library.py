#!/usr/bin/env python
from headers import *
from DMP_Invariant import *

class primitive_library():

	def __init__(self):

		self.number_segments = 9
		self.segment_length = 20
		self.overlap = 10

		self.trajectory_length = 100
		self.dim = 2
		self.trajectory = npy.zeros((self.trajectory_length,self.dim))

		self.segments = npy.zeros((self.number_segments, self.segment_length, self.dim))		
		self.primitives = [DMP() for i in range(self.number_segments)]

	def load_trajectory(self):
		# self.trajectory = npy.loadtxt(str(sys.argv[1]))
		self.trajectory = npy.load(str(sys.argv[1]))

	def segment_trajectory(self):
		for i in range(0,self.number_segments):

			print(i)
			# self.segments[i,:,:] = self.trajectory[i*self.segment_length:(i+1)*self.segment_length,:]
			self.segments[i] = self.trajectory[i*(self.segment_length-self.overlap):(i+1)*self.segment_length-i*self.overlap]

	def initialize_DMPs(self):
		for i in range(0,self.number_segments):
			self.primitives[i].load_pos(self.segments[i])
			self.primitives[i].initialize_variables()

	def learn_DMPs(self):
		for i in range(0,self.number_segments):
			self.primitives[i].learn_DMP()

	def save_DMPs(self):
		for i in range(0,self.number_segments):
			self.primitives[i].save_DMP_parameters(i)

def main(args):    

	library = primitive_library()
	library.load_trajectory()
	library.segment_trajectory()
	library.initialize_DMPs()
	library.learn_DMPs()
	library.save_DMPs()

if __name__ == '__main__':
    main(sys.argv)

