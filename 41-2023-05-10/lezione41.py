# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:48:31 2023

@author: gianluca
"""

# In[PANDAS]

import pandas as pd

df = pd.DataFrame()

df['ColA'] = [8, 2, 1, 9]
df['ColB'] = [12, 21, 10, 9.8]

print(df.shape)

num_righe = df.shape[0]
num_colonne = df.shape[1]

print(df.describe())

print( df['ColA'].min() )
print( df['ColB'].max() )
print( df['ColB'].mean() )

df['ColC'] = [0, 2.71, '3.14', 'stringa']

# In[]

df['ColD'] = 2*df['ColA']
df['ColE'] = df['ColA'] + df['ColB']

# In[]

print(df[ [True, False, False, True] ])

# In[]

print(df['ColA'] > 5)

df_f = df[ df['ColA'] > 5  ]

print(df_f)

# In[]

print(df.columns)

df.columns = ['A', 'B', 'C', 'D', 'E']

print(df.columns)

# In[]

print(df_f.index)

# reindicizzazione
df_f.index = range(df_f.shape[0])

print(df_f)

# In[]

print(df.iloc[0:2, 1:3])
print(df.iloc[:,1:3])

print(df.loc[0:2, 'B':'D'])
print(df.loc[:,'B':'D'])

# In[]

df_c = pd.read_csv('2019fifa-wwc-c.csv')

df_c['Score_diff'] = df_c['Score1'] - df_c['Score2']

team = 'Italy'

df_t = df_c[ (df_c['Team1'] == team) | (df_c['Team2'] == team) ]

punti_t = 0
for _, x in df_t.iterrows():
    if x['Team1'] == team:
        if x['Score1'] > x['Score2']:
            punti_t += 3
    if x['Team2'] == team:
        if x['Score2'] > x['Score1']:
            punti_t += 3
    if x['Score2'] == x['Score1']:
        punti_t += 1

print(punti_t)

# In[]

classifica = pd.DataFrame()

list_teams = list(df_c['Team1']) + list(df_c['Team2'])


# In[creazione della lista delle squadre, senza ripetizioni]
l = []

for t in list_teams: # per n volte
    if t not in l: # O(len(l))
        l.append(t)
        
# operazione di costo O(n**2), non mi piace

# In[soluzione più efficiente]

dict_teams = {}

for t in list_teams: # per n volte
    if t not in dict_teams: # O(1)
        dict_teams[t] = None
        
# costo O(n) in media

classifica['Team'] = dict_teams.keys()

# In[]

scores = []

for team in classifica['Team']:
    df_t = df_c[ (df_c['Team1'] == team) | (df_c['Team2'] == team) ]

    punti_t = 0
    for _, x in df_t.iterrows():
        if x['Team1'] == team:
            if x['Score1'] > x['Score2']:
                punti_t += 3
        if x['Team2'] == team:
            if x['Score2'] > x['Score1']:
                punti_t += 3
        if x['Score2'] == x['Score1']:
            punti_t += 1

    scores.append(punti_t)
    
classifica['Scores'] = scores

classifica = classifica.sort_values(by='Scores', ascending=False)

print(classifica)