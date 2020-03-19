#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails
import os

title_prefix = "Error - "
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

if psutil.cpu_percent(60) > 80:
    title =  title_prefix + "[CPU usage is over 80%]"
    message = emails.generate_email(sender, receiver, title, body, None)
    emails.send_email(message)

du = shutil.disk_usage("/")
free_space = du.free / du.total * 100

if free_space < 20:
    title =  title_prefix + "[available disk space is lower than 20%]"
    message = emails.generate_email(sender, receiver, title, body, None)
    emails.send_email(message)

ru = psutil.virtual_memory()
free_ram = ru.free / 1024 / 1024

if free_ram < 500:
    title =  title_prefix +  "[available memory is less than 500MB]"
    message = emails.generate_email(sender, receiver, title, body, None)
    emails.send_email(message)

localhost = socket.gethostbyname('localhost')
if not localhost == "127.0.0.1":
    title =  title_prefix +  "[localhost cannot be resolved to 127.0.0.1]"
    message = emails.generate_email(sender, receiver, title, body, None)
    emails.send_email(message)

