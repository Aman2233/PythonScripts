# coding=utf-8


import sys
import requests # This package will allow the programme to accept web requests

sub_list = open("wordlist.txt").read() #reading a list of words from wordlist.txt
directories = sub_list.splitlines() #splitting line to diffrinciate each directory

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" # requests for sub domains .html domains e.g http://tryhackme/file.html http://tryhackme/index.html
    r = requests.get(dir_enum)
    if r.status_code==404: #no webpage 
        pass
    else:
        print ("Valid directory:" ,dir_enum)

