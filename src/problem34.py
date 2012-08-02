#!/usr/bin/env python
#coding:UTF-8

from mymath import factorial

accept = []

facts = map(factorial, range(0, 10))

for num in range(0, 1000000):
    if num == sum([facts[int(dig)] for dig in str(num)]):
        accept.append(num)

print accept
print sum(accept)