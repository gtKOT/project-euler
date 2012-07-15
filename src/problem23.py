#!/usr/bin/env python
#coding:UTF-8

from mymath import *

limit = 28123

abundunts = [x for x in range(1, limit) if isAbunduntNumber(x)]
sumOfExpressables = 0

for i in range(1, limit):
    for abundunt in abundunts:
        another = i - abundunt
        if(another <= 0):
            break    # abundunts is sorted
        if(another in abundunts):
            sumOfExpressables += i
            break

print sum(range(1,limit)) - sumOfExpressables