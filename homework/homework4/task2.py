__author__ = 'Leria'
from operator import mul
from functools import reduce

adj_amount = 0
noun_amount = 0
verb_amount = 0
adj_suffix = 'yo'
noun_suffix = 'ka'
with open('dict.txt', 'r') as vocab:
    vocab_list = [line.strip() for line in vocab]
    for char in vocab_list:
        if char.endswith(adj_suffix):
            adj_amount += 1
        elif char.endswith(noun_suffix):
            noun_amount += 1
        else:
            verb_amount += 1
temp = adj_amount
summary = 0
# for i in range(1, adj_amount):
#     print(i)
#     for k in range(1, i):
#         print(k)
#         elt = temp*(adj_amount - k)
#         temp = elt
#         print(temp)
#         adj_comb = temp + elt
#     summary += adj_comb
# print((adj_comb)*noun_amount*verb_amount)
adj_comb = (lambda n: sum(map(lambda k: reduce(mul, range(n-k, n+1), 1), range(n+1))))(adj_amount)
sentences = adj_comb*noun_amount*verb_amount
print(adj_comb)
print(sentences)

