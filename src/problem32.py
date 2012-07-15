#!/usr/bin/env python
#coding:UTF-8

def check(num, already):
    for dig in str(num):
        if dig in already:
            return False
        else:
            already.append(dig)

    return True


def checkDigOverlap(num1, num2, num3):
    already = ["0"]

    return check(num1, already) and check(num2, already) and check(num3, already)



suitable = set()

# check [1dig * 4dig = 4dig]
for oneDig in range(1, 10):
    for fourDig in range(1000, 10000):
        rhs = oneDig * fourDig

        if rhs >= 10000:
            break

        if checkDigOverlap(oneDig, fourDig, rhs):
            suitable.add(rhs)
            print [oneDig, fourDig, rhs]

# check [2dig * 3dig = 4dig]
for twoDig in range(10, 100):
    for threeDig in range(100, 1000):
        rhs = twoDig * threeDig

        if rhs >= 10000:
            break

        if checkDigOverlap(twoDig, threeDig, rhs):
            suitable.add(rhs)
            print [twoDig, threeDig, rhs]

print sum(suitable)