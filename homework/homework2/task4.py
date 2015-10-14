#! /usr/bin/env python3

def euclid(a, b):
    return euclid(b, a % b) if b else a


def rpfilter(a, *args):
    rp = list(filter(lambda arg: euclid(a, arg) == 1, args))
    return rp

firstarg, *otherargs = map(int, input().split())
if rpfilter(firstarg, *otherargs) != []:
    for char in (rpfilter(firstarg, *otherargs)):
        print(char, end=' ')
else:
    (print(None))