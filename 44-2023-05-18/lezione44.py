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

print(n)

# In[Settimana dell'anno mediamente più calda]

# dataframe df_temp_week: colonne le città e righe le settimane
# df_temp_week.loc[3, 'Boston'] temperatura media a Boston nella settimana 3 dell'anno

# 1. colonna con numero settimane

df_temp['Week'] = df_temp['Date'].apply(lambda x: x.week)

# 2 nuovo dataframe
df_temp_week = pd.DataFrame()

for city in cities:
    temps = []
    for w in range(1, 54):
        temps.append( df_temp[ df_temp['Week'] == w ][city].mean() )
    df_temp_week[city] = temps
    
# settimana dell'anno mediamente più calda

mean_tmps = []

for _, x in df_temp_week.iterrows():
    mean_tmps.append(x.mean())
    
df_temp_week['Mean'] = mean_tmps

# In[]

print(df_temp_week['Mean'].argmax(), df_temp_week['Mean'].max())

# In[]

d = {}

for c in cities:
    d[c] = [df_temp_week[c].max() - df_temp_week[c].min()]
    
df_d = pd.DataFrame(d)

df_d = df_d.transpose()

p = df_d[0].argmin()

print( df_d.index[p] )

# In[]

c = 'San Juan'

# trovare la giornata in c in cui si è registrato lo sbolzo di temperatura
# maggiore rispetto al giorno precedente

p = (df_temp[c].shift(1) - df_temp[c]).argmax()

print(df_temp['Date'].iloc[p], (df_temp[c].shift(1) - df_temp[c]).max() )

# In[]

import matplotlib.pyplot as plt

plt.plot(df_temp_week['Boston'], label='Boston')
plt.plot(df_temp_week['Miami'], label='Miami')
plt.xlabel('Settimane')
plt.ylabel('Gradi')
plt.title('Temperature medie settimanali')
plt.legend()

# In[]

plt.bar(['a', 'b', 'c'], [10, -9, 8] )

