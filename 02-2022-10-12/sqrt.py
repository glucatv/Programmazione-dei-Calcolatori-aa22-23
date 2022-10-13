#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:21:17 2021

@author: gianluca
"""


# input
x = 20 # assegnazione

# prima ipotesi
g = 5.0
print(g)

while abs( g*g - x ) > 0.00001: # questo e' un ciclo
    g = 0.5 * ( g + x/g )
    print(g)

print("La radice quadrata di", x, "è", g)

