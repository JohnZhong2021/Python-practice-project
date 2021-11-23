# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 18:51:59 2021

@author: zhongqiang
"""

def fibonacci_num(i):
    j = 3
    f1 = 1
    f2 = 1
    if i == 1 or i == 2:
        return 1
    else:
        while j <= i:
            f = f1 + f2
            f2 = f1
            f1 = f
            j += 1
        return f
for i in range(1, 45):
    print(fibonacci_num(i), end=" ")

