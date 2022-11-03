#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:53:40 2022

@author: gianluca
"""

# In[Soluzione esercizio per casa]
import random as rn

def r_float( n ):
    '''
    Input: n, un intero
    Output: un float pseudo-casuale in [0,1) con n cifre significative dopo
        il punto
    '''
    str_f = '0.'
    for c in range(n-1):
        # n-1 caratteri in 0...9
        str_f += str(rn.randint(0, 9))
    # l'ultimo carattere non deve essere 0
    str_f += str(rn.randint(1, 9))
    return float(str_f)

print(r_float(20))


# In[Docstring e return multipli]

def massima_intersezione( x, y ):
    '''
    Input: x ed y sono due stringhe
    Output: restituire il carattere in x che è il più frequente in y e la
        sua frequenza
    '''
    n_max, c_max = 0, None # unpacking
    for c in x:
        # conta il numero di volte in cui c compare in y
        n_c = 0
        for c_y in y:
            if c_y == c:
                n_c += 1
        if n_c > n_max:
            n_max, c_max = n_c, c
    return c_max, n_max

a, b = 'ciao', 'ramarro marrone'
c, n = massima_intersezione( a, b ) # unpacking
print(c, n)
    
# In[Funzioni con numero variabile di argomenti]

def f( *args ):
    for a in args:
        print(a)
        
f('ciao', 9, 'python', 3.14, True)

# In[Esempio: stampa verticale]
def print_v( *strings ):
    '''
    Input: un numero variabile di stringhe
    Stampa le stringhe in verticale, uno di fianco l'altra
    Restituisce: None
    
    Esempio print_v('ciao', 'python')
    
    cp
    iy
    at
    oh
     o
     n
    '''    
    
    r = 0 # numero di riga
    terminato = False
    while not terminato:
        terminato = True
        # definiamo la riga r
        riga_r = ''
        for a in strings:
            if len(a) > r:
                riga_r += a[r]
                terminato = False
            else:
                riga_r += ' '
        if not terminato:
            print(riga_r)
        r += 1
        
print_v('ciao', 'python', 'programmazione', 'java', 'c++')

# In[Astrazione e modularità]

def radice_quadrata( x, eps=0.01 ):
    # prima ipotesi
    g = x/2
    
    while abs( g*g - x ) > eps: # questo e' un ciclo
        g = 0.5 * ( g + x/g )

    return g

# attenzione se si modifica una implementazione di una funzione, per garantire
# la compatibilià l'interfaccia non deve essere mutata

def radice_quadrata(x, eps=10):
    return x**0.5

print(radice_quadrata(20, 0.000001))
print(radice_quadrata(20))
print(radice_quadrata(eps=0.000001, x = 90))

