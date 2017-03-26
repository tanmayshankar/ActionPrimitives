#!/usr/bin/env python
import numpy as npy
import matplotlib.pyplot as plt
import sys
import random
from scipy import signal
import copy
import os
from sklearn.cluster import KMeans
import shutil
import subprocess
import glob
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d
from scipy.ndimage.filters import gaussian_filter1d
from DMP_Segment import *
# import scipy.interpolate.interp1d as interp