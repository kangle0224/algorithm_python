#!/usr/bin/env python
# coding: utf-8

def radix_sort(li):
    max_num = max(li)  # 最大值
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        # 分桶
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        li.clear()
        # 把数重新写回列表
        for buc in buckets:
            li.extend(buc)
        it += 1


import random
li =list(range(100))
random.shuffle(li)

radix_sort(li)
print(li)
