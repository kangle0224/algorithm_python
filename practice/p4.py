#!/usr/bin/env python
# coding: utf-8

"""
给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数。保证肯定仅有一个结果。
例如，列表[1,2,3,4,5]与目标整数3,1+2=3，结果为(0,1)
输入的列表无序
"""

from utils import cal_time


def binary_search(li, left, right, val):
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid][0] == val:
            return mid
        elif li[mid][0] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # 待查找的值在mid右侧
            left = mid + 1
    else:
        return None


def twoSum(nums, target):
    """

    :param nums:
    :param target:
    :return:
    """
    new_nums = [[num, i] for i, num in enumerate(nums)]
    new_nums.sort(key=lambda x: x[0])

    for i in range(len(nums)):
        a = new_nums[i][0]
        b = target - a
        if b >= a:
            j = binary_search(new_nums, i + 1, len(new_nums) - 1, b)
        else:
            j = binary_search(new_nums, 0, i - 1, b)

        if j:
            break

    return sorted([new_nums[i][1], new_nums[j][1]])


li = [2, 6, 7, 9]
print(twoSum(li, 8))
