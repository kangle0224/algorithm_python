#!/usr/bin/env python
# coding: utf-8

"""
栈帧：实现递归
"""
from utils import cal_time


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


rStack = Stack()


@cal_time
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr(n // base, base)


print(toStr(1234567890, 10))
