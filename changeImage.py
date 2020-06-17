#!/usr/bin/env python3
from PIL import Image
import os
from pathlib import Path

src = r"/home/student-00-ab307bfaf59a/supplier-data/images"
dest = src

def fixImage(file):
    # open image
    with Image.open(file) as img:

        # resize to 600x400
        out = img.resize((600, 400))

        # save as jpg in new dest
        f, e = os.path.splitext(os.path.basename(file))
    outfile = dest + "/" + f
    out.save(outfile, "JPEG")

for file in os.listdir(src):
     try:
         print("fixing {}".format(file))
         fixImage(src+"/"+file)
     except:
         print("{} not image".format(file))
