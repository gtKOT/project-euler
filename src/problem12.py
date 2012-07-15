#!/usr/bin/env python
#coding: utf-8

divisors = []

def devideNumAMAP(num, divisor):
    count = 0
    while num % divisor == 0:
        num /= divisor
        count += 1
    divisors.append(count)
    return num

def numOfDivisors(num):
    global divisors
    tmp = num
    div = 2
    tmp = devideNumAMAP(tmp, div)
    div = 3
    while(tmp > 1):
        tmp = devideNumAMAP(tmp, div)
        div += 2

    numOfDevs = 1
    for i in divisors:
        numOfDevs *= i + 1
    divisors = []

    return numOfDevs

triNum = 1
nextNum = 2
numOfDevs = 0
while(True):
    triNum += nextNum
    nextNum += 1
    print triNum
    if(numOfDivisors(triNum) >= 501):
        break

print triNum