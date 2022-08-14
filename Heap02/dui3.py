#!/usr/bin/env python
# coding: utf-8


"""
topk问题:
现在有n个数，设计算法得到前k大的数
解决思路：
1. 排序后切片  O(nlogn)
2. 排序Lowb三人组 O(kn)
3. 堆排序 O(nlogk)

堆排序思路：
1. 取列表前k个元素建立一个小根堆。堆顶就是目前第k大的数
2. 依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；如果大于堆顶，则将堆顶更换为该元素，并对堆进行一次调整。
3. 遍历列表所有元素后，倒序弹出堆顶。
"""


def sift(li, low, high):
    """

    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素位置
    :return:
    """

    i = low  # i最开始指向跟节点
    j = 2 * i + 1  # j最开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右孩子有且比较大
            j = j + 1  # j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大，把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级领导位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def topk(li, k):
    heap = li[0:k]
    # 1.建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)

    # 2.遍历
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    # 出数
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


import random

li = list(range(100))
random.shuffle(li)

print(topk(li, 10))
