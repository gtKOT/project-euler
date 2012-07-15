#!/usr/bin/env python
#coding:UTF-8

from mymath import isPowerOf
from math import sqrt

aLimit = 5
bLimit = 5
latterStart = int(sqrt(aLimit)) + 1
s = set([])

##for a in range(2, aLimit+1):
##    for b in range(2, bLimit+1):
##            s.add(a**b)
## print len(s)

for a in range(2, latterStart):
    for b in range(2, bLimit + 1):
        num = a**b

        for base in range(2, bLimit + 1):
            if isPowerOf(base, num):
                break

        s.add(num)

latterSum = (aLimit - latterStart + 1) * (bLimit - 2 + 1)

print len(s) + latterSum