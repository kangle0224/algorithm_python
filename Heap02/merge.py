#!/usr/bin/env python
# coding: utf-8

"""
分解： 将列表越分越小，直至分成一个元素
终止条件：一个元素是有序的
合并：将两个有序列表归并，列表越来越大
"""


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只有左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # 肯定有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


def merge_sort(li, low, high):
    if low < high:  # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


li = list(range(10))
import random

random.shuffle(li)
print(li)
merge_sort(li, 0, len(li) - 1)
print(li)
