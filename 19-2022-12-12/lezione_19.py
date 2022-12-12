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

# In[esercizio 2-a]

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
                if k in d:
                    d[k].append(v)
                else:
                    d[k] = []         
            f.close()
    return d

# Complessità computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati

#d = analizza_test('/home/gianluca/Dropbox/teaching_and_work/tv/programmazione/aa2022-23/Programmazione-dei-Calcolatori-aa22-23/19-2022-12-12')
#d = analizza_test('19-2022-12-12')
d = analizza_test('.') # cartella corrente
print(d)

# In[Soluzione con metodo get]

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
                d[k] = a.append(v) # cosa c'è  che non va?
                
            f.close()
    return d

# Complessità computazionale
#
# n*O(1) = O(n) operazioni, ovvero O(1) per ogni riga dei file analizzati

d = analizza_test('.')
print(d)

