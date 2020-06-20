#!/usr/bin/env python3
import requests
import os
from pathlib import Path

student = "student-00-8915069d6cb8"
src = r"/home/{}/supplier-data/images".format(student)

def uploadFile(file):
    """upload the file"""
    url = "http://localhost/upload/"
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})

for file in os.listdir(src):
    """if file is a jpeg, upload it"""
    # get filetype
    f, e = os.path.splitext(os.path.basename(file))
    if e == ".jpeg":
        try:
            print("uploading {}".format(file))
            uploadFile(src + "/" + file)
        except:
            print("{} failed to upload".format(file))