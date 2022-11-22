# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:31:08 2022

@author: Gianluca
"""

def g(x, y):
    return 0 if x < y else 1

def f(k):
    n = k**2
    return g(n, k)

print(f(9))

# In[]

def f(n):
    if n == 0:
        return 0
    else:
        return 1+f(n-1)
   
k = 2
print(f(k))

# In[]

def max_ric(a):
    '''
    Input: una lista di numeri
    Output: massimo in a
        La funzione deve essere ricorsiva
        non si deve usare la funzione max
    '''
    n = len(a)
    if n == 1:
        return a[0]
    else:
        m = max_ric(  a[1:] )
        if a[0] > m:
            return a[0]
        else:
            return m
        
b = [1,7,2]
print(max_ric(b))
    