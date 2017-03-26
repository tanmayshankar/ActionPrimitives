#!/usr/bin/env python
import numpy as npy
import cv2
import scipy.interpolate as scin
import pdb
import os
import sys

def interpolate_depth(FILE_DIR,num_frames):

	for i in range(0,num_frames):
		print("Interpolating Frame", i)
		dimage = cv2.imread(os.path.join(FILE_DIR,"Depth_{0}.png".format(i)),-1)

		mask = dimage>0
		xx,yy = npy.meshgrid(npy.arange(dimage.shape[1]),npy.arange(dimage.shape[0]))
		xym = npy.vstack((npy.ravel(xx[mask]),npy.ravel(yy[mask]))).T

		data_var = npy.ravel(dimage[:,:][mask])
		interp = scin.NearestNDInterpolator(xym,data_var)
		result = interp(npy.ravel(xx),npy.ravel(yy)).reshape(xx.shape)

		cv2.imwrite(os.path.join(FILE_DIR,"Interpolated_Depth_{0}.png".format(i)),result)

def main(argv):

	# FILE_DIR = "/home/tanmay/catkin_ws/src/Visualize_Primitives/Data/K2_Demos/Desk_Demo_7/"
	#FILE_DIR = "/home/tanmay/Code/K2_Demo/Desk_Demo_7/"
	FILE_DIR = str(sys.argv[1])
	num_frames = int(sys.argv[2])

	interpolate_depth(FILE_DIR,num_frames)

if __name__ == '__main__':
	main(sys.argv)	

