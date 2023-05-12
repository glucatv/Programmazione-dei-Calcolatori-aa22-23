# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:48:31 2023

@author: gianluca
"""

# In[PANDAS]

import pandas as pd


df_c = pd.read_csv('2019fifa-wwc-c.csv')



# In[]

classifica = pd.DataFrame()

list_teams = list(df_c['Team1']) + list(df_c['Team2'])

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

# In[]

classifica = classifica.sort_values(by='Scores', ascending=False)

print(classifica)

# In[]

dict_score_diff = {}

for _, x in df_c.iterrows():
    score_diff = x['Score1'] - x['Score2']

    try:
        dict_score_diff[ x['Team1'] ] += score_diff
    except KeyError:
        dict_score_diff[ x['Team1'] ] = score_diff
        
    dict_score_diff[ x['Team2'] ] = dict_score_diff.get( x['Team2'], 0 ) -\
        score_diff

        
 # In[]

list_score_diff = []

for t in classifica['Team']:
    list_score_diff.append( dict_score_diff[t] )
    
classifica['Score diff'] = list_score_diff

# In[]

classifica = classifica.sort_values(by=['Scores', 'Score diff'], ascending=False)

# In[]

import pandas as pd

df_t = pd.read_excel('triathlon.xls')

df_t['trs'] = pd.to_timedelta(df_t['trs'])
df_t['trb'] = pd.to_timedelta(df_t['trb'])
df_t['trr'] = pd.to_timedelta(df_t['trr'])

df_t['time'] = df_t['trs'] + df_t['trb'] + df_t['trr']

df_t = df_t.sort_values(by='time', ascending=True)

print(df_t[ ['COGNOME', 'M/F', 'time']  ])

classifica_femminile = df_t[ df_t['M/F'] == 'F' ]

print(classifica_femminile[ ['COGNOME', 'M/F', 'time']  ])
