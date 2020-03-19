#! /usr/bin/env python3

import os
import requests
import json
import re

directory = 'supplier-data/descriptions/'
url = "http://35.222.28.72/fruits/"
files =  os.listdir(directory)
# print(files)

for file in files:
    try:
        filename, ext = os.path.splitext(file)
        with open(directory+file, 'r') as f:
            lines = f.readlines()
            # print(lines)
            product = {}
            product['name'] = lines[0].rstrip()
            regex = r"(\d*) lbs"
            weight_text = lines[1].rstrip()
            weight = re.match(regex, weight_text)
            product['weight'] = weight.group(1)
            product['description'] = lines[2].rstrip()
            product['image_name'] = filename + '.jpeg'
            #print(feedback)
            data = json.dumps(product)
            response = requests.post(url, data=data, headers={'Content-type': 'application/json;charset=utf-8'})
            print(response.status_code)
            #print(dump)
    except IOError as err:
        print(err.errno)
        print(err)
        pass