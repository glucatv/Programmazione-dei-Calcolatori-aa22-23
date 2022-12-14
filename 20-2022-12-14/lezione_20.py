#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:03:35 2022

@author: gianluca
"""

# In[esercizio 1]

def dizionario_iniziali( a ):
    '''
    Input: una lista di n stringhe
    Output: un dizionario d che mappa caratteri in liste di stringhe tale che
        se d[k] = b, b contiene tutte le stringhe in a che iniziano per k 
    '''
    d = {}              # O(1)
    for x in a:         # per n volte
        if x == '':     # O(1)
            continue # torno a testare la condizione del ciclo saltando
                    # la  parte restante del blocco
        k = x[0]        # O(1)
        if k in d:      # O(1)
            d[k].append(x) # O(1) lettura del dizionario + O(1) per append
        else:
            d[k] = [x]  # O(1) costo per creare la lista + O(1) per scrittura
                        # nel dizionario
    return d

a = ['python', 'for', 'codice', 'programma', '', 'input', 'while', 'for', 'in']
d = dizionario_iniziali(a)
print(d)

# complessità computazionale:
#
# n*O(1) operazioni per il for, ovvero O(n) 


# In[Soluzione con metodo get]

import os

def analizza_test( cartella ):
    '''
    Assumiamo che n sia la dimensione complessiva dei file da analizzare
    '''
    d = {}
    for filename in os.listdir(cartella):
        if filename.split('.')[-1] == 'csv':
            print(filename)
            # analizziamo filename
            filepath = os.path.join(cartella, filename)
            f = open(filepath)
            for line in f: # per ogni riga di tutti i file (per n volte)
                # elaborare line
                k, v = line.split(';') # unpacking
                v = int(v)
                a = d.get(k, [])
                a.append(v)
                d[k] = a 
                
            f.close()
    return d

# Complessità computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati

d = analizza_test('.')
print(d)

# In[Soluzione con metodo get]


def analizza_test( cartella ):
    '''
    Assumiamo che n sia la dimensione complessiva dei file da analizzare
    '''
    d = {}
    mappa_punti_valori = {6:0.3, 7:0.4, 8:0.6, 9:1, 10:1.5}
    for filename in os.listdir(cartella):
        if filename.split('.')[-1] == 'csv':
            print(filename)
            # analizziamo filename
            filepath = os.path.join(cartella, filename)
            f = open(filepath)
            for line in f: # per ogni riga di tutti i file (per n volte)
                # elaborare line
                k, p = line.split(';') # unpacking
                p = int(p)                
                d[k] = d.get(k, 0) + mappa_punti_valori.get(p, 0)              
            f.close()
    return d

# Complessità computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati

d = analizza_test('.')
print(d)

# In[Versione senza dizionario]

# in sostituzione della struttura dati dizionario viene utilizzata una lista
# contenente coppie identificativo,voto raccolte in liste di due elementi 

def analizza_test_dict_free( folder ):
    mappa_voto = [0, 0, 0, 0, 0, 0, 0.3, 0.4, 0.6, 1, 1.5]
    d = [] # lista di liste di due elementi, se [k, v] è in d, v è la valutazione
            # finale di k
    for filename in os.listdir(folder):
        fullpath = os.path.join(folder, filename)
        if os.path.isfile(fullpath) and filename.split('.')[-1] == 'csv':
            f = open(fullpath)
            print(filename)
            for line in f: # per n volte
                k, p = line.split(';')  # O(1)
                v = mappa_voto[int(p)]  # O(1)
                # cerca k in d
                trovato, i = False, 0   # O(1)
                while not trovato and i < len(d): # nel caso peggiore O(n)
                    if d[i][0] == k:
                        d[i][1] += v
                        trovato = True
                    i += 1
                if not trovato:
                    d.append([k, v])
    return d

d = analizza_test_dict_free('.')
print(d)


# Complessità computazionale è O(n**2)

# In[ORDINAMENTO - BubbleSort]

a = [10, 1, 23, 4, 80, 9, 11, 4]

a = [1, 4, 4, 9, 100, 11, 23, 80]

# In[]



n = len(a)

for j in range(n-1):
    i = 0
    while i < n-1-j:
        if a[i] > a[i+1]:
            # se la lista è ordinata non entro
            a[i], a[i+1] = a[i+1], a[i]
        i += 1

print(a, j)

# In[]

ordinata = False
j = 0

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
        
print(a, j)