# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:02:03 2022

@author: Gianluca
"""

def merge( a, b ):
    '''
    Parameters
    ----------
    a,b : liste (in realtà iterabile) di interi (anche altro, purché
                            confrontabili con <)
    ordinati secondo la relazione <=

    Returns: una lista c contenente gli elementi di a e b ordinati
        secondo la relazione <=
    '''
    
    c = []
    i, j = 0, 0
    
    # sia n = len(a)+len(b)
    
    while i < len(a) and j < len(b): # eseguito <= n volte
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            
#    if i == len(a): # costo O(n) ma richiede slicing quindi memoria aggiuntiva
#        c.extend(b[j:])
#    else:
#        c.extend(a[i:])
        
    if i == len(a):
        t, k = b, j
    else:
        t, k = a, i
    
    while k < len(t): # O(n) senza richiedere memoria aggiuntiva
        c.append(t[k])
        k += 1
        
    return c

L0 = [1,5,9,10,11,20, 23]
L1 = [0,1,2,10,12,20, 21,23,24,29]
M = merge(L0, L1)
print(M)

# In[algoritmo merge sort]

def merge( a, lx, cx, rx ):
    '''
    Parameters
    ----------
    a : lista di valori confrontabili con < 
        con a[lx:cx] e a[cx:rx] ordinati
        lx<cx<rx
    
    Output: muta a in modo tale che a[lx:rx] sia ordinata 
    '''
    
    c = []
    i, j = lx, cx
    
    # sia n = len(a)
    # sia m = rx-lx
    
    while i < cx and j < rx: # eseguito <= m volte
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
        
    if i == cx:
        k, last_index = j, rx
    else:
        k, last_index = i, cx
    
    while k < last_index: # costo O(m)
        c.append(a[k])
        k += 1
        
    #a = a[:lx] + c + a[rx:] # costo O(n), non va bene!!!!
    
    for t in range(rx-lx): # costo O(m)
        a[lx+t] = c[t]
    
L = [10, 4, 5, 2, 5, 6, 0, 1, 2, 4, 0, 5, 4, 10]
merge(L, 3, 6, 10)
print(L)


def merge_sort(a, lx, rx):
    '''
    Parameters
    ----------
    a : lista di elementi per cui vale la relazione <
    lx < rx : int, indici in a
    Returns
    -------
    Muta a in modo tale che a[lx:rx] sia ordinata con <
    '''
    
    if rx  == lx  or rx == lx+1:
        return
    
    cx = (rx+lx)//2
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    merge(a, lx, cx, rx)
    
L = [10, 4, 5, 2, 5, 6, 0, 1, 2, 4, 0, 5, 4, 10]
merge_sort(L, 0, len(L))
print(L)
    