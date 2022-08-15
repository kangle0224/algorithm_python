#!/usr/bin/env python
# coding: utf-8

"""
在计数排序中，如果元素的范围比较大(比如在1-1亿之间)，如何改造算法？
桶排序：首先将元素分在不同的桶中，对每个桶中的元素进行排序
"""


def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        i = min(var // (max_num // n), n - 1)  # 把var加到桶里面
        buckets[i].append(var)
        # 保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], \
                                                   buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)

    return sorted_li


import random

li = [random.randint(0, 100) for i in range(100)]
print(li)

li = bucket_sort(li)
print(li)
