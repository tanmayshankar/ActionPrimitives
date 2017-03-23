	#!/usr/bin/env python
from headers import *
import cv2

# FILE_DIR = "/home/tanmay/catkin_ws/src/Visualize_Primitives/Data/K2_Demos/Desk_Demo_13/"
FILE_DIR = "/home/tanmay/catkin_ws/src/Visualize_Primitives/Data/K2_Demos/Grid_Demo/D{0}"

# lh_seg_inds = npy.load(os.path.join(FILE_DIR,"RH_Seg.npy"))
# rh_seg_inds = npy.load(os.path.join(FILE_DIR,"RH_Seg.npy"))

video_index = 3
rh_seg_inds = npy.load(os.path.join(FILE_DIR.format(video_index),"D{0}_RH_NFSeg.npy".format(video_index)))
# rh_seg_inds = npy.array([  0,   1,  35,  74, 124, 158, 197, 264, 301, 335, 342])
seg = 0
window = 10

for k in range(len(rh_seg_inds)-1):
	for t in range(rh_seg_inds[k],rh_seg_inds[k+1]):
		
		margin = 0
		print(t)

		imgpath = os.path.join(FILE_DIR.format(video_index),"RGB_{0}.png".format(t+1))
		img = cv2.imread(imgpath)		
		label = img.copy()		

		cv2.rectangle(label,(0,900),(1920,1080),(255*(k%2),0,255*((k+1)%2)),-1)				
		cv2.putText(label,"Time: {0} Segment: {1} Next: {2}".format(t,k,rh_seg_inds[k+1]),(500,1000),cv2.FONT_ITALIC,2,(255,255,255),3)

		cv2.addWeighted(label,0.5,img,0.5,0,img)		
		cv2.imshow("Right Hand Frame",img)
		
		if (abs(rh_seg_inds[k]-t)<window)or(abs(rh_seg_inds[k+1]-t)<window):				
			margin = 0
		cv2.waitKey(50+margin)

cv2.destroyAllWindows()

