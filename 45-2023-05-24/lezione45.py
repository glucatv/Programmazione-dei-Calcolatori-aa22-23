# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:48:31 2023

@author: gianluca
"""


# In[]
import pandas as pd


df_temp = pd.read_csv('us_temperatures_f.csv')

df_temp = df_temp[df_temp.columns[1:]]

for c in df_temp.columns[1:]:
    df_temp[c] = (df_temp[c] - 32)*5/9
    

cities = df_temp.columns[1:]
    
    
# In[]

df_temp['Date'] = pd.to_datetime(df_temp['Date'], format='%Y%m%d')


df_temp2003 = df_temp[ df_temp['Date'].apply(lambda x: x.year == 2003) ]

# In[]


import matplotlib.pyplot as plt

# In[]

'''
plt.plot(df_temp_week['Boston'], label='Boston')
plt.plot(df_temp_week['Miami'], label='Miami')
plt.xlabel('Settimane')
plt.ylabel('Gradi')
plt.title('Temperature medie settimanali')
plt.legend()
'''
# In[]

def plot_avg_month( m ):    
    lista_mesi = ['', 'Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set',\
                  'Ott', 'Nov', 'Dic']
    
    df_m = df_temp[ df_temp['Date'].apply(lambda x: x.month == m) ]
    
    temps = []
    
    for c in cities:
        temps.append( df_m[c].mean() )
    
    plt.barh(cities, temps)
    
    plt.title('Temperature medie nel mese di '+lista_mesi[m])
    plt.xlabel('C')
    plt.savefig(lista_mesi[m]+'.png', format='png', dpi=200, pad_inches=120)
    
plot_avg_month( 10 )

# In[]

def argmax(a):
    p = 0
    n = len(a)
    for i in range(1, n):
        if a[i] > a[p]:
            p = i
    return p

def jefferson( voti, n_seggi ):
    '''
    input: voti, lista ordinata in modo decrescente di interi. voti[j] rappresenta
        il numero di voti ottenuti dal partito j
    n_seggi: intero positivo
    
    output: lista seggi di interi tale che seggi[j] rappresenta il numero di
        seggi preso dal partito j
    '''
    
    n = len(voti) # numero di partiti
    
    seggi = [0]*n
    
    for s in range(n_seggi):
        # defininiamo il partito che prende il seggio s+1
        p = argmax( [voti[i]/(1+seggi[i]) for i in range(n)] ) # O(n)
        seggi[p] += 1 # O(1)

    return seggi


    '''
    Complessità temporale
        O(n*n_seggi)
    '''


voti = [100000, 80000, 30000, 20000]
n_seggi = 8
print(jefferson(voti, n_seggi))
    
# In[]

def jefferson( voti, n_seggi ):
    '''
    input: voti, lista ordinata in modo decrescente di interi. voti[j] rappresenta
        il numero di voti ottenuti dal partito j
    n_seggi: intero positivo
    
    output: lista seggi di interi tale che seggi[j] rappresenta il numero di
        seggi preso dal partito j
    '''
    n = len(voti)
    
    seggi = [0]*n
    quot = []
    
    for d in range(n_seggi):
        for p in range(n):
            quot.append( (voti[p]/(1+d), p)  )  # O(n*n_seggi)
                
    quot.sort(reverse=True) # O(n*n_seggi log (n*n_seggi) )
    
    for _, p in quot[:n_seggi]:
        seggi[p] += 1

    return seggi


voti = [100000, 80000, 30000, 20000]
n_seggi = 8
print(jefferson(voti, n_seggi))