# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:51:59 2021

@author: JohnZhong
"""
def fibonacci_num(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibonacci_num(i - 1) + fibonacci_num(i - 2)
for i in range(1, 25):
    print(fibonacci_num(i), end=" ")
