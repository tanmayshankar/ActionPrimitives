#!/usr/bin/env python

# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""

import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, sys, cv2
import argparse
import numpy as npy

CLASSES = ('__background__',
 'person',
 'bicycle',
 'car',
 'motorcycle',
 'airplane',
 'bus',
 'train',
 'truck',
 'boat',
 'traffic light',
 'fire hydrant',
 'stop sign',
 'parking meter',
 'bench',
 'bird',
 'cat',
 'dog',
 'horse',
 'sheep',
 'cow',
 'elephant',
 'bear',
 'zebra',
 'giraffe',
 'backpack',
 'umbrella',
 'handbag',
 'tie',
 'suitcase',
 'frisbee',
 'skis',
 'snowboard',
 'sports ball',
 'kite',
 'baseball bat',
 'baseball glove',
 'skateboard',
 'surfboard',
 'tennis racket',
 'bottle',
 'wine glass',
 'cup',
 'fork',
 'knife',
 'spoon',
 'bowl',
 'banana',
 'apple',
 'sandwich',
 'orange',
 'broccoli',
 'carrot',
 'hot dog',
 'pizza',
 'donut',
 'cake',
 'chair',
 'couch',
 'potted plant',
 'bed',
 'dining table',
 'toilet',
 'tv',
 'laptop',
 'mouse',
 'remote',
 'keyboard',
 'cell phone',
 'microwave',
 'oven',
 'toaster',
 'sink',
 'refrigerator',
 'book',
 'clock',
 'vase',
 'scissors',
 'teddy bear',
 'hair drier',
 'toothbrush')

NETS = {'vgg16': ('VGG16',
                  'VGG16_faster_rcnn_final.caffemodel'),
        'zf': ('ZF',
                  'ZF_faster_rcnn_final.caffemodel'),
        'coco': ('VGG16',
                  'coco_vgg16_faster_rcnn_final.caffemodel')}

class detections():

    def __init__(self,image_path):

        self.image_path = image_path
        self.bbox = []
        self.score = []
        self.class_ind = []
        self.class_name = []

def document_detections(im_file, class_ind, class_name, dets, thresh=0.5):
    
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return

    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]      
        
        obj.bbox.append(bbox)
        obj.score.append(score)
        obj.class_ind.append(class_ind)
        obj.class_name.append(class_ind)

        
def demo(net, image_index, FILE_DIR):
    """Detect object classes in an image using pre-computed object proposals."""
  
    #im_file = os.path.join('/home/tanmay/Code/ActionPrimitives/Data/Cornell_Data/Subject1_rgbd_images',image_name)    
    # im_file = os.path.join('/home/tanmay/Code/K2_Demo/Desk_Demo_9/',image_name)
    FILE_DIR = str(FILE_DIR)
    im_file = os.path.join(FILE_DIR,"RGB_{0}.png".format(image_index))
    print(im_file)
    print("Reading Image")
    im = cv2.imread(im_file)
    print("Read Image")
    
    # Detect all object classes and regress object bounds
    timer = Timer()
    timer.tic()
    scores, boxes = im_detect(net, im)
    timer.toc()
    print ('Detection took {:.3f}s for '
           '{:d} object proposals').format(timer.total_time, boxes.shape[0])

    # Visualize detections for each class
    CONF_THRESH = 0.7
    NMS_THRESH = 0.3

    obj = detections(im_file)

    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
        cls_scores = scores[:, cls_ind]
        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
        keep = nms(dets, NMS_THRESH)
        dets = dets[keep, :]       

        inds = np.where(dets[:, -1] >= CONF_THRESH)[0]

        if (len(inds)):
            for i in inds:
                bbox = dets[i,:4]
                score = dets[i,-1]

                obj.bbox.append(bbox)
                obj.score.append(score)
                obj.class_ind.append(cls_ind)
                obj.class_name.append(cls)

    fname_split = os.path.splitext(im_file)[0]
    npy.save('{0}.npy'.format(fname_split),obj)


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Faster R-CNN demo')
    parser.add_argument('--gpu', dest='gpu_id', help='GPU device id to use [0]',
                        default=0, type=int)
    parser.add_argument('--cpu', dest='cpu_mode',
                        help='Use CPU mode (overrides --gpu)',
                        action='store_true')
    parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16]',
                        choices=NETS.keys(), default='coco')
    
    parser.add_argument('--data', dest='data_file', help='Directory Containing Images.',
                        default='/home/tanmay/Code/K2_Demo/Desk_Demo_13')    

    parser.add_argument('--numf',dest='num_frames',help='Number of Images.',
                        default=345, type=int)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    cfg.TEST.HAS_RPN = True  # Use RPN for proposals

    args = parse_args()

    prototxt = os.path.join(cfg.MODELS_DIR, NETS[args.demo_net][0],
                            'faster_rcnn_alt_opt', 'coco_test.pt')
    caffemodel = os.path.join(cfg.DATA_DIR, 'faster_rcnn_models',
                              NETS[args.demo_net][1])

    if not os.path.isfile(caffemodel):
        raise IOError(('{:s} not found.\nDid you run ./data/script/'
                       'fetch_faster_rcnn_models.sh?').format(caffemodel))

    if args.cpu_mode:
        caffe.set_mode_cpu()
    else:
        caffe.set_mode_gpu()
        caffe.set_device(args.gpu_id)
        cfg.GPU_ID = args.gpu_id        

    net = caffe.Net(prototxt, caffemodel, caffe.TEST)

    print '\n\nLoaded network {:s}'.format(caffemodel)

    print(args.data_file, args.num_frames)

    for i in range(args.num_frames):
        print("Running Image:",i)
        demo(net,i,args.data_file)
    
    # for ictr in range(len(image_list)):
    # #for ictr in range(1):
    #     im_name = image_list[ictr]     
    #     print("Running Image: ", ictr)

    #     demo(net, im_name)


