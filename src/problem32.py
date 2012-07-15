#!/usr/bin/env python
#coding:UTF-8

def check(num, already):
    for dig in str(num):
        if dig in already:
            return False
        else:
            already.append(dig)

    return True;


def checkTriple(num1, num2, num3):
    already = ["0"]

    return check(num1, already) and check(num2, already) and check(num3, already)



suitable = set();

# check [1dig * 4dig = 4dig]
for oneDig in range(1, 10):
    for fourDig in range(1000, 10000):
        right = oneDig * fourDig

        if right >= 10000:
            break

        if checkTriple(oneDig, fourDig, right):
            suitable.add(right)
            print [oneDig, fourDig, right]

# check [2dig * 3dig = 4dig]
for twoDig in range(10, 100):
    for threeDig in range(100, 1000):
        right = twoDig * threeDig

        if right >= 10000:
            break

        if checkTriple(twoDig, threeDig, right):
            suitable.add(right)
            print [twoDig, threeDig, right]

print sum(suitable)