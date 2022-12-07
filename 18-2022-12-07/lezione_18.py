#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:13:09 2022

@author: gianluca
"""

# In[Implementazione della ricerca binaria]


def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n-1 se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

    n = len(bins)+1 # numero di segmentio
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n-1
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2
        # cx è il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k >= bins[cx]:
            # a dx del segmento cx
            lx = cx+1
        else:
            rx = cx-1
    
    return cx

print( bin_search(12, [6, 10] ) )

# In[]

def hist( a, bins ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in v < bins[0]
        - h[n-1] = numero di elementi in v >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    
    n = len(bins)+1 # un numero costante (rispetto a n e m) di operazioni
    h = [0]*n       # circa n operazioni
    
    for k in a:
        i = bin_search(k, bins) # O(log n)
        h[i] += 1
        
    return h # un numero costante (rispetto a n e m) di operazioni

print( hist([1, 3, -8, 10, 12, 9], [0, 10, 20, 30]) )

# Costo computazionale (Complessità computazionale)
#
# O(m*log n) caso peggiore o è fisso?

# In[Funzione list]
t = (1,2,3,4)
a = list(t) # costo lineare
print(a)

b = list('python')
print(b)

c = list(range(10))
print(c)

# In[Comprensione di lista (list comprehension)]

a = [ i**2 for i in range(10) ]
print(a)

# In[]

def hist( a, bins = [ i*10 for i in range(10) ] ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in v < bins[0]
        - h[n-1] = numero di elementi in v >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
    
    n = len(bins)+1 # un numero costante (rispetto a n e m) di operazioni
    h = [0]*n       # circa n operazioni
    
    for k in a:
        i = bin_search(k, bins) # O(log n)
        h[i] += 1
        
    return h # un numero costante (rispetto a n e m) di operazioni

print( hist([1, 3, -8, 10, 12, 9]) )

# In[Dizionari]

d0 = {} # dizionario vuoto
d1 = { 'k0':6, 'k1':'python', 6:3.14 }

# lettura
print( d1['k1'] )
#print( d1['k9'] ) # non è una chiave del dizionario, errore!

if 'k9' in d1:
    print( d1['k9'] )
else:
    d1['k9'] = 'cappanove'
    
print(d1)

d1[6] = 'sei'

print(d1)

del(d1[6])  # elimina l'elemento con chiave 6

print(d1)

d1['L'] = [1]

print(d1)

d1['L'].append(0)

print(d1)

print(len(d1))

d1['k2'] = 6

print(d1.keys(), d1.values())