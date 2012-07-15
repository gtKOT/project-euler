#!/usr/bin/env python
#coding: utf-8

days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def isLeap(year):
    return (year % 4 == 0) and not( (year % 400 != 0) and (year % 100 == 0) )

def daysOfMonth(year, month):
    if isLeap(year) and month == 2:
        return days[month] + 1
    else:
        return days[month]

start = 1       ## 1900/1/1 は月曜日
for month in range(1, 13):
    start += daysOfMonth(1900, month)

start %= 7      ## 1901/1/1
count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if start == 0:
            count += 1
        start = (start + daysOfMonth(year, month)) % 7

print count