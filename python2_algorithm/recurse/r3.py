#!/usr/bin/env python
# coding: utf-8

"""
乌龟画图
"""

from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(80)
        drawSpiral(myTurtle, lineLen-5)

drawSpiral(myTurtle, 50)
myWin.exitonclick()