#! /usr/bin/env python3

def prime(x):
    counter = True
    for i in range(2, 5000):
        if x == 2:
            break
        elif (x % i == 0) and x != i:
            counter = False
        i += 1
    return counter

n = int(input())
numlst = [int(input()) for char in range(n)]
boolst = [prime(char) for char in numlst]
for i in boolst:
    print(i)
