#!/usr/bin/env python
#coding:UTF-8



def isEven(num):
    return (num & 1) == 0

def isOdd(num):
    return (num & 1) == 1



# 不足数
def isDeficientNumber(num):
    return num > sumOfProperDivisors(num)

# 完全数
def isPerfectNumber(num):
    return num == sumOfProperDivisors(num)

# 過剰数
def isAbunduntNumber(num):
    return num < sumOfProperDivisors(num)



# numの約数の総和
def sumOfDivisors(num):
    if num == 1:
        return 1

    total = 1
    primes = getPrimes(num)
    indexes = getPrimeFactorizationIndexes(num)

    while len(indexes) != 0:
        part = 1
        prime = primes.pop(0)

        for index in range(0, indexes.pop(0)):
            part += prime**index

        total *= part

    return total

# numの真の約数の総和
def sumOfProperDivisors(num):
    return sumOfDivisors(num) - num



def isLeap(year):
    return (year % 4 == 0) and not( (year % 400 != 0) and (year % 100 == 0) )



# num以下の素数リストを取得 (エラトステネスの篩)
def getPrimes(num):
    if num <= 1:
        return []
    if num == 2:
        return [2]

    searchList = range(3, num+1, 2)
    primeList = [2]

    while primeList[-1]**2 < searchList[-1]:
        prime = searchList.pop(0)
        primeList.append(prime)

        for i in range(prime**2, searchList[-1]+1, prime):
            if i in searchList:
                searchList.remove(i)

    return primeList + searchList



# numの素因数分解結果の肩リストを返す
def getPrimeFactorizationIndexes(num):
    if num <= 0:
        return []
    if num == 1:
        return [0]

    tmp = num
    indexes = []
    primes = getPrimes(num)

    while len(primes) != 0:
        index = 0
        prime = primes.pop(0)

        while tmp%prime == 0:
            tmp /= prime
            index += 1
        indexes.append(index)

        if tmp == 1:
            break

    return indexes



#temporary
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result



#temporary
def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)



def permutation(n, r):
    rhs = 1
    for i in range(r, n+1):
        rhs *= i
    return rhs



def isPowerOf(base, targetNum):
    """
    targetNumがbaseのべき乗ならば,True.
    そうでなければ,False.
    """
    while targetNum != 1:
        if targetNum % base != 0:
            return False
        targetNum /= base
    return True



def digitOf(num):
    """targetの(10進数での)桁数を返す."""
    if num == 0:
        return 0

    digit = 0
    while num != 0:
        num /= 10
        digit += 1
    return digit

