__author__ = 'Leria'

import re
import sys

def uncle_Sam(data):
    wants = len(re.findall('(y|Y)ou', data))
    return wants

data = sys.stdin.read()
print(uncle_Sam(data))