#!/usr/bin/env python
#coding: utf-8

def devideNumAMAP(num, div, primeFactorization):
    count = 0
    while num % div == 0:
        num /= div
        count += 1
        if num == 1 or num == 0:
            break
    primeFactorization[div] = count
    return num

def primeFactorize(num):
    primeFactorization = {}
    div = 2
    num = devideNumAMAP(num, div, primeFactorization)
    div = 3
    while(num > 1):
        num = devideNumAMAP(num, div, primeFactorization)
        div += 2
    return primeFactorization

def sumOfDivisors(num):
    primeFacts = primeFactorize(num)
    sum = 1
    for key in primeFacts.keys():
        factor = 1
        for i in range(1, primeFacts[key] + 1):
            factor += key ** i
        sum *= factor
    return sum

def realSumOfDivisors(num):
    return sumOfDivisors(num) - num

def isFriendNum(num):
    partner = realSumOfDivisors(num)
    if partner == num:
        return False
    return num == realSumOfDivisors(partner)

limit = 10000
sum = 0
for i in range(0, limit + 1):
    if isFriendNum(i):
        print "friend number: " + str(i)
        sum += i
print sum