#!/usr/bin/env python
from headers import *
import cv2

rhns = npy.load("Interp_Segment_All/RH_Num_Seg.npy")
# rhns = npy.load("RH_Number_Force_Segments.npy")

rh_seg_inds = npy.load("Interp_Segment_All/RH_Seg_Ind.npy")
# rh_seg_inds = npy.load("RH_Seg_Inds.npy")

print(rh_seg_inds)
# lhns = npy.load("LH_Number_Force_Segments.npy")
# rhns = npy.load("RH_Number_Force_Segments.npy")

# lh_seg_inds = npy.load("LH_Seg_Inds.npy")
# rh_seg_inds = npy.load("RH_Seg_Inds.npy")


image_paths = npy.load("IMAGE_PATHS.npy")
# num_files = 10
num_files = 9
# num_files = 5
seg = 0
window = 10

for i in range(num_files-1,num_files):
	for k in range(len(rh_seg_inds[i])-1):
		for t in range(rh_seg_inds[i][k],rh_seg_inds[i][k+1]):
			
			margin = 0
			# print(i,t)

			imgpath = image_paths[i]+'/'+"RGB_{0}.png".format(t+1)		
			img = cv2.imread(imgpath)		
			label = img.copy()		

			# cv2.rectangle(label,(0,400),(640,480),(0,0,255),-1)
			cv2.rectangle(label,(0,400),(640,480),(255*(k%2),0,255*((k+1)%2)),-1)				
			cv2.putText(label,"Time: {0} Segment: {1} Next: {2}".format(t,k,rh_seg_inds[i][k+1]),(90,450),cv2.FONT_ITALIC,0.9,(255,255,255),3)

			cv2.addWeighted(label,0.5,img,0.5,0,img)		
			cv2.imshow("Left Hand Frame",img)
			cv2.moveWindow("Left Hand Frame",1100,900)
			# cv2.moveWindow("Left Hand Frame",900,500)			
			
			if (abs(rh_seg_inds[i][k]-t)<window)or(abs(rh_seg_inds[i][k+1]-t)<window):				
				margin = 0
			cv2.waitKey(40+margin)
	
	cv2.destroyAllWindows()

