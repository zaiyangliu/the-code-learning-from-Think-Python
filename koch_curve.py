# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 07:51:59 2018

@author: zaiyangliu
"""
import turtle as tu

def Koch(length):
    """draw a Koch fractal curve recursively"""
    if length <= 2 :
        tu.fd(length)
        return
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)
    tu.rt(120)
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)

length = 300.0
tu.pu()         #画笔移动到（-150，90）以前不画
tu.goto(-150,90)
tu.pd()         #开始绘画
tu.title('Koch fractal curve')
Koch(length)

tu.mainloop()
