#!/usr/bin/env python
# coding: utf-8

from utils import cal_time


def orderSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not stop and not found:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = False
            else:
                pos += 1
    return found
