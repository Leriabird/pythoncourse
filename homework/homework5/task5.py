__author__ = 'Leria'

import re
import sys

data = sys.stdin.read()

def telegram(text):
    # pattern = "\W"
    # res = re.sub(pattern, ' ', text)
    # res_norm = re.sub('\s{2}', ' ', res)
    pattern = "[^a-zA-Z0-9]+"
    res = re.sub(pattern, ' ', data)
    return res

print(telegram(data))