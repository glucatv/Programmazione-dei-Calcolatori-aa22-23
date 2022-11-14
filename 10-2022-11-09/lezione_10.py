    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:56:53 2022

@author: gianluca
"""

# In[Esercizio per casa]

def init_tuple(n, v=None):
    if v == None:
        return (0, )*n
    t = ()
    for i in range(n):
        # concateno (v(i), ) a t
        t += (v(i), )
    return t

# In[Seconda versione]

def init_tuple(n, v = lambda x: 0 ):
    t = ()
    for i in range(n):
        # concateno (v(i), ) a t
        t += (v(i), ) # richiede i+2 operazioni
    return t

t0 = init_tuple(10, str)
print(t0)
t1 = init_tuple(10)
print(t1)

# In[]

t2 = init_tuple(10, v = lambda k: 2*k+1)
print(t2)

t3 = init_tuple(10, v = lambda k: 'X'*(k+1))
print(t3)

t4 = init_tuple(10, v = lambda k: (k,)*10)
print(t4)

# In[]

t5 = t4 + t0
print(t0)

# In[Liste]

a0 = [] #lista vuota
a1 = [9, 'python', (1,2), [], 3.14]
a2 = ['ciao']

# supporta: indicizzazione, slicing, concatenazione, ripetizione, funzione le

a3 = a1 +a2 #nuova lista richiede len(a1)+len(a2) operazioni elementari
a4 = a1*2 # nuova lista richiede 2*len(a1) operazioni elementari

print(a1, a2, a3) 

a2.append('mondo') # una operazione elementare

print(a2)

a2[0] = 'Ciao'

print(a2)

del(a2[0])

print(a2)

print(a4)

a4[2] = None

print(a4)



