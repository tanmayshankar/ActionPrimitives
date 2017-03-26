#!/usr/bin/env python
import cv2 as cv 
import numpy as np
import scipy
import PIL.Image
import math
import time
from config_reader import config_reader
import util
import copy
import matplotlib
import pylab as plt
import sys
import os

FILE_DIR = "/home/tanmay/Code/py-faster-rcnn/tools"
sys.path.insert(0, FILE_DIR)

from _init_paths import *
import caffe

def main(argv):

	# IMG_DIR = "/home/tanmay/Code/K2_Demo/Desk_Demo_9/"
	IMG_DIR = str(sys.argv[1])
	num_images = int(sys.argv[2])

	param, model = config_reader()

	if param['use_gpu']:
		caffe.set_mode_gpu()
		caffe.set_device(param['GPUdeviceNumber']) # set to your device!
	else:
		caffe.set_mode_cpu()
	net = caffe.Net(model['deployFile'], model['caffemodel'], caffe.TEST)
	
	coordinates = np.zeros((num_images,4,2))

	for i in range(num_images):

		oriImg = cv.imread(os.path.join(IMG_DIR,"RGB_{0}.png".format(i)))	
		print(os.path.join(IMG_DIR,"RGB_{0}.png".format(i)))
	        multiplier = [x * model['boxsize'] / oriImg.shape[0] for x in param['scale_search']]

		print("PROCESSING IMAGE",i)

		for m in range(len(multiplier)):

			scale = multiplier[m]
			heatmap_avg = np.zeros((oriImg.shape[0], oriImg.shape[1], 19))

			imageToTest = cv.resize(oriImg, (0,0), fx=scale, fy=scale, interpolation=cv.INTER_CUBIC)
			imageToTest_padded, pad = util.padRightDownCorner(imageToTest, model['stride'], model['padValue'])
			# print imageToTest_padded.shape

			net.blobs['data'].reshape(*(1, 3, imageToTest_padded.shape[0], imageToTest_padded.shape[1]))
			#net.forward() # dry run
			net.blobs['data'].data[...] = np.transpose(np.float32(imageToTest_padded[:,:,:,np.newaxis]), (3,2,0,1))/256 - 0.5;
			start_time = time.time()
			output_blobs = net.forward()

			print('At scale %d, The CNN took %.2f ms.' % (m, 1000 * (time.time() - start_time)))

			# extract outputs, resize, and remove padding
			heatmap = np.transpose(np.squeeze(net.blobs[output_blobs.keys()[1]].data), (1,2,0)) # output 1 is heatmaps
			heatmap = cv.resize(heatmap, (0,0), fx=model['stride'], fy=model['stride'], interpolation=cv.INTER_CUBIC)
			heatmap = heatmap[:imageToTest_padded.shape[0]-pad[2], :imageToTest_padded.shape[1]-pad[3], :]
			heatmap = cv.resize(heatmap, (oriImg.shape[1], oriImg.shape[0]), interpolation=cv.INTER_CUBIC)
			  
			# print(np.unravel_index(heatmap[:,:,2].argmax(),heatmap[:,:,2].shape))  

			coordinates[i,0] = np.unravel_index(heatmap[:,:,7].argmax(),heatmap[:,:,7].shape)
			coordinates[i,1] = np.unravel_index(heatmap[:,:,5].argmax(),heatmap[:,:,5].shape)
			coordinates[i,2] = np.unravel_index(heatmap[:,:,4].argmax(),heatmap[:,:,4].shape)
			coordinates[i,3] = np.unravel_index(heatmap[:,:,2].argmax(),heatmap[:,:,2].shape)

	np.save(os.path.join(IMG_DIR,"HAND_COORDINATES.npy"),coordinates)

if __name__ == '__main__':
	main(sys.argv)