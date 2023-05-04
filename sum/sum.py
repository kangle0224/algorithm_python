#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(self.nums)
        for j in range(0,length-1):
            for k in range(1, length):
                if self.nums[j] + self.nums[k] == self.target:
                    return j, k

s=Solution([2,7,11,15],9)
print(s.twoSum())

