def conta_somme_consecutive(a):
    c = 0
    for x, y, z in zip(a[:-2], a[1:-1], a[2:]):
        if z == x+y:
            c += 1
            
    return c

a = [5,3,8,6,14]
print( conta_somme_consecutive(a) )

# In[]

def my_min( a, b ):
    if a < b:
        return a
    else:
        return b
    
t = (8,0)

print(my_min( t[0], t[1] ))
print(my_min( *t ))

# In[la funzione zip e lo spacchettamento]

import matplotlib.pyplot as plt

c = {10: (42.29000000000006, 22.67),
 20: (178.31000000000012, 63.45000000000001),
 30: (418.61999999999966, 110.99999999999994),
 40: (753.9299999999997, 164.62999999999997),
 50: (1194.1700000000008, 221.74999999999997),
 60: (1727.4000000000003, 281.21000000000004),
 70: (2372.1299999999983, 344.2599999999999),
 80: (3114.8799999999997, 407.97),
 90: (3947.5199999999995, 474.6700000000002),
 100: (4879.860000000001, 541.7600000000001),
 110: (5913.650000000001, 610.6300000000001),
 120: (7043.649999999995, 680.5899999999999),
 130: (8262.549999999996, 751.28),
 140: (9630.200000000004, 824.8399999999999),
 150: (11057.300000000001, 899.9100000000008),
 160: (12620.250000000004, 975.2399999999999),
 170: (14225.670000000013, 1051.83),
 180: (15962.009999999991, 1128.7199999999996),
 190: (17803.690000000006, 1205.06)}

x = c.keys()

'''
Vogliamo creare due liste,  y0 e y1, contenenti rispettivamente i primi elementi delle
coppie di valori in c ed i secondi elementi.

La funzione zip prende in input sequenze di dimensione n e ritorna n sequenze tali che
la i-esima sequenza ritornata contiene gli elementi in posizione i delle sequenze in input.
Ad esempio, ce c è il dizionari definito sopra

list(zip( c[10], c[20], c[30],..., c[190] )) 

ritorna le liste y0 e y1 come richiesto.

L'operatore di spacchettamento * si applica a sequenze. Se t è una sequenza di lunghezza n,
*t sono gli n elementi della sequenza spacchettati dalla sequenza
(vedere l'esempio nella precedente cella ) quindi
                                       
zip(*c.values())

è equivalente a

zip( c[10], c[20], c[30],..., c[190] )
'''

y0, y1 = list(zip(*c.values()))

plt.plot(x,y0, c='r', label='bubble-sort')
plt.plot(x,y1, c='b', label='merge-sort')
plt.legend()
plt.xlabel('dimensione lista')
plt.ylabel('numero confronti')

# In[]

def my_min_2( a ):
    '''

    Parameters
    ----------
    a : lista di lunghezza n

    '''
    m = a[0]
    for x in a:
        if x < m:
            m = x
    return m

a = [1,2,3,2,1,2,3,4]
print(my_min_2(a))

# In[]

def contavocali( a ):
    '''
    Input: a, stringa di lunghezza n
    '''
    #b = a[:]
    c = 0
    for x in b:
        if x in 'aeiouAEIOU':
            c += 1
    return c

b = 'python'
print(contavocali(b))

# In[]

def my_min_3( a, i = 0 ):
    if i == len(a)-1:
        return a[i]
    m = my_min_3(a, i+1)
    return m if m < a[i] else a[i]

b = [4,1,3,7,9]
print(my_min_3(a))
        
