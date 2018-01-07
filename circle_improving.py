# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:01:26 2018

@author: zaiyangliu
"""
import math

def polyline(t, n, length, angle):
    
    for i in range(n):
        
        t.fd(length)
        
        t.lt(angle)

def polygon(t, n, length):
    
    angle=360/n
    
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length=2*math.pi*r*angle/360
   
    n=int(arc_length/3)+1
    
    step_length=arc_length/n
    
    step_angle=float(angle)/n
    
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    
    arc(t, r, 360)

import turtle

bob=turtle.Turtle()

arc(bob,7,70)

print(bob)

turtle.mainloop()
