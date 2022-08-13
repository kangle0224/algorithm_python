#!/usr/bin/env python
# coding: utf-8

"""
heap sort
堆排序过程
1. 建立堆
2. 得到堆顶元素，为最大元素
3. 去掉堆顶元素，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
4. 堆顶元素为第二大元素
5. 重复步骤3， 直到堆变空
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
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有且比较大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大，把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级领导位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上

