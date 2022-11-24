# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:02:27 2022

@author: Gianluca
"""

def deep_count( a ):
    '''
    Input: una lista  o una tupla
    Output: il numero di 'int', 'float', 'str', 'bool' e 'None' in a ed in tutte
        le sue sottoliste o sottotuple annidate
    '''

    c = 0
    for x in a:
        if type(x) in (int, float, str, bool, type(None)):
            c += 1
        elif type(x) in (list, tuple):
            c += deep_count( x )
    return c

a = [ 2, [True, [1, 2.1], None], '94', (12, [None, ['tre', [4, ['1']], [False, [4,5]] ]] ), 0 ]
print(deep_count( a ))

# In[]

def deep_clone( a ):
    b = []
    for x in a:
        if type(x) == list:
            b.append(deep_clone(x))
        else:
            b.append(x)
    return b

a = [0, [1, 2], 3, [4, 5] ]
b = deep_clone(a)
print(b)

# In[]

import os

cartella = os.listdir()

for x in cartella:
    if os.path.isdir(x):
        print(f'DIR : {x}')
    elif os.path.isfile(x):
        print(f'FILE: {x}')
        
# In[]

def browse_dir( d ):
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            print(f'FILE: {full_path}')
        elif os.path.isdir(full_path):
            browse_dir( full_path )
            
browse_dir( os.getcwd() )

