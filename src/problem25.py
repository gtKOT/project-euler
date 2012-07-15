#!/usr/bin/env python
#coding:UTF-8

def digitCheck(n):
    return n >= 10**999

a = 1
b = 1
tmp = 0

index = 2

while True:
    index += 1
    tmp = a + b

    if digitCheck(tmp):
        print "index:" + str(index) + " value:" + str(tmp)
        break

    a = b
    b = tmp