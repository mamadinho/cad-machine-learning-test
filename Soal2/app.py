# importing required modules
import PyPDF2
import re
import pandas as pd
import sys

import argparse
 
parser = argparse.ArgumentParser(description="A simple app to extract text from PDF table",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("filename")
args = parser.parse_args()
config = vars(args)

file_name = config['filename']
  
# creating a pdf file object
pdfFileObj = open(file_name, 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
# creating a page object
pageObj = pdfReader.pages

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 20000:
        parts.append(text)
  
df = []
# extracting text from page
for i in range(20):
    parts = []
    description = pageObj[i].extract_text().split("Description")[1].split("Possible Root")[0].split('Troubleshooting')[0].strip()
    cause = pageObj[i].extract_text().split("Description")[1].split("Possible Root")[1].split('Troubleshooting')[0].replace('cause', '').strip()
    pageObj[i].extract_text(visitor_text=visitor_body)
    page = parts[1]
    lst = [description, cause, page]
    df.append(lst)
  
# closing the pdf file object
pdfFileObj.close()

# export to csv
df = pd.DataFrame(df)
df.columns = ['Description', 'Possible Root Cause', 'Page Number']
df.to_csv('output.csv', index=False)
