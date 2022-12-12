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