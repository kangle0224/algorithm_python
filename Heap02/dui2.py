#!/usr/bin/env python
# coding: utf-8

import heapq
import random

li = list(range(100))
random.shuffle(li)

print li
heapq.heapify(li)  # 建堆
n =len(li)
for i in range(n):
    print (heapq.heappop(li)),  # 弹出最小的数
