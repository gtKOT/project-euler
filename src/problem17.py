#!/usr/bin/env python
#coding: utf-8

numDict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
        6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
        11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
        16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
        20:"twenty", 30:"thirty", 40:"forty", 50:"fifty",
        60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety",
        100:"hundred"}

def numToEnglish(num):
    if(num == 1000):
        return "onethousand"

    english = ""
    if(num >= 100):
        english += numDict[num / 100] + numDict[100]
        num %= 100
        if(num == 0):
            return english
        english += "and"

    if(num >= 20):
        english += numDict[(num / 10) * 10]
        num %= 10
        if(num == 0):
            return english

    english += numDict[num]
    return english


sum = 0
for i in range(1, 1001):
    print str(len(numToEnglish(i))) + " " + numToEnglish(i)
    sum += len(numToEnglish(i))
print sum
