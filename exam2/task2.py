__author__ = 'Leria'

import re
import urllib
import requests

with open('links.txt', 'r') as l:
    lin = l.read()
    lst = lin.split('\n')
    mailset = []
    for char in lst:
        text = requests.get(char).text
        r = "[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
        temp = re.findall(r, text)
        tempout = list(set(temp))
        mailset.extend(tempout)
    for char in mailset:
        print(char)