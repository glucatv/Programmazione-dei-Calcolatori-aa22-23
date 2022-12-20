# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:06:00 2022

@author: Gianluca
"""

# In[Esercizio 1 e 2]

def bubble_sort( a ):
    ordinata = False
    j = 0
    n = len(a)

    while not ordinata:
        ordinata = True
        i = 0
        while i < n-1-j:
            if a[i] > a[i+1]:
                # se la lista è ordinata non entro
                a[i], a[i+1] = a[i+1], a[i]
                ordinata = False
            i += 1
        j += 1
        
L = [5,3,9,2,1,0,9]
bubble_sort(L)
print(L)

# Il ciclo interno viene eseguiro n-1-j volte dove j conta quante volte viene
# eseguito il ciclo esterno. Al massimo può essere eseguito n-1 volte.
# Nel caso peggiore il ciclo interno è eseguito
# (n-1) + (n-2) +...+ 1 = O(n**2) che è il costo dell'algoritmo nel caso peggiore.
# Nel caso migliore viene eseguito una sola volta con un costo di O(n)

# In[Esercizio 3]

def bubble_sort(a, inplace=True):
    '''
    Input:  a, una lista di str; inplace un bool
    Output: ordina le stringhe in a dalla più corta alla più lunga, ritorna la lista ordinata.
    	Se inplace è True la funzione muta a, altrimenti viene restituita una nuova lista
    	con le stringhe di a ordinate come richiesto
    '''
    
    if inplace:
        b = a
    else:
        b = a[:]  
    
    ordinata = False
    j = 0
    n = len(a)

    while not ordinata:
        ordinata = True
        i = 0
        while i < n-1-j:
            if len(b[i]) > len(b[i+1]):
                # se la lista è ordinata non entro
                b[i], b[i+1] = b[i+1], b[i]
                ordinata = False
            i += 1
        j += 1  
        
    return b
    
L = ['print', 'while', 'for', 'list', 'int', 'not', 'def', 'in', 'and', 'or']
M = bubble_sort(L, inplace=True)
print(L)
print(M)

# In[]

def bubble_sort(a, key=lambda x:x, inplace=True):
    '''
    Input:  a, una lista; inplace un bool, key una
        funzione che assegna valori agli elementi di a
    Output: ordina gli elementi in a in ordine crescente
        rispetto ai valori che key assegna agli elementi
        di a, ritorna la lista ordinata.
    	Se inplace è True la funzione muta a, altrimenti viene restituita una nuova lista
    	con le stringhe di a ordinate come richiesto
    '''
    
    if inplace:
        b = a
    else:
        b = a[:]  
    
    ordinata = False
    j = 0
    n = len(a)

    while not ordinata:
        ordinata = True
        i = 0
        while i < n-1-j:
            if key(b[i]) > key(b[i+1]):
                # se la lista è ordinata non entro
                b[i], b[i+1] = b[i+1], b[i]
                ordinata = False
            i += 1
        j += 1  
        
    return b
    
L = ['print', 'while', 'for', 'list', 'int', 'not', 'def', 'in', 'and', 'or']
M0 = bubble_sort(L, key=len, inplace=False)
print(M0)
M1 = bubble_sort(L, key=str, inplace=False)
print(M1)
L = [1, 5, 10, 3, 9, 40, 34.5, 34.1]
M2 = bubble_sort(L, key=lambda x:x, inplace=False)
print(M2)
M3 = bubble_sort(L, inplace=False)
print(M3)

# In[]

L = [3, 'uno', 5, 0, 'quattro', 'nove', 'due', 9, 2, 10]

# Ordinare L in modo che i numeri precedano le stringhe,
# i numeri siano ordinati dal più piccolo al più grande,
# le stringhe in modo lessicografico

def num_str( v ):
    if type(v) in (float, int):
        return (0, v)
    else:
        return (1, v)
    
M0 = bubble_sort(L, key=num_str, inplace=False)
print(M0)

# se t0 e t1 sono due tuple, t0 < t1 se nella prima posizione in cui le due tuple
# differiscono, diciamo i,  t0[i] < t1[i]
#
# la funzione num_str se usata come parametro key assegna valori pù piccoli ai numeri
# e più grandi alle stringhe. Quindi i numeri precederanno le stringhe. All'interno
# della sequenza dei numeri (o delle stringhe), verrà utilizzato il valore, ovvero
# il secondo elemento della tupla

# In[]
L = [ 8,1, 10, 3]
L.sort()
print(L)
L = ( 8,1, 10, 3)
L1 = sorted(L)
print(L1)