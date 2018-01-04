# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
def polygon(t, n, length):
    angle=360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    length=circumference/n
    polygon(t,n,length)
import turtle
bob=turtle.Turtle()
circle(bob,70)
print(bob)
turtle.mainloop()
