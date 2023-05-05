#!/usr/bin/env python
# coding: utf-8

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid], item)
            else:
                return binarySearch(alist[mid + 1:], item)


alist = [1, 2, 3, 4, 5, 6, 7, 8]
print(binarySearch(alist, 7))
