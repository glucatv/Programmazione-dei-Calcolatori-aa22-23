#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:01:56 2022

@author: gianluca
"""

# In[Esercizio per casa 1]

def init_list(n, v = lambda x: 0 ):
    t = []
    for i in range(n):
        t.append(v(i))
    return t

t0 = init_list(10, str)
print(t0)
t1 = init_list(10)
print(t1)

# In[Esercizio per casa 2]

def rem_none( a ):
    i = 0
    while i < len(a):
        if a[i] == None:
            del(a[i])
        else:
            i += 1
    return a

b = [0, None, 1, None, 2, None]
b = rem_none(b)
print(b)
b = [0, None, None, None, 2, None]
b = rem_none(b)
print(b)

# In[Operatore in]

print(2 in (4, 2, 9, 'ciao'))
print(2 in [4, 2, 9, 'ciao'])

# In[]

a = [1,5,4,3, 0]
b = (1,5,4,3, 0)
c = ['python', 'zorro', 'casa']

print( max(a), min(a), sum(a) )
print( max(4, 2, 1) )
print(min(b), sum(b))
print(max(c))

n = 12

print( max( [n**2, 1/n, (n+12)/2] ) )

# In[Esercizio]

def media_incrementale( a ):
    '''
    Input: a una lista di numeri (float o int)
    Output: una lista b t.c b[i] contenga la media dei primi i+1 elementi di a
    '''
    b = []
    for i in range(len(a)):
        b.append( sum(a[:i+1])/(i+1) )
    return b

def my_sum(a, k):
    somma = 0
    for i in range(k):
        somma += a[i]
    return somma
    

def media_incrementale( a ):
    '''
    Input: a una lista di numeri (float o int)
    Output: una lista b t.c b[i] contenga la media dei primi i+1 elementi di a
    '''
    b = []
    for i in range(len(a)):
        b.append( my_sum(a, i+1)/(i+1) )
    return b

def media_incrementale( a ):
    '''
    Input: a una lista di numeri (float o int)
    Output: una lista b t.c b[i] contenga la media dei primi i+1 elementi di a
    '''
    b, somma = [], 0
    for i in range(len(a)):
        b.append( (somma+a[i])/(i+1) )
        somma += a[i]
    return b

a = [1,2,3,4,5,6]
print( media_incrementale(a) )

# In[Aliasing e clonazione]

a = [10,10,10,5,5,0]
b = a # aliasing
c = a[:] # clonazione
b[1] = 'casa'
c[0] = None
print(a)
print(b)
print(c)

def make_none( a ):
    for i in range(len(a)):
        a[i] = None

make_none(a)
print(a)
print(b)
print(c)

