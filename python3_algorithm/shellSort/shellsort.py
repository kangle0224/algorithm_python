#!/usr/bin/env python
# coding: utf-8

def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("after increments of size", sublistcount,
              "the list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
