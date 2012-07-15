#!/usr/bin/env python
#coding: utf-8

max = 0
limit = 1000000

def isEven(num):
    return (num % 2) == 0

def next(num):
    if isEven(num):
        return num / 2
    else:
        return 3*num + 1

dict = {}
for start in range(1, limit):
    length = 0
    tmp = start
    while(tmp != 1):
        if(dict.has_key(tmp)):
            length += dict[tmp]
            break
        else:
            tmp = next(tmp)
            length += 1

    if(length > max):
        max = length
        print "start: " + str(start)
        print "maxLen: " + str(max)

    dict[start] = length

##for start in range(1, limit):
##    count = 1
##    tmp = start
##    while(tmp != 1):
##        if(isEven(tmp)):
##           tmp = tmp / 2
##        else:
##           tmp = 3*tmp + 1
##        count += 1
##    if(count > max):
##        max = count
##        print start
##        print max

