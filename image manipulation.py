# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 02:54:52 2017

@author: Sabs
"""

from PIL import Image

img = Image.open(r"images\19153.jpg")
width = img.size[0]
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

#print w_r, h_r
resized_img.show()