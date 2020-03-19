#!/usr/bin/env python3

import emails
import reports
import re
import os
import sys
import datetime
from datetime import date

def load_data(directory):
    files =  os.listdir(directory)
    # print(files)
    
    data = []

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
                data.append(product)
        except IOError as err:
            print(err.errno)
            print(err)
            pass

    return data

def process_data(data):
    paragraph = ""

    for item in data:
        line = "name: {}<br/>weight: {} lbs<br/><br/>".format(item["name"], item["weight"])
        paragraph += line

    return paragraph

def main(argv):
    directory = "supplier-data/descriptions/"
    data = load_data(directory)

    pdf_file = "reports/processed.pdf"
    if not os.path.exists("reports/"):
        os.makedirs("reports/")
    today = date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)
    body = process_data(data)
    reports.generate_report(pdf_file, title, body)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, pdf_file)
    # emails.send_mail(message)

if __name__ == "__main__":
    main(sys.argv)