#! /usr/bin/env python3

#from fractions import gcd

def euclid(a, b):
    while b:
        a, b = b, a % b
    return a
# а вот тут я не поняла, почему не работает модуль из стандартной библиотеки 
# (хотела быть хитрецом):
# def euclid(n, m):
#     x = gcd(20, 8)
#     return x

lst = input().split()
n = int(lst[0])
m = int(lst[1])
print(euclid(n, m))