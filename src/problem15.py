#!/usr/bin/env python
#coding: utf-8

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

print comb(40, 20)