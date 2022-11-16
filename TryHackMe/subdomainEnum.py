# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import requests # This package will allow the programme to accept web requests

sub_list = open("subdomains.txt").read() #reading a list of subdomains
subdoms = sub_list.splitlines() #splitting line to diffrinciate each domain

for sub in subdoms: #for loop for the subdomains in subdoms
    sub_domains = f"http://{sub}.{sys.argv[1]}" # this allows an entry e.g http://web.tryhackme.com, http://skype.tryhackme.com

    try: #try requests line by line
        requests.get(sub_domains)
    except requests.ConnectionError: #if connection error pass onto the next sub
        pass
    else:
        print("Valid domain: ", sub_domains)