#!/usr/bin/env python
# coding: utf-8

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


alist = [1, 2, 3, 4, 5, 6]
print(binarySearch(alist, 4))
