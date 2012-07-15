#!/usr/bin/env python
#coding:UTF-8


def sumOfCircuit(n):
    """一辺の長さがnの周の4頂点の和 (ただし, n≧3)"""
    return 4*n**2 - 6*n + 6

total = 1  # 最初の1
for n in range(3, 1002, 2):
    total += sumOfCircuit(n)

print total