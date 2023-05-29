# Argomenti per lezione

## Lezione 1 del 2022-10-10

Introduzione al corso. Metodo algoritmico. Esempi: Rompicapo di Guarini; Calcolo della radice quadrata.

[Video della lezione](https://www.dropbox.com/s/y4ex3zqymdx975o/Lezioni%202022-23-20221010_140146-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 2 del 2022-10-12

Dall'algoritmo al programma. Linguaggi di programmazione compilati ed interpretati. Introduzione al linguaggio Python. L'interprete e la console. Il primo programma Python e le sue componenti: commenti; variabili; assegnazioni; funzioni incorporate (`print`, `abs`); ciclo `while` e condizioni; blocchi ed *indentazioni*; tipi di dato (`int`, `float`, `str`, `bool`);

[Video della lezione](https://www.dropbox.com/s/yeeqv0tqewfzzjw/Lezione%202%20-%202022-10-12-20221012_140236-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 3 del 2022-10-17

Tipi di dato ed operatori: la funzione `type; `operatori tra tipi numerici (somma, differenza, moltiplicazione, divisione, divisione intera, modulo, potenza); operatori tra stringhe (concatenazione, ripetizione, appartenenza o `in`, indicizzazione, funzione `len`). Assegnamenti multipli. Diramazione del codice: le istruzioni `if`-`elif`-`else`. La funzione `input`. Le funzioni di conversione `float`, `int` e `str` *Esercizio per casa*: scrivere un programma che chieda in input una stringa e calcoli il numero di vocali che essa contiene.

[Video della lezione](https://www.dropbox.com/s/v8v3wjxu3jtxctc/Lezione%203%20-%202022-10-17-20221017_135822-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 4 del 2022-10-19

Operatori relazionali e logici; operatore di addizione (o sottrazione) e assegnazione (`+=`, `-=`). La dichiarazione `for` sulle stringhe. Immutabilità delle stringhe.

*Esercizio per casa*: scrivere un programma che chieda all'utente di inserire due stringhe `x`ed `y` e stampi la posizione di `x` a partire dalla quale compare `y`; nel caso in cui `y` non sia contenuto in `x`, stampi `-1`. Ad esempio, se

```python
x = 'programmazione'
y = 'gramma'
```

il programma deve stampare `3`.

[Video della lezione](https://www.dropbox.com/s/xagw6mgygwy7cjj/Lezione%204%20-%20Lezioni%202022-23-20221019_135859-Registrazione%20della%20riunione.mp4?dl=1 )

## Lezione 5 del 2022-10-24

Correzione dell'esercizio per casa, diverse versioni. L'istruzione `break`. L'operazione di *slicing* di una stringa.

*Esercizio per casa*. Risolvere l'esercizio proposto nella lezione precedente utilizzando lo slicing.

[Video della lezione](https://www.dropbox.com/s/lw9ukiatanhvfkl/Lezione%205%20-%20Lezioni%202022-23-20221024_140009-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 6 del 2022-10-26

Soluzione dell'esercizio per casa. Le funzioni in Python: funzioni incorporate (`print`, `input`, `len`, `str`, `int`,...); funzioni di libreria (*moduli*); funzioni definite dall'utente. Utilizzare i moduli: importare moduli o singole funzioni da un modulo. Cenni sui moduli `random` (funzione `random` e `randint`), `math` e `time`. Funzioni definite dall'utente: definizione di funzione; parametri formali; invocazione di funzione; parametri attuali; la dichiarazione `return`; ambienti di funzione. La funzione `range`.

*Esercizio per casa*. Scrivere una funzione che prende in input due stringhe e restituisce il carattere della prima stringa che compare più volte nella seconda. Ad esempio se la prima stringa è `ciao` e la seconda è `ramarro marrone`, la funzione deve restituire `a`.

[Video della lezione](https://www.dropbox.com/s/vonbo0gfir8uhl1/Lezione%206%20del%202022-10-26-20221026_135747-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 7 del 2022-10-31

Soluzione dell'esercizio per casa. Il tipo di dato `None`. Stringhe formattate. Caratteri speciali. Ambienti delle funzioni e visibilità delle variabili. Parametri delle funzioni con valori di default; i parametri della funzione `print`; argomenti per nome.

*Esercizio per casa*. Scrivere una funzione che riceva in input un intero `n` e restituisca un `float` (pseudo)-casuale compreso tra 0 ed 1 composto da `n` cifre decimali significative dopo la virgola. 

[Video della lezione](https://www.dropbox.com/s/ouebn0j64eqaohw/Lezione%207%20-%20Lezioni%202022-23-20221031_140033-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 8 del 2022-11-02

Soluzione dell'esercizio per casa. Funzioni: *docstring*; output multipli; numero variabile di argomenti (esercizio, stampa verticale); uso delle funzione per creare astrazione e rendere modulare il codice; insidie dell'astrazione.

#### Esercizi per casa

Dati `3` segmenti adiacenti ed `n` `float` si vuole calcolare quanti degli `n` `float` ricadono in ogni segmento. I segmenti sono  rappresentati da 2 `float` `h0` e `h1` che definiscono i segmenti: `(-`&infin;`, h0)`, `[h0, h1)`, `[h1, `&infin;`)`. Si progetti una funzione che prenda in input la descrizione di 3 segmenti (`h0` e `h1`) e un numero variabile di `float` e restituisca una terna di interi che rappresenta il numero di `float` che ricade in ciascuno dei 3 segmenti.

Ad esempio se l'input della funzione fosse `-7, 5, 3, 10, -4, 5, -12, 6, 0`, i segmenti sono: i numeri minori di `-7`; i numeri compresi tra `-7` e `5` (escluso); i numeri maggiori-uguali a `5`. I valori `-12` e `-4` fanno parte del primo segmento; `3` e `0` fanno parte del secondo segmento; `10`, `5` e `6` fanno parte del terzo segmento. Quindi la funzione dovrebbe restituire la terna: `1, 3, 3`

*Suggerimento* La funzione abbia la seguente intestazione

```python
def hist(h0, h1, *numbers)
```

dove `numbers` rappresenta il numero variabile di `float`

[Video della lezione](https://www.dropbox.com/s/wu2xw027v48nan0/Lezione%208%20-Lezioni%202022-23-20221102_135913-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 9 del 2022-11-07

Soluzione dell'esercizio per casa. Le *tuple*: definizione, indicizzazione, slicing, packing, unpacking, immutabilità. Funzioni come input di altre funzioni. Funzioni `lambda`. Espressioni condizionali. Cenni sui metodi.

##### Esercizi per casa

1. Si progetti una funzione denominata `init_tuple` che prenda in input un intero positivo `n` e, opzionalmente, una funzione `v`. La funzione restituisca una tupla di lunghezza `n` che in posizione `i` contenga `v(i)`. Qualora il parametro `v` non fosse specificato, la funzione restituirebbe una tupla composta da `n` zeri.

	*Suggerimento*. Potrebbe essere utile partire da una tupla vuota - si indica così `()` - e poi procedere per concatenazioni successive. A tal proposito si provi ad usare l'operatore `+` come si fa con le stringhe. Una tupla composta da un unico elemento `e` si definisce in questo modo `(e, )`.  

2. Utilizzare la funzione `init_tuple` per creare una tupla contenente i primi 10 numeri dispari
3. Utilizzare la funzione `init_tuple` per creare una tupla contenente 10 stringhe non vuote di lunghezza crescente
4. Utilizzare la funzione `init_tuple` per creare una tupla contenente 10 tuple tali che la tupla in posizione `i` sia lunga 10 e contenga `i` in ogni posizione. *Suggerimento*: come per le stringhe, `*` sulle tuple è l'operatore di ripetizione.

[Video della lezione](https://www.dropbox.com/s/rxb6ylvn2ez003l/Lezione%209%20-%20Lezioni%202022-23-20221107_140018-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 10 del 2022-11-09

Soluzione dell'esercizio per casa e stima del numero di operazioni eseguite dalla funzione. Le operazioni di concatenazione e ripetizione su tuple. Numero di operazioni eseguite da una funzione e sua relazione con il tempo di calcolo. Le liste: creazione, indicizzazione, slicing, concatenazione, ripetizione, funzione `len`, cancellazione, il metodo `append`. Numero di operazioni elementari richieste dalle precedenti funzionalità.

#### Esercizi per casa

1. Si progetti una funzione analoga a `init_tuple` per le liste.
2. Si progetti una funzione, denominata `rem_none` che prenda in input una lista ed elimini da questa tutti gli elementi a valore `None`.

[Video della lezione](https://www.dropbox.com/s/uei7a28hxykl1sx/Lezione%2010%20del%202022-11-09-20221109_135950-Registrazione%20della%20riunione.mp4?dl=1)


## Lezione 11 del 2022-11-14

Soluzione degli esercizi per casa: ottimizzazione del numero di operazioni eseguito. L'operatore `in` su tuple e liste. Le funzioni `min`, `max`, `sum`. *Aliasing* e *clonazione*.

[Video della lezione](https://www.dropbox.com/s/qfva5jttwwtfnxq/Lezione%2011%20-%20Lezioni%202022-23-20221114_140056-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 12 del 2022-11-16

Prima prova intermedia

## Lezione 13 del 2022-11-21

Soluzioni e commenti sulla prova intermedia. Funzioni ricorsive: convergenza; memoria utilizzata.

#### Esercizio per casa

Si progetti una funzione, denominata `count_int` che prenda in input una lista che può contenere liste annidate e restituisca il numero di interi nella lista e in tutte le sottoliste annidate che questa contiene. Ad esempio `count_int( [3, [9, [2,5], 2], 10, [8, [4,3], [1,2], 3]] )` dovrebbe restituire 12.

[Video della lezione](https://www.dropbox.com/s/715fkpe32kiyllj/Lezione%2013%20-%20Lezioni%202022-23-20221121_140127-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 14 del 2022-11-23

Soluzione dell'esercizio per casa con arricchimenti. Esercizio svolo in classe: implementazione di una funzione ricorsiva per la *clonazione profonda* di liste. Il modulo `os` e le funzioni `os.listdir()`, `os.getcwd()`, `os.path.isfile()`, `os.path.isdir()`, `os.path.join()`. Esempio: `browse_dir()`, una funzione che prende in input il nome di una cartella (un `str`) e stampa i nomi di tutti i file nella cartella ed in tutte le sue sottocartelle.

#### Esercizi per casa

1. Modificare `browse_dir` nel seguente modo:  aggiungere un secondo parametro `ext` opzionale di tipo `str` che, se specificato, stampi solo i file che hanno per estensione `ext`. Se non indicato, la funzione si comporti nel modo originale.

2. Modificare la precedente funzione in modo tale che, invece di stampare i nomi dei file, li ritorni in una lista.

[Video della lezione](https://www.dropbox.com/s/qtgro34ga4twvu4/Lezione%2014%20-%20Lezioni%202022-23-20221123_140139-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 15 del 2022-11-28

Soluzione degli esercizi per casa, il metodo `extend` delle liste. File di testo: lettura, scrittura (creazione) e *append*; la funzione `open`; i metodi `write` e `close`; iterare su file.

#### Esercizio per casa

Implementare la funzione che soddisfi la seguente specifica:

```python
def hist( a, bins ):
    '''
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in a < bins[0]
        - h[n-1] = numero di elementi in a >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    '''
```

[Video della lezione](https://www.dropbox.com/s/o5yxre6rdcknpug/Lezione%2015%20-%20Lezioni%202022-23-20221128_140208-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 16 del 2022-11-30

Soluzione dell'esercizio per casa. Il costo computazionale delle funzioni (o algoritmi), contare il numero di operazioni elementari per stimare il tempo di calcolo; il costo nel caso peggiore; analisi del costo della funzione data per casa. Algoritmo di ricerca binaria: descrizione e costo computazionale (`O(log n)`).

#### Esercizio per casa

Si progetti una funzione che rispetti la specifica

```python
def find_in_file( filename, k):
	'''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le righe del file in cui compare k  
	'''
```
Sia `n` il numero di righe nel file, calcolare il costo computazionale della funzione nei seguenti casi:

1. la lunghezza di ogni riga e la stringa `k` abbiano lunghezza costante;
2. lunghezza di ogni riga sia al più `m` e la stringa `k` abbia lunghezza costante;

Modificare la funzione in modo che la nuova specifica sia

```python
def find_in_file( filename, k):
	'''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla ( (r0, c0), (r1, c1), ...) di coppie di interi che indicano le
		righe e le colonne del file in cui compare k. Per colonna si intende la posizione
		all'interno della riga  
	'''
```

[Video della lezione](https://www.dropbox.com/s/ynnsdt0d1yxuems/Lezione%2016%20del%202022-11-30-20221130_135916-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 17 del 2022-12-05

Soluzione degli esercizi per casa. La funzione `tuple`. Implementazione dell'algoritmo di ricerca binaria.

#### Esercizio per casa

Completare il *debug* della funzione `bin_search` e correggere gli eventuali errori.	

[Video della lezione](https://www.dropbox.com/s/0cga07v5p8zozbm/Lezione%2017%20Lezioni%202022-23-20221205_140036-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 18 del 2022-12-07

Soluzione dell'esercizio per casa (prova di debugging). La funzione `list` e la *comprensione di lista*. La struttura dati **dizionario**: definizione; lettura; aggiornamento o inserimento; cancellazione; la funzione `len`; i metodi `keys` e `values`.

#### Esercizi per casa

1. (*Riscaldamento*) Si scriva una funzione che prenda in input una lista di stringhe `a` e restituisca un dizionario che abbia per chiavi le iniziali delle stringhe in `a` e ad ogni chiave `k` associ come valore la lista di stringhe in `a` che cominciano con `k`.
2. Il docente ha raccolto in una cartella del pc dei file di testo con i risultati delle prove intermedie dell'esame di programmazione. Ogni file contiene l'esito di una prova e riporta su ogni riga l'email dello studente ed il punteggio ottenuto (un intero tra 0 e 10). Il docente deve scrivere un programma Python per raccolga tutti i risultati, in particolare vuole ottenere un dizionario che associ agli indirizzi email degli studenti (le chiavi) la lista dei punteggi riportati nelle prove a cui ha partecipato. Si progetti una funzione denominata `analizza_test` che prenda in input il nome della cartella contenente i file di testo e restituisca il dizionario così come descritto sopra. Si assuma che i file contenenti i risultati abbiano estensione `csv`, contengano una riga per ogni partecipante all'esame e le righe abbiano il formato:

		email_studente;voto
		
	*Esempio*: L'esecuzione di `analizza_test( '18-2022-12-07' )` deve produrre il seguente dizionario 
	
	```
	{'ironman@avengers.mv': [5],
 	'captain.america@avengers.mv': [7, 6],
 	'hulk@avengers.mv': [6],
 	'spiderman@avengers.mv': [9, 9],
 	'superman@justiceleague.dc': [4, 6],
 	'wonder.woman@justiceleague.dc': [10],
 	'aquaman@justiceleague.dc': [8, 8],
 	'thor@avengers.mv': [4],
 	'batman@justiceleague.dc': [5],
 	'green.lantern@justiceleague.dc': [7]}
 	```
3. Modificare la precedente funzione in modo che il dizionario associ indirizzi email al voto finale derivante da tutte le prove a cui hanno partecipato gli studenti. Per il voto finale ogni prova intermedia contribuisce nel seguente modo: da 0 a 5 punti il contributo è 0, con 6 il contributo è 0.3, con 7 il contributo è 0.4, con 8 il contributo è 0.6, con 9 punti il contributo è 1 e con 10 punti il contributo è 1.5.

	*Esempio*: L'esecuzione della nuova versione di  `analizza_test( '18-2022-12-07' )` deve produrre il seguente dizionario:
	
	```
	{'ironman@avengers.mv': 0,
	'captain.america@avengers.mv': 0.7,
	'hulk@avengers.mv': 0.3,
	'spiderman@avengers.mv': 2,
	'superman@justiceleague.dc': 0.3,
	'wonder.woman@justiceleague.dc': 1.5,
	'aquaman@justiceleague.dc': 1.2,
	'thor@avengers.mv': 0,
	'batman@justiceleague.dc': 0,
	'green.lantern@justiceleague.dc': 0.4}  
	```

[Video della lezione](https://www.dropbox.com/s/zyi1l4tsyahj2bl/Lezione%2018%20-%20Riunione%20in%20_Lezioni%202022-23_-20221207_140219-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 19 del 2022-12-12

Soluzione parziale degli esercizi per casa. Il metodo `get` dei dizionari. Soluzione della prima parte del secondo esercizio per casa utilizzando il metodo `get`... *da completare*.

#### Esercizi per casa

1. Debugging e correzione dell'esercizio da completare
2. Risolvere la seconda parte dell'esercizio 2

[Video della lezione](https://www.dropbox.com/s/p6zbgii1e76oye7/Lezione%2019%20-%20Riunione%20in%20_Lezioni%202022-23_-20221212_140312-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 20 del 2022-12-14

Soluzione degli esercizi per casa e cosa cambia, in termini di costo, se i problemi vengono risolti utilizzando una lista invece del dizionario. Il problema dell'ordinamento; l'algoritmo **Bubble Sort**, descrizione ed implementazione.

#### Esercizi per casa

1. Trasformare il codice dell'algoritmo Bubble Sort in una funzione denominata `bubble_sort`che prenda in input una lista di numeri e la muti ordinandoli in modo crescente.
2. Sia `n` la lunghezza della lista in input, calcolare la complessità computazione della funzione `bubble_sort` distinguendo il caso peggiore ed il caso migliore.
3. Modificare la funzione `bubble_sort` in modo da soddisfare la seguente specifica

	```python
	def bubble_sort(a, inplace=True):
	'''
	Input:  a, una lista di str; inplace un bool
	Output: ordina le stringhe in a dalla più corta alla più lunga, ritorna la lista ordinata.
		Se inplace è True la funzione muta a, altrimenti viene restituita una nuova lista
		con le stringhe di a ordinate come richiesto
	'''
	```
	
[Video della lezione](https://www.dropbox.com/s/qzqjjd30t4vk7nx/Lezione%2020%20del%202022-12-14-20221214_140111-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 21 del 2022-12-19

Soluzione degli esercizi per casa. Impostare il criterio per l'ordinamento sulla funzione `bubble_sort` con apposito parametro (*key*). Ordinamento multi-criterio realizzato con il **confronto tra tuple* da una opportuna funzione da passare come parametro `key`. Il metodo `sort` delle liste e la funzione `sorted`.

#### Esercizio per casa

Si progetti ed implementi una funzione che prenda in input due liste di numeri ordinati in modo crescente e restituisca una nuova lista contenente tutti gli elementi delle liste in input ordinati dal più piccolo al più grande.

[Video della lezione](https://www.dropbox.com/s/qtq68v0awwh1ar6/Lezione%2021%20del%202022-12-19-20221219_140033-Registrazione%20della%20riunione.mp4?dl=1)


## Lezione 22 del 2022-12-21

Soluzione dell'esercizio per casa, algoritmo di *merge*. Utilizzo dell'algoritmo di merge per definire l'algoritmo di *ordinamento per fusione* (**merge sort**): descrizione, complessità computazionale (`O(n log n)`), implementazione.

#### Esercizi per casa

1. Modificare le funzioni `bubble_sort` e `merge_sort` in modo che ritornino il numero di confronti eseguiti; scrivere una funzione per testare quanti confronti eseguono i due algoritmi su istanze di lunghezza diversa. La funzione deve eseguire i test su liste generate 'casualmente' di lunghezze diverse e, per ogni test eseguito, deve salvare su una riga di un file csv: la lunghezza della lista usata per il test; numero di confronti eseguiti da `bubble_sort`; numero di confronti eseguiti da `merge_sort`.

2. Modificare la funzione `merge_sort` rendendo i parametri `lx` e `rx` opzionali. Se non indicati, la funzione deve ordinare tutta la lista.

3. Modificare la funzione dell'Esercizio 1 in modo la questa ritorni un dizionario `C` che mappi interi a coppie di `float` con la seguente semantica: `C[n] = (b, m)` se su liste lunghe `n` il numero di confronti medi di `bubble_sort` è stato `b` e quello di `merge_sort` è stato `m`.

[Video della lezione](https://www.dropbox.com/s/hpb5qb9e8yt7fdm/Lezione%2022%20del%202022-12-21-20221221_140124-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 23 del 2023-01-09

Soluzione degli esercizi per casa. Introduzione al modulo `matplotlib`, la funzione `plot`. La gestione delle eccezioni con `try...except`. La funzione `zip`.

#### Esercizi per casa

1. Sperimentare la funzione `zip` con sequenze in input di lunghezza diversa.
2. Si abbiano `n` tuple di dimensione 2 denominate `t1`, `t2`, ..., `tn` cosa restituisce `zip(t1,t2,...,tn)`?
3. Scrivere una funzione che prenda in input una lista di interi `a` e restituisca il numero di volte in cui la somma di due elementi consecutivi è uguale all'elemento che li segue. Ad esempio se `a = [5,3,8,6,14]` la funzione dovrebbe restituire `2`.

[Video della lezione](https://www.dropbox.com/s/he8tgspgq7xhnah/Lezione%2023%20-%20Riunione%20in%20_Generale_-20230109_140126-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 24 del 2023-01-11

Soluzione degli esercizi per casa. L'operatore di spacchettamento `*` ed utilizzo con la funzione `zip` per estrarre le sequenze di tutti gli elementi in una data posizione in un elenco di sequenze. Il costo computazione in termini di *memoria utilizzata*: valutazione al netto della memoria utilizzate per l'input e l'output; memoria utilizzata dalle funzioni ricorsive.

[Video della lezione](https://www.dropbox.com/s/h93qzi5g0yhgd36/Lezione%2024%20del%202023-01-11-20230111_140037-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 25 del 2023-03-09

Seconda prova intermedia

## Lezione 26 del 2023-03-15

Soluzioni e commenti sulla prova intermedia. Introduzione al linguaggio C: il processo di compilazione; la funzione main; dichiarazione di variabili e tipi; la funzione `printf` della libreria standard `stdio`.

[Video della Lezione](https://www.dropbox.com/s/8snrbkvpkmhw892/Lezione%2026%20del%202023-03-15-20230315_133125-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 27 del 2023-03-16

Linguaggio C: operatori logici e relazionali; cicli `while` e `for`; le istruzioni `if`...`else`; output formattato con `printf`; la libreria `math` e la funzione `fabs`; definizione di funzioni; il tipo di dato `char`.

#### Esercizio per casa

Scrivere una funzione C denominata `switch_case` che prende in input un `char` `c`: se `c` è una lettera maiuscola ritorni il corrispondente minuscolo; se `c` è una lettera minuscola ritorni il corrispondente maiuscolo; nel caso `c` non sia una lettera, la funzione ritorni `-1`. 

[Video della lezione](https://www.dropbox.com/s/davmzie8hv233ei/Lezione%2027%20del%202023-03-16-20230316_113043-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 28 del 2023-03-22

Soluzione dell'esercizio per casa. Prototipo delle funzioni. Il processo di compilazione e l'inclusione dei file `.h`. La struttura dati *array*: definizioni e proprietà; array come parametri di funzione; funzioni che modificano array; la funzione `sizeof()`.

[Video della lezione](https://www.dropbox.com/s/mvjoguk6ojuzrsp/Lezione%2028%20del%202023-03-22-20230322_133121-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 29 del 2023-03-23

Il tipo di dato puntatore. Allocare memoria in *run-time* con la funzione di libreria `malloc`. La funzione `free`. Aritmetica dei puntatori. Come clonare un array. Introduzione alla creazione di array dinamici.


[Video della lezione](https://www.dropbox.com/s/uogt1odr6q7h1qn/Lezione%2029%20del%202023-03-23-20230323_110108-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 30 del 2023-03-26

Le stringhe come array di `char`. Esempi: calcolare la lunghezza di due stringhe e creare una nuova stringa formata dalla concatenazione di due altre stringhe. Creare nuovi tipi di dato con le `struct` e `typedef`. Prima versione di array dinamico che supporta l'operazione di append.

[Video della lezione](https://www.dropbox.com/s/o5he4fl9pgghsjq/Lezione%2030%20del%202023-03-29-20230329_133011-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 31 del 2023-03-30

Array dinamici con costo di append costante (costo ammortizzato). L'operazione di inserimento. L'operazione di pop (eliminazione dell'elemento dal fondo), introduzione.

[Video della lezione](https://www.dropbox.com/s/t0vya9yqdhn1c3a/Lezione%2031%20del%202023-03-30-20230330_110025-Registrazione%20della%20riunione.mp4?dl=1)


**Esercizio per casa**: Si scriva una funzione `C`, avente il seguente prototipo:

```c
array_int trova_spazi(char *a);
```

La funzione riceve in input una stringa e restituisce un `array_int` contenente le posizioni degli spazi in `a`.

## Lezione 32 del 2023-04-05

Soluzione dell'esercizio per casa. L'operazione `pop` su array a dimensione variabile. La funzione `realloc`. La libreria `string` e le funzioni `strlen` e `strcpy`. Implementazione di liste (array) con elementi  di tipo disomogeneo: utilizzo del puntatore a `void`; casting; l'operarore `*`;

[Video della lezione](https://www.dropbox.com/s/hc8y7zfpws60t0l/Lezione%2032%20del%202023-04-05-20230405_133021-Registrazione%20della%20riunione.mp4?dl=1)

**Esercizi per casa**

1. Implementare la funzione `append` su `array_int` utilizzando la funzione `realloc`
2. Implementare la funzione avente il seguente prototipo:
	
	```c
	array_int delete(array_int a, int i);
	```
	
	che elimina da `a` l'elemento in posizione `i`. Ritorna l'`array_int` modificato. Discutere la complessità temporale e spaziale della funzione implementata.
3. Implementare la funzione avente il seguente prototipo:
	```c
	int str_cmp(char *a, char *b);
	```	
	La funzione ritorna `0` se le due stringhe sono uguali; ritorna -1 se `a` precede `b` lessicograficamente e `+1` altrimenti.
	
## Lezione 33 del 2023-04-12

Ancora sugli array con elementi di tipo disomogeneo: finalizzazione dell'implementazione. Liste concatenate: definizioni, inserimento di un elemento in testa alla lista.

[Video della lezione](https://www.dropbox.com/s/t68frj1mbvj8xsk/Lezione%2033%20del%202023-04-12-20230412_133052-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 34 del 2023-04-13

Liste concatenate: ricerca; inserimento; cancellazione. Liste concatenate di stringhe. Argomenti alla linea di comando.

[Video della lezione](https://www.dropbox.com/s/5q9xr0rdxd0wusb/Lezione%2034%20del%202022-04-13-20230413_110610-Registrazione%20della%20riunione.mp4?dl=1)

**Esercizi per casa**

1. Scrivere un programma che crei una lista concatenata di stringhe utilizzando quelle passate dalla linea di comando. Le posizioni delle stringhe nella lista deve rispettare quelle nella linea di comando.
2. Si scriva una funzione avente il seguente prototipo:

	```c
	linked_list move_to_tail(linked_list L);
	```
	
che sposta in coda il primo nodo della lista; restituisce la lista modificata.

## Lezione 35 del 2023-04-19

Argomenti di funzione per riferimento: l'operarore `&`. Le funzioni `scanf` e `sscanf`.

[Video della lezione](https://www.dropbox.com/s/2vq6yx9dfnz5ul0/Lezione%2035%20del%202023-04-19-20230419_133217-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 36 del 2023-04-20

Implementazioni dei dizionari in `C` con liste di trabocco: funzioni di ricerca ed update.

[Video della lezione](https://www.dropbox.com/s/pnnf82aghpji35n/Lezione%2036%20del%202023-04-20-20230420_110056-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 37 del 2023-04-26

Dizionari in `C`: funzioni `hash`; cancellazione; ridimensionamento dell'array delle liste di trabocco per mantenere costante la lunghezza delle liste. Implementazione di array multidimensionali.

[Video della lezione](https://www.dropbox.com/s/xbheda7t0gaor2n/Lezione%2037%20del%202023-04-26.mp4?dl=1)

## Lezione 38 del 2023-04-27

Matrici con array lineare: funzioni di conversione indice-coordinate e viceversa. Matrici con array di array.

[Video della lezione](https://www.dropbox.com/s/yok6o1gys2tzjsy/Lezione%2038%20del%202023-04-27.mp4?dl=1)

## Lezione 39 del 2023-05-03

Terza prova intermedia

## Lezione 40 del 2023-05-04

Correzione e commenti sulla terza prova intermedia. Le `union` in `C`.

[Video della lezione](https://www.dropbox.com/s/qbienic5g1bbbu1/Lezione%2040%20del%202023-05-04.mkv?dl=1)

## Lezione 41 del 2023-05-10

La libreria **pandas**: `DataFrame`; operazione su colonne; filtri sulle righe; re-indicizzazione; *slicing* con `loc` e `iloc`; iterazione su righe; ordinamento.

**Esercizio**. Si modifichi il DataFrame `classifica` creato a lezione aggiungendo una colonna contenente la differenza reti di ogni squadra.

[Video della lezione](https://www.dropbox.com/s/p92rawacdhv1ozv/Lezione%2041%20del%202023-05-10-20230510_133309-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 42 del 2023-05-11

La libreria *panda*: ordinamento su più criteri; gestione di colonne con tempi (la funzione `to_timedelta`); esempi.

[Video della lezione](https://www.dropbox.com/s/8s7nkbbbvixjegg/Lezione%2042%20del%202023-05-11-20230511_110250-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 43 del 2023-05-17

Esercizi con `pandas`; serie temporali; `pandas`, funzione `to_datetime` e metodo `apply`. Variagili globali e dichiarazione `global`. 

[Video della lezione](https://www.dropbox.com/s/yed39b1da8stxw6/Lezione%2043%20del%202023-05-17-20230517_133053-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 44 del 2023-05-18

La libreria `pandas`:  metodi `argmax`, `argmin`, `transpose`, `shift`; rappresentazione grafica dei dati in un dataframe con la libreria `matplotlib`. **Esercizio**: Utilizzando il dataset `us_temperatures.csv` rappresentare con un diagramma a barre la temperatura media delle città del dataset.

[Video della lezione](https://www.dropbox.com/s/w9in7h1ir7kaho8/Lezione%2044%20del%202023-05-18-20230518_110017-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 45 del 2023-05-24

Esercitazioni con `Pandas`, `matplotlib`. La funzione `barh`. Esportazione da `matplotlib` in formato grafico.

[Video della lezione](https://www.dropbox.com/s/4cbamj3f3pwg8ig/Lezione%2045%20del%202023-05-24-20230524_103116-Registrazione%20della%20riunione.mp4?dl=1)

## Lezione 46 del 2023-05-25

Esercitazione con il `C` su puntatori ed array.

[Video della lezione](https://www.dropbox.com/s/14gbahi9r8sbwpy/Lezione%2046%20del%202023-05-25-20230525_103055-Registrazione%20della%20riunione.mp4?dl=1)


