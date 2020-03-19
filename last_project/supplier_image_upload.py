#!/usr/bin/env python3

import requests
import os

ori_dir = "supplier-data/images/"
images = os.listdir(ori_dir)
print(images)

url = "http://104.155.153.214/upload/"
for image in images:
    filename, ext = os.path.splitext(image)
    outfile = filename + ".jpeg"
    if image == outfile:
        try:
            with open(ori_dir+image, 'rb') as img:
                request = requests.post(url, files={'file':img})
        except IOError as err:
            print(err.errno)
            print(err)
            pass
