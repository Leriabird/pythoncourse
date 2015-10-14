#! /usr/bin/env python3

def plural(n, lst):
    deflst = [2, 3, 4]
    exclst = [12, 13, 14]
    if (n % 10 == 1) and (n % 100 != 11):
        return lst[0]
    if (n % 10 in deflst) and (n % 100 not in exclst):
        return lst[1]
    else:
        return lst[2]

word = input()
amount = int(input())
if word == 'утюг':
    data = ['утюг', 'утюга', 'утюгов']
elif word == 'чайник':
    data = ['чайник', 'чайника', 'чайников']
elif word == 'ложка':
    data = ['ложка', 'ложки', 'ложек']
elif word == 'гармошка':
    data = ['гармошка', 'гармошки', 'гармошек']
print(amount, plural(amount, data))