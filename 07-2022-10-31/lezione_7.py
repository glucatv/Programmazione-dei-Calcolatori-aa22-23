#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:53:40 2022

@author: gianluca
"""

# In[]

def massima_intersezione( x, y ):
    '''
    Input: x ed y sono due stringhe
    Output: restituire il carattere in x che è il più frequente in y
    '''
    n_max, c_max = 0, None # soluzione parziale
    for c in x:
        # conta il numero di volte in cui c compare in y
        n_c = 0
        for c_y in y:
            if c_y == c:
                n_c += 1
        if n_c > n_max:
            n_max, c_max = n_c, c
    return c_max

a, b = 'ciao', 'ramarro marrone'
r = massima_intersezione(a, b)
if r != None:
    print(f'Il carattere di \'{a}\' che compare più volte in \'{b}\' è \'{r}\'')
else:
    print(f'\'{a}\' e \'{b}\' non hanno caratteri in comune')
    
# In[]

print('prima riga\nseconda riga\ttabulazione') # caratteri speciali

# In[]

def f(x):
    x += 1
    for y in range(10):
        x += y
    return x

x = 100
y = 25
print(f(x))

# In[]

def radice_quadrata( x, eps=0.01 ):
    # prima ipotesi
    g = x/2
    
    while abs( g*g - x ) > eps: # questo e' un ciclo
        g = 0.5 * ( g + x/g )

    return g

print(radice_quadrata(20, 0.000001))
print(radice_quadrata(20))
print(radice_quadrata(eps=0.000001, x = 90))

# In[]
print('prima', 'ariprima', sep='*', end=' ')
print('seconda')
