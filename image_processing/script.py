#!/usr/bin/env python3

import os
import sys
from PIL import Image

print("Hello")
ori_dir = "ori/"
arr = os.listdir(ori_dir)
print(arr)

for infile in arr:
    try:
        with Image.open(ori_dir+infile) as im:
            print(infile, im.format, "%dx%d" % im.size, im.mode)
            f, e = os.path.splitext(infile)
            print(f)
            directory = 'output/'
            outfile = directory + f + '.jpg'
            print(outfile)
            out = im.resize((128, 128)).rotate(90) # degrees counter-clockwise
            if not os.path.exists(directory):
                os.makedirs(directory)
            out.convert('RGB').save(outfile)
    except IOError as e:
        print(e.errno)
        print(e)
        pass
