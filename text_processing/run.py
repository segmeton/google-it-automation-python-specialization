#! /usr/bin/env python3

import os
import requests
import ipaddress
import json

directory = 'data/feedback/'
files =  os.listdir(directory)
# print(files)

feedbacks = []
for file in files:
    try:
        with open(directory+file, 'r') as f:
            lines = f.readlines()
            # print(lines)
            # for line in lines:
            #     print(line.rstrip()) 
            feedback = {}
            feedback['title'] = lines[0].rstrip()
            feedback['name'] = lines[1].rstrip()
            feedback['date'] = lines[2].rstrip()
            feedback['feedback'] = lines[3].rstrip()
            #print(feedback)
            dump = json.dumps(feedback)
            print(dump)
            feedbacks.append(feedback)    
    except IOError as e:
        print(e.errno)
        print(e)
        pass

# print(feedbacks)

data = json.dumps(feedbacks)
# print(data)

ip = ipaddress.ip_address('192.168.0.1')
url = 'https://www.mocky.io/v2/5185415ba171ea3a00704eed'
# print(ip)

# response = requests.post(url, data=data)
# print(response.status_code)
# print(response.request.body)