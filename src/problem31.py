#!/usr/bin/env python
#coding:UTF-8

def coinsUpto(bound):
    if bound == 200:
        return [1, 2, 5, 10, 20, 50, 100, 200]
    elif bound == 100:
        return [1, 2, 5, 10, 20, 50, 100]
    elif bound == 50:
        return [1, 2, 5, 10, 20, 50]
    elif bound == 20:
        return [1, 2, 5, 10, 20]
    elif bound == 10:
        return [1, 2, 5, 10]
    elif bound == 5:
        return [1, 2, 5]
    elif bound == 2:
        return [1, 2]
    else:
        return [1]

waysCache = {}

def numOfWays(amount, coinsBound):
    if amount == 0:
        return 1
    if waysCache.has_key(amount + 1000*coinsBound):
        return waysCache[amount + 1000*coinsBound]

    num = sum( numOfWays(amount-coin, coin) for coin in coinsUpto(coinsBound) if amount >= coin)
    waysCache[amount + 1000*coinsBound] = num
    return num


print numOfWays(200, 200)

