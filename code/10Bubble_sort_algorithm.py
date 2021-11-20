# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:58:17 2021

@author: JohnZhong
"""
import random
def generate_ramdon_list(n):
    L = []
    i = 1
    while i<=n:
        L.append(random.randint(1,n))
        i += 1
    return L

def bubble_sort(L):
    n = len(L)
    if n == 1 or n==0:
        return L
    else:
        while n >= 2:
            j = 0
            while j < n-1:
                if L[j] > L[j+1]:
                    E = L[j+1]
                    L[j+1] = L[j]
                    L[j] = E
                else:
                    pass
                j += 1
            n -= 1
        return L
print(bubble_sort(generate_ramdon_list(100)))