#! /usr/bin/env python3

def combinations(n, k):
    if 0 <= k <= n:
        ncomb = 1
        kcomb = 1
        for i in range(1, min(k, n - k) + 1):
            ncomb *= n
            kcomb *= t
            n -= 1
        return ncomb // kcomb
    else:
        return 0

lst = input().split()
n = int(lst[0])
k = int(lst[1])
print(combinations(n, k))
