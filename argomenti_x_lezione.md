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


