#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:04:40 2022

@author: gianluca
"""

# In[Operatori tra tipi numerici]

x = 2
y = 7
z = x+y

pi = 3.14

w = pi+y

print(z, w)

y = 8

d = y/x

print(d)

d = y//x # divisione intera

print(d)

d = y//0.88 # divisione intera

print(d)

m = y%3 # modulo

print(m)

print(2**3)

# In[Operatori tra stringhe]

x, y = 'python', 'programmazione'

z = x+y   # concatenzione
print(z)

z = 2*x
print(z)

a = 'tho'
print(a in x)
print(a in y)
print('la lunghezza di x è', len(x))

x = input('Digita qualcosa ')

# In[esercizio]

x = input('Digita la prima stringa: ')
y = input('Digita la seconda stringa: ')

if x in y:
    print('la prima stringa è contenuta nella seconda')
elif y in x:
    print('la seconda stringa è contenuta nella prima')
else:
    print('le stringhe non si contengono')
    
# In[casting, float]

x = input('Digita un numero: ')
x = float(x)
if x < 0:
    print('Il numero è negativo')
else:
    print('Il numero è positivo')

# In[casting int, str]

x = int('1234')
print(x, type(x))

y = str(3.14)
print(type(y))

# In[indicizzazione]

x = 'programma'
print(x[2])


