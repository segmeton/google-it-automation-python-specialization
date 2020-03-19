#!/usr/bin/env python3

import os
import sys
from PIL import Image

ori_dir = "supplier-data/images/"
directory = 'supplier-data/images/'
files = os.listdir(ori_dir)
#print(files)

if not os.path.exists(directory):
    os.makedirs(directory)

for file in files:
    filename, ext = os.path.splitext(file)
    outfile = filename + ".jpeg"
    if file != outfile:
        try:
            with Image.open(ori_dir+file) as img:
                print(file, img.format, "%dx%d" % img.size, img.mode)
                new_images = directory + outfile
                #print(new_images)
                img.resize((600, 400)).convert('RGB').save(new_images)
        except IOError as err:
            print(err.errno)
            print(err)
            pass
