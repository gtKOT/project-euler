#!/usr/bin/env python
#coding: utf-8

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = factorial(100 - 1)
sum = 0
for i in str(num):
    sum += int(i)

print num
print sum