#!/usr/bin/env python
# coding: utf-8

"""
给定一个m*n的二维列表，查找一个数是否存在。列表有下列特征：
每一行的列表从左到右已经排序好
每一行第一个数比上一行最后一个数大
"""
from utils import cal_time

@cal_time
def searchMatrix(matrix, target):
    """

    :param matrix:
    :param target:
    :return:
    """
    h = len(matrix)
    if h == 0:
        return False
    w = len(matrix[0])
    if w == 0:
        return False
    left = 0
    right = h * w - 1
    while left <= right:
        mid = (left + right) // 2
        i = mid // w
        j = mid % w
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(searchMatrix(a, 14))
