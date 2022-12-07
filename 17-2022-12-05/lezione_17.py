#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:13:09 2022

@author: gianluca
"""


def find_in_file(filename, k):
    '''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
    f = open(filename)    # O(1) ovvero costo costante
    lines = ()            # O(1) 
    r = 1 # riga corrente
    
    for line in f:         # eseguito O(n)
        if k in line:      # le len(line) è O(1), O(1) operazioni 
            lines += (r, ) # è O(len(lines))+1 
        r += 1
    
    f.close()         # O(1)
    return lines      # O(1)

t = find_in_file('lezione_17.py', 'lines')
print(t)
    
# COSTO COMPUTAZIONALE
#
# Nel caso peggiore, k in ogni riga, il costo è O(n^2)

# In[]

def find_in_file(filename, k):
    '''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
    f = open(filename)    # O(1) ovvero costo costante
    lines = []            # O(1) 
    r = 1 # riga corrente
    
    for line in f:          # eseguito O(n)
        if k in line:       # se len(line) è O(1), O(1) operazioni 
            lines.append(r) # O(1)
        r += 1
    
    f.close()         # O(1)
    return tuple(lines)      # nel caso peggiore O(n)

t = find_in_file('lezione_17.py', 'lines')
print(t)

# COSTO COMPUTAZIONALE
# 
# len(line) è O(1)
# Nel caso peggiore k in ogni riga, il costo è O(n)
#
# len(line) è O(m)
#
# if k in line: # se len(line) è O(m), O(m) operazioni 
#
# Nel caso peggiore il for richiede O(nm) operazioni
#
# Il costo della funzione è O(nm)

# In[]

def find_in_file( filename, k):
    '''
    Input: filename e k sono str, filename è il nome di un file
    Output: una tupla ( (r0, c0), (r1, c1), ...) di coppie di interi che indicano le
        righe e le colonne del file in cui compare k. Per colonna si intende la posizione
        all'interno della riga  
    '''
    f = open(filename)    # O(1) ovvero costo costante
    lines = []            # O(1) 
    r = 1 # riga corrente
    
    for line in f:          # eseguito O(n)
        for c in range(len(line)-len(k)+1):
            # verificare se  k è il line a partire dalla posizione c
            if k == line[c:c+len(k)]: # len(line)-len(k)+len(k)
                lines.append( (r, c+1) ) # O(1)
        r += 1
    
    f.close()         # O(1)
    return tuple(lines)      # nel caso peggiore O(n)

t = find_in_file('lezione_17.py', 'lines')
print(t)  

# lines lines lines fds fdsf dsfd sf ds lines

# In[Implementazione della ricerca binaria]


def bin_search( k, bins ):
    '''
    sia n-1 la lunghezza di bins, ritorna 0 se k < bins[0],
        n-1 se k >= bin[n-2], i se bins[i-1] <= k < bin[i]
    '''

    n = len(bins)+1
    
    if k < bins[0]:
        return 0
    if k >= bins[n-2]:
        return n-1
    
    lx, rx = 0, n
    trovato = False
    
    while not trovato:
        cx = (lx+rx)//2
        # cx è il segmento mediano tra lx e rx
        if k >= bins[cx-1] and k < bins[cx]:
            trovato = True
        elif  k < bins[cx-1]:
            # a sx del segmento cx
            rx = cx-1
        else:
            lx = cx+1
    
    return cx

print( bin_search(7, [6, 8, 10] ) )