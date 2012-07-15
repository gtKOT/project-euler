#!/usr/bin/env python
#coding:UTF-8

def getLen(num):
    return len(str(num))

def getCycleLength(num):
    length = 0
    history = [1]
    tmp = 10

    while True:
        while getLen(tmp) <= getLen(num):
            tmp *= 10
            length += 1

        remainder = tmp % num
        if remainder == 0:
            return 0

        if remainder in history:
            return length + (len(history) - history.index(remainder))
        else:
            history.append(remainder)

        tmp = remainder * 10

max = 0
num = 0
for i in range(2, 1000):
    tmp = getCycleLength(i)
    if(tmp > max):
        max = tmp
        num = i
print num