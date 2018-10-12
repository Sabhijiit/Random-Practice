# -*- coding: utf-8 -*-
"""
@author: Sabhijiit
"""
import cv2
import numpy as np
from PIL import Image

img_list = ["19120.jpg"]


# Function to resize input image to size (299, 299)
def manipulation_func(i):
    img = cv2.imread(i)
    width = np.size(img, 1)
    height = img.size[1]
    half_width = width/2
    half_height = height/2
    img_crop = img.crop((0,
                 half_height - half_width,
                 width,
                 half_height + half_width))
    w_crop = img_crop.size[0]
    h_crop = img_crop.size[1]
    basewidth = 299
    resize_ratio = float(basewidth)/w_crop
    hsize = int((float(h_crop) * float(resize_ratio)))
    if hsize < 299:
        hsize = 299
    resized_img = img_crop.resize((basewidth, hsize), Image.ANTIALIAS)
    w_r = resized_img.size[0]
    h_r = resized_img.size[1]
    print "width of image ", i, "is: ", w_r, "and height is: ", h_r
    resized_img.show()
    
for i in img_list:
    manipulation_func(i)
