__author__ = 'Leria'

import re
from collections import Counter

with open('hp5.txt', 'r') as hp:
    text = hp.read()
    pattern1 = ("(whisper\w+) ([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+)")
    pattern2 = ("([A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+) (whisper\w+)")
    tup1 = re.findall(pattern1, text)
    tup2 = re.findall(pattern2, text)
    print(tup1)
    print(tup2)
    lst1 = [char[1] for char in tup1]
    lst2 = [char[0] for char in tup2]
    lst = lst1 + lst2
    counts = Counter(lst)
    mc = counts.most_common(1)
    print(mc[0][1], mc[0][0])