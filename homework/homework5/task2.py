__author__ = 'Leria'

import re
import sys

data = sys.stdin.read()

def klezmatics(numbers):
    num_lst = numbers.strip().split('\n')
    switch = False
    for line in num_lst:
        switch = False
        for char in line:
           if len(re.findall(char+"{3,11}", line)) > 0:
                switch = True
        if switch:
            print(line)

print(klezmatics(data))