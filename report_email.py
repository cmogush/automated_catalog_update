#!/usr/bin/env python3

import json
import locale
import sys
import emails
import reports
import os
from datetime import datetime

student = "student-00-8915069d6cb8"
dir = r"/home/{}/supplier-data/descriptions".format(student)

def process_descriptions(dir):
    """iterate over descriptions dir and generate summary from text files"""
    summary = ""
    for file in os.listdir(dir):  # iterate over the dir
        f, e = os.path.splitext(file)  # find out the file extension
        if e == ".txt":  # if it's a text file
            with open(os.path.join(dir, file), 'r') as f:
                summary += "<br/>"
                summary += "name: {}<br/>".format(f.readline())
                summary += "weight: {}<br/>".format(f.readline())
    return summary

def main(argv):
  """Process the descriptions and generate a full report out of it."""
  summary = process_descriptions(dir)
  today = str(datetime.date(datetime.now()))
  reports.generate("/tmp/processed.pdf", "Processed Update on "+today, summary)

  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")  # creates email
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)