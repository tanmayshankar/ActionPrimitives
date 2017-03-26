#!/usr/bin/env python
from headers import *
from scipy.ndimage.filters import gaussian_filter1d

def main(argv):

	FILE_DIR = "/home/tanmay/Research/Code/ActionPrimitives/Data/Cornell_Data/Primitive_Library/Subject1/Resolved_Trajectories/"
	lhsmooth = npy.load(os.path.join(FILE_DIR,"LH_Presmooth.npy"))
	rhsmooth = npy.load(os.path.join(FILE_DIR,"RH_Presmooth.npy"))

	for i in range(31):
		print(i)
		lhsmooth[i] = gaussian_filter1d(lhsmooth[i],3.5,axis=0,mode='nearest')
		rhsmooth[i] = gaussian_filter1d(rhsmooth[i],3.5,axis=0,mode='nearest')

	npy.save("LH_Smooth.npy",lhsmooth)
	npy.save("RH_Smooth.npy",rhsmooth)

if __name__ =='__main__':
	main(sys.argv)