# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:48:31 2023

@author: gianluca
"""


# In[]

import pandas as pd

df_t = pd.read_excel('triathlon.xls')

df_t['trs'] = pd.to_timedelta(df_t['trs'])
df_t['trb'] = pd.to_timedelta(df_t['trb'])
df_t['trr'] = pd.to_timedelta(df_t['trr'])

df_t['time'] = df_t['trs'] + df_t['trb'] + df_t['trr']

df_t = df_t.sort_values(by='time', ascending=True)


# In[]

print(df_t[ ['COGNOME', 'M/F', 'time']  ])

# In[]

classifica_femminile = df_t[ df_t['M/F'] == 'F' ]

print(classifica_femminile[ ['COGNOME', 'M/F', 'time']  ])

# In[Classifica di categoria]

dict_pos_cat = {} # mappa categorie (es. MS2) in posizioni (prossima posizione da assegnare)

lista_pos_cat = []

for _, x in df_t.iterrows():
    k_cat = x['M/F']+x['CATEGORIA']
    lista_pos_cat.append( dict_pos_cat.get(k_cat, 1) )
    dict_pos_cat[k_cat] = dict_pos_cat.get(k_cat, 1) + 1
    
df_t['CLASSIFICA CAT.'] = lista_pos_cat

print(df_t[ ['COGNOME', 'M/F', 'CATEGORIA', 'CLASSIFICA CAT.']  ].iloc[:20])

# In[]
import pandas as pd


df_temp = pd.read_csv('us_temperatures_f.csv')


print(df_temp.isnull())

print(df_temp.isnull().any())

# In[]

df_temp = df_temp[df_temp.columns[1:]]

for c in df_temp.columns[1:]:
    df_temp[c] = (df_temp[c] - 32)*5/9
    
# In[ Temperatura media nel 2003 per ogni città]

# solo il 2003
df_temp2003 = df_temp[  (df_temp['Date'] > 20030000) & (df_temp['Date'] < 20040000) ]

for c in df_temp2003.columns[1:]:
    print(c, df_temp2003[c].min(), df_temp2003[c].mean(), df_temp2003[c].max())
    
# In[]

df_temp['Date'] = pd.to_datetime(df_temp['Date'], format='%Y%m%d')


df_temp2003 = df_temp[ df_temp['Date'].apply(lambda x: x.year == 2003) ]

# In[]

def report_year(y):
    global n

    try:    
        n += 1
    except NameError:
        n = 1
    df_y = df_temp[ df_temp['Date'].apply(lambda x: x.year == y) ]
    
    for c in df_y.columns[1:]:
        print(c, df_y[c].min(), df_y[c].mean(), df_y[c].max())
        
report_year(2003)
print('***********************')
report_year(2013)

