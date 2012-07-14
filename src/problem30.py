#!/usr/bin/env python
#coding:UTF-8

def f(n):
    """nの各桁を5乗した数の和"""
    return sum( map((lambda x: int(x)**5), str(n)) )

list = []
for n in range(1, (9**5 * 6) + 1):
    if(n == f(n)):
        list.append(n)

print list
print sum(list) - 1



