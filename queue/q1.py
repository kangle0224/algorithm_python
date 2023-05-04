#!/usr/bin/env python
# coding: utf-8

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
q.enqueue("lion")
q.enqueue(123)
print(q.size())
print(q.dequeue())
print(q.size())

