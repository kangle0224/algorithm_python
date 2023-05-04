#!/usr/bin/env python
# coding: utf-8

import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("func %s use % seconds." % (func.__name__, end_time - start_time))
        return result

    return wrapper