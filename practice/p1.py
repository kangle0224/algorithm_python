#!/usr/bin/env python
# coding: utf-8

"""
给两个字符串s和t，判断t是否为s的重新排序后组成的单词
s = "anagram", t = "nagaram", return true
s = "rat", t = "car", return false
"""


# nlogn
def isAnagram(s, t):
    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    return ss == tt


s = "anagram"
t = 'nagaram'

print(isAnagram(s, t))


# 2
def isAnagram1(s, t):
    dict1 = {}
    dict2 = {}

    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1

    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2

print(isAnagram1(s,t))
