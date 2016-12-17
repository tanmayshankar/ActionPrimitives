#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as npy
import sys

num_points = 100
points = npy.zeros((num_points,2))
counter = 0

fig,ax = plt.subplots()
ax.plot(range(50))

def onclick(event): 
	global counter, points
	print(counter)
	points[counter,0] = event.xdata
	points[counter,1] = event.ydata		
	counter+=1
	if (counter==99):
		plt.close()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

with file("points_{0}.npy".format(sys.argv[1]),'w') as outfile:
	npy.save(outfile,points)