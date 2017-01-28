#!/usr/bin/env python
from headers import *

# file_list = glob.glob("Subject1_annotations/*/*[0-9][0-9].txt")
file_list = npy.load("Primitive_Library/Subject_1/File_List.npy")

for i in range(len(file_list)):
	# npy.genfromtxt("file.txt",delimiter=',',dtype=float,skip_footer=1)
	
	print(i)
	skeleton = npy.genfromtxt(file_list[i],delimiter=',',dtype=float,skip_footer=1)

	right_hand = skeleton[:,159:163] #Till 162, saving confidence values.
	left_hand = skeleton[:,155:159]	#Till 158, saving confidence values.

	right_shoulder = skeleton[:,81:85] #Till 84
	left_shoulder = skeleton[:,53:57] #Till 56

	# with file("Original_Right_Hand_{0}.npy".format(i),'w') as outfile:
	# 	npy.save(outfile,right_hand)

	# with file("Original_Left_Hand_{0}.npy".format(i),'w') as outfile:
	# 	npy.save(outfile,left_hand)
	
	with file("Original_Right_Shoulder_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_shoulder)

	with file("Original_Left_Shoulder_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_shoulder)		

# with file("File_List.npy",'w') as outfile:
# 	npy.save(outfile,npy.array(file_list))



for i in range(25,31):
	print(i)
	
	left_hand = npy.load("Traj_{0}/Original_Left_Hand_{0}.npy".format(i))
	left_shoulder = npy.load("Traj_{0}/Original_Left_Shoulder_{0}.npy".format(i))
	left_compensated = left_hand - left_shoulder
	
	with file("Left_Hand_Compensated_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_compensated)
	
	shutil.move("Left_Hand_Compensated_{0}.npy".format(i),"Traj_{0}/".format(i))	

	right_hand = npy.load("Traj_{0}/Original_Right_Hand_{0}.npy".format(i))
	right_shoulder = npy.load("Traj_{0}/Original_Right_Shoulder_{0}.npy".format(i))
	right_compensated = right_hand - right_shoulder
	
	with file("Right_Hand_Compensated_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_compensated)
	
	shutil.move("Right_Hand_Compensated_{0}.npy".format(i),"Traj_{0}/".format(i))