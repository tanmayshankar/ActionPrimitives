#!/usr/bin/env python
from headers import *
import cv2

lhns = npy.load("LH_Number_Force_Segments.npy")
rhns = npy.load("RH_Number_Force_Segments.npy")

lh_seg_inds = npy.load("LH_Seg_Inds.npy")
rh_seg_inds = npy.load("RH_Seg_Inds.npy")

image_paths = npy.load("IMAGE_PATHS.npy")
num_files = 4
seg = 0
window = 10

for i in range(num_files-1,num_files):
	for k in range(len(lh_seg_inds[i])-1):
		for t in range(lh_seg_inds[i][k],lh_seg_inds[i][k+1]):
			
			margin = 0
			print(i,t)

			imgpath = image_paths[i]+'/'+"RGB_{0}.png".format(t+1)		
			img = cv2.imread(imgpath)		
			label = img.copy()		

			# cv2.rectangle(label,(0,400),(640,480),(0,0,255),-1)
			cv2.rectangle(label,(0,400),(640,480),(255*(k%2),0,255*((k+1)%2)),-1)				
			cv2.putText(label,"Time: {0} Segment: {1} Next: {2}".format(t,k,lh_seg_inds[i][k+1]),(90,450),cv2.FONT_ITALIC,0.9,(255,255,255),3)

			cv2.addWeighted(label,0.5,img,0.5,0,img)		
			cv2.imshow("Right Hand Frame",img)
			cv2.moveWindow("Right Hand Frame",900,500)
			
			if (abs(lh_seg_inds[i][k]-t)<window)or(abs(lh_seg_inds[i][k+1]-t)<window):				
				margin = 0
			cv2.waitKey(40+margin)
	
	cv2.destroyAllWindows()

