#!/usr/bin/env python
# coding: utf-8

"""
将证书转换成2-16为进制基数的字符串
"""
from utils import cal_time


@cal_time
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
        # return convertString[n % base]+toStr(n // base, base)


print(toStr(123, 10))
