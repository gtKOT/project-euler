#!/usr/bin/env python
#coding:UTF-8

def charToScore(char):
    return ord(char) - 64

def nameToScore(name):
    score = 0
    for c in name:
        score += charToScore(c)
    return score

file = open(r"D:\Documents\python_workspace\ProjectEuler\names.txt", "r")
names = file.readline().strip('"').split('","')  # replace使おう stripは先頭と末尾のみ
names.sort()

score = 0
for i in range( len(names) ):
    score += (i+1) * nameToScore(names[i])
print score