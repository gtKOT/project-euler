#!/usr/bin/env python
#coding:UTF-8

from mymath import getPrimes

def calc(n, a, b):
    return n**2 + a*n + b

primeList = [2];
maxLen = 0
aAtMax = -999
bAtMax = 3

for b in getPrimes(999):
    if b <= 38:
        continue

    for a in range(-(1+b), 1000):
        if a%2 == 0:
            continue

        n = 0
        while True:
            num = calc(n,a,b)

            if num > primeList[-1]:
                primeList = getPrimes(num + 1000)

            if not (num in primeList):
                break

            n += 1

        if n > maxLen:
            maxLen = n
            aAtMax = a
            bAtMax = b

print [maxLen, aAtMax, bAtMax]