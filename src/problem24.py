#!/usr/bin/env python
#coding:UTF-8

import sys
from mymath import *

##def getDigit(num):
##    digit = 0
##    while num >= 1:
##        digit += 1
##        num -= permitation(10, digit)
##    return digit

limit = 1000000
digitNums = range(10)
count = 0
num = 0

def createNum(depth, digitNum):
    global count
    global num

    digitNums.remove(digitNum)

    if len(digitNums) == 0:
        count += 1
        if count == limit:
            num += digitNum * 10**depth
    else:
        digitNums.sort()
        list = digitNums[:]
        for i in list:
            createNum(depth+1, i)
            if count == limit:
                num += digitNum * 10**depth
                break

    digitNums.append(digitNum)

for i in range(10):
    createNum(0,i)
print num




