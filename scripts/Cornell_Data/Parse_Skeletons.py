#!/usr/bin/env python
from headers import *

file_list = glob.glob("Subject1_annotations/*/*[0-9][0-9].txt")

for i in range(len(file_list)):
	# npy.genfromtxt("file.txt",delimiter=',',dtype=float,skip_footer=1)
	skeleton = npy.genfromtxt(file_list[i],delimiter=',',dtype=float,skip_footer=1)

	right_hand = skeleton[:,159:163] #Till 162, saving confidence values.
	left_hand = skeleton[:,155:159]	#Till 158, saving confidence values.

	with file("Original_Right_Hand_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,right_hand)

	with file("Original_Left_Hand_{0}.npy".format(i),'w') as outfile:
		npy.save(outfile,left_hand)

with file("File_List.npy",'w') as outfile:
	npy.save(outfile,npy.array(file_list))

	