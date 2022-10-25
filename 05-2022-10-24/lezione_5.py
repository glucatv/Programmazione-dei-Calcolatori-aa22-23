#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:57:14 2022

@author: gianluca
"""

# In[]

x = 'programmgrazione'
#y = 'gramma'
y = 'grxa'



p, trovato = 0, False
while p <= len(x)-len(y) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se y è in x a partire da p
    q = 0
    while q < len(y) and x[p+q] == y[q]:
        q += 1
    if not (q < len(y) ):
        print(y + ' compare in posizione ' + str(p) + ' di ' + x)
        trovato = True
        
    p += 1
    
if not trovato:
    print('non esiste corrispondenza')
    
# In[]

x = 'programmgrazione'
#y = 'gramma'
y = 'gra'



p, trovato = 0, False
while p <= len(x)-len(y) and not trovato: # modificato tenendo conto che possa aver successo...
    # verifico se y è in x a partire da p
    q = 0
    while q < len(y) and x[p+q] == y[q]:
        q += 1
    if not (q < len(y) ):
        trovato = True
        break # esce dal ciclo più interno
    p += 1
    
if not trovato:
    print('non esiste corrispondenza')
else:
    print(y + ' compare in posizione ' + str(p) + ' di ' + x)
    
    
# In[]

x = 'programmgrazione'
#y = 'gramma'
y = 'gra'

p = 0
while p <= len(x)-len(y): # modificato tenendo conto che possa aver successo...
    # verifico se y è in x a partire da p
    q = 0
    while q < len(y) and x[p+q] == y[q]:
        q += 1
    if not (q < len(y) ):
        break # esce dal ciclo più interno
    p += 1
    
if not (p <= len(x)-len(y)):
    print('non esiste corrispondenza')
else:
    print(y + ' compare in posizione ' + str(p) + ' di ' + x)
# In[Slicing]

x = 'programmazione'

x0 = x[1:4]
x1 = x[:4]
x2 = x[3:len(x)]
x3 = x[3:]
x4 = x[:]
x5 = x[3::2]
x6 = x[6:1:-1]
x7 = x[::-1]


print( x0 )
print( x1 )
print( x2 )
print( x3 )
print( x4 )
print( x5 )
print( x6 )
print( x7 )





