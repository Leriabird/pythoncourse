__author__ = 'Leria'

import re
import sys

data = sys.stdin.read()

def harder(code):
    pattern = "[^a-zA-Z0-9.,]" + " = "
    listed = code.split('\n')
    list = [elt.lstrip() for elt in listed]
    for index, line in enumerate(list):
        if not line.startswith('#'):
            treasures = re.findall("(\s*[\w_., ]+) = ", line)
            if len(treasures) > 0:
                print(index + 1, ''.join(treasures[0].split(',')))

harder(data)