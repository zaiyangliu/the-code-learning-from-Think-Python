# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 07:51:59 2018

@author: zaiyangliu
"""
import re  #利用正则表达式判断输入是否为正数

def is_triangle(a,b,c):
    if (a + b) > c and (b + c) > a and (c + a) > b:
        print('Yes')
    else:
        print('No')

a=input('please input the length of triangle a\n')

while not re.findall('^[0-9]+$',a):
    a=input('this is not an integer')

b=input('please input the lenght of triangle b\n')

while not re.findall('^[0-9]+$',b):
    b=input('this is not an integer')

c=input('please input the length of triangle c\n')

while not re.findall('^[0-9]+$',c):
    c=input('this is not an integer')
    
is_triangle(int(a),int(b),int(c))
