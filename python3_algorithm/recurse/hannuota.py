#!/usr/bin/env python
# coding: utf-8

from utils import cal_time


def moveDisk(fp, tp):
    print("moving disk from %d to %d\n" % (fp, tp))

@cal_time
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

moveTower(3,1,3,2)
