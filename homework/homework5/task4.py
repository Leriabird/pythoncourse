__author__ = 'Leria'

import re
import sys
data = 'a, b, c = 12, 13, 15\nfor x in [1, 2, 3, 4]:\n    a, b = x, x + 1\n    # yo = x\n    # to, to = 6, 5\n    c, d = x + 2, x + 3  # thats ok'
def harder(code):
    pattern = "[^a-zA-Z0-9.,]" + " = "
    listed = code.split('\n')
    list = [elt.lstrip() for elt in listed]
    for index, line in enumerate(list):
        if not line.startswith('#'):
            treasures = re.findall("(\s*[\w_., ]+) = ", line)
            if len(treasures) > 0:
                print(index + 1, ''.join(treasures[0].split(',')))

print(harder(data))