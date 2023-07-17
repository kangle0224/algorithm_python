#!/usr/bin/env python
# coding: utf-8

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []


def leftmatchright(left, right):
    lefts = "([{"
    rights = ")]}"
    # 判断左右两个的位置是否一致
    if lefts.index(left) == rights.index(right):
        return True
    else:
        return False


def judgeStr(strItem):
    t = Stack()
    balance = True
    index = 0

    while index < len(strItem) and balance:
        str_per = strItem[index]

        if str_per in "([{":
            t.push(str_per)
        else:
            if t.isEmpty():
                balance = False
            else:
                left = t.pop()
                if not leftmatchright(left, str_per):
                    balance = False

        index += 1

    if t.isEmpty() and balance:
        return True
    else:
        return False


a1="()"
a2="()[]{}"
a3="(]"
res1=judgeStr(a1)
res2=judgeStr(a2)
res3=judgeStr(a3)
print(res1)
print(res2)
print(res3)
