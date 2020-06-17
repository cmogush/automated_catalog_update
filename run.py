#! /usr/bin/env python3
import os
import requests

dir = r"/home/student-00-ab307bfaf59a/supplier-data/descriptions"
post_url = "http://34.68.200.112/fruits/"

def processFiles(dir, post_url):
    """iterate over all text files in directory"""
    for file in os.listdir(dir):  # iterate over the dir
        f, e = os.path.splitext(file)  # find out the file extension
        if e == ".txt":  # if it's a text file
            dict = convertToDict(file)  # convert the file to the dict
            response = requests.post(post_url, json=dict)  # make a POST request
            if response.status_code == 201:
                print("Successfully posted {}".format(file))
            else:
                print("Failed {}".format(response.status_code))

def convertToDict(file):
    """convert text file to a dictionary"""
    dict = {}
    with open(dir+"/"+file, 'r') as f:
        dict['name'] = f.readline()
        weight, lbs = f.readline().split(" ")
        dict['weight'] = int(weight)
        dict['description'] = f.readline()
        f, e = os.path.splitext(file)
        image = f + ".jpeg"
        dict['image_name'] = image
    return dict

processFiles(dir, post_url)