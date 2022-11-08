#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:46:56 2022

@author: gianluca
"""

def hist(h0, h1, *numbers):
    seg0, seg1, seg2 = 0, 0, 0
    for x in numbers:
        if x < h0:
            seg0 += 1
        elif x < h1:
            seg1 += 1
        else:
            seg2 += 1
    return seg0, seg1, seg2


i0, i1, i2 = hist(-7, 5, 3, 10, -4, 5, -12, 6, 0)

t = hist(0, 5, 3, 10, -4, 5, -12, 6, 0)

print(i0, i1, i2)

# In[Tuple]

t = (1, 'python', 3.14, (0,1) )   # packing
t = 1, 'python', 3.14, (0,1) 
print(t)

x = t[2] # indicizzazione
print(x)

print(t[1:3]) # slicing
print(t[::-1]) # slicing con step negativo

# t[2] = 4 # non ammissibile, le tuple sono immutabili

x0, x1, x2, x3 = t # unpacking

print(x0, x1, x2, x3)

print(len(t))

# In[]

def identita(x):
    return x

def str_cmp(x, y, key=str):
    '''
    Input: x, y, due stringhe; key una funzione con input str
    Output: ritorna -1 se key(x) < key(y); 0 se key(x) è uguale a key(y);
        +1 se key(y)< key(x)
    '''
    if key(x) < key(y):
        return -1
    if key(x) == key(y):
        return 0
    return 1

def str_cmp(x, y, key=None):
    '''
    Input: x, y, due stringhe; key una funzione con input str
    Output: ritorna -1 se key(x) < key(y); 0 se key(x) è uguale a key(y);
        +1 se key(y)< key(x)
    '''
        
    x0, y0 = (x, y) if key == None else (key(x), key(y)) # espressione condionale

    if x0 < y0:
        return -1
    if x0 == y0:
        return 0
    return 1



print(str_cmp('Addio', 'addio', len))
print(str_cmp('Addio', 'addio', str))
print(str_cmp('Addio', 'addio', identita))
print(str_cmp('Addio', 'addio'))

# In[]

'''
Esercizio: descrivere come utilizzare la funzione str_cmp in modo che vengano
confrontati i caratteri in posizione 0 di due
stringhe in input x e y. In particolare ritorna -1 se x[0] < y[0];
ritorna 0 se x[0] == y[0]; ritorna +1 altrimenti
'''

def primo_elemento(x):
    return x[0]

print(str_cmp('aio', 'addio', primo_elemento))

# In[funzioni lambda]

print( (lambda x: x+1)(1) )

print( str_cmp('aio', 'addio', lambda x: x[0]) )

f = lambda x: x**2 + 2*x + 6

print(f(10))

def str_cmp(x, y, key = lambda x:x):
    '''
    Input: x, y, due stringhe; key una funzione con input str
    Output: ritorna -1 se key(x) < key(y); 0 se key(x) è uguale a key(y);
        +1 se key(y)< key(x)
    '''
    if key(x) < key(y):
        return -1
    if key(x) == key(y):
        return 0
    return 1

print(str_cmp('aio', 'addio'))

# In[Metodi]

a = 'Python'

print( a.islower() )

t = (0,1,0)

print(t.count(0))

a.
