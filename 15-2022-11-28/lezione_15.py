# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:04:48 2022

@author: Gianluca
"""

# In[Soluzioni esercizi per casa]

import os

def browse_dir( d, ext=None ):
    '''
    Input: d è il nome di una cartella (un str), ext è una str che indica
        una estensione di file
    Output: ritorna la lista di tutti i file in d e in tutte le sue sottocartelle che
        terminanano in .ext. Se ext==None, stampa tutti i file
    '''
    
    b = []
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            if ext == None or x.split('.')[-1] == ext:
                b.append(full_path)
        elif os.path.isdir(full_path):
            c = browse_dir( full_path, ext=ext )
            b.extend(c)
            # equivalente a...
            #for x in c:
            #    b.append(x)
    return b
  
b = browse_dir( os.getcwd(), ext = 'py')
print(b)

# In[Leggere e scrivere su file]

# caso Windows
#a = 'C:\\Users\\Gianluca\\Dropbox\\teaching_and_work\\tv\\programmazione\\aa2022-23\\Programmazione-dei-Calcolatori-aa22-23\\15-2022-11-28\\lezioone_15.py'
# caso Linux/Unix
a = '/home/gianluca/Dropbox/teaching_and_work/tv/programmazione/aa2022-23/Programmazione-dei-Calcolatori-aa22-23/15-2022-11-28/lezione_15.py'

# personalizare a in base alle esigenze

f = open(a)

for line in f:
    print(line)
    
f.close()

# In[Ricerca di file in base al contenuto]

def browse_dir( d, txt ):
    b = []
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path) and full_path.split('.')[-1] == 'py':
            f = open(full_path)
            for line in f:
                if txt in line:
                    b.append(full_path)
                    break
            f.close()
        elif os.path.isdir(full_path):
            c = browse_dir( full_path, txt=txt )
            b.extend(c)
    return b
  
b = browse_dir( os.getcwd(), 'len' )
print(b)

# In[Scrittura e append su file]

f = open('prova_scrittura.txt', 'w')
f.write('prima riga\n')
f.write('seconda riga')
f.close()
f = open('prova_scrittura.txt', 'a')
f.write('\nprima riga\n')
f.write('seconda riga')
f.close()

