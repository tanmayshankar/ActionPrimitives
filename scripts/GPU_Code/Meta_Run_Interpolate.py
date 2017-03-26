#!/usr/bin/env python
import os
import subprocess
import sys
import shutil
import time
import signal
import numpy as npy

FRCNN_DIR = "/home/tanmay/Code/py-faster-rcnn/tools"
CPM_DIR = "/home/tanmay/Code/Realtime_Multi-Person_Pose_Estimation/testing/python"
INTERP_DIR = "/home/tanmay/Code/Meta_Scripts"
IMG_DIR = "/home/tanmay/Code/Grid_Demo/Grid_Demo/"
number_images = npy.load(os.path.join(IMG_DIR,"Number_Images.npy"))


# # COMMANDS: 
# # RUN FRCNN
# command = ['python {0}/save_detections_gpu_args.py --data {1}D{2}/ --numf {3}']
# # .format with (FRCNN_DIR,IMG_DIR,d_index, number_images[d_index-1], INTERP_DIR)

# # RUN CPM
# # MUST BE RUN IN TESTING/PYTHON of CPM FOLDER
# command = ['python Video_CPM_args.py {1}D{2}/ {3}']
# # .format with (FRCNN_DIR, IMG_DIR,d_index,number_images[d_index-1], INTERP_DIR)

# # RUN INTERPOLATE DEPTH
# command = ['python {4}/Interpolate_Depth_Args.py {1}D{2} {3}']
# # .format with (FRCNN_DIR, IMG_DIR, d_index, number_images[d_index-1], INTERP_DIR)

# RUN FRCNN
command = 'python {4}/Interpolate_Depth_Args.py {1}D{2} {3}'

for d in range(1,11):

	print("STARTING TO PROCESS VIDEO",d)
	
	p = subprocess.Popen(command.format(FRCNN_DIR, IMG_DIR, d, number_images[d-1], INTERP_DIR),shell=True)

	p.wait()
	time.sleep(2)
