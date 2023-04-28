#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* chiave: stringa; valore: float */
struct dict_item {
	char *k;
	float v;
};
typedef struct dict_item dict_item;

struct node {
	dict_item info;
	struct node *next;
};
typedef struct node node;

struct linked_list {
	node *a; /* punta al primo elemento della sequenza*/
	int n;
};
typedef struct linked_list linked_list;

struct dict {
	node **a;
	int n;
	int M;
};
typedef struct dict dict;

dict dict_init(int);
int h(dict, char*);
dict dict_set(dict, dict_item);
node *dict_search(dict, char*);
void print_dict(dict);
int dict_del(dict, char*);
dict dict_resize(dict, int);

void print_llist(node*);
node *in0(node*, dict_item);
linked_list init(void);
node *search(linked_list, int);
linked_list insert(linked_list, int, char*);
linked_list delete(linked_list, int);
linked_list del0(linked_list);
linked_list move_to_tail(linked_list L);


void main(int dim, char *args[]){
	dict d = dict_init(3);
	int i;
	dict_item e;
	
	for(i = 1; i < dim; i++){
		e.k = args[i];
		e.v = i;
		d = dict_set(d, e);
	}

	print_dict(d);	
}


/* 
 * Funzione hash
 * ritorna un indice del dizionario
 * 
 * */

int h(dict d, char *k){
	/*  
	 * Operatori bit-a-bit
	 * 
	 * ^ XOR
	 * & AND
	 * | OR
	 *
	 */
	
	int i = 0, hash_val = 0;
	
	while( k[i] != '\0') {
		hash_val = hash_val ^ k[i];
		i += 1;
	}
	
	return hash_val % d.M;
}

/* imposta un volore per una chiave del dizioario usando e */
dict dict_set(dict d, dict_item e){
	int p = h(d, e.k);
	node *nd;
	
	nd = dict_search(d, e.k);
	if( nd != NULL ) {
		nd->info.v = e.v;
	} else {
		d.a[p] = in0(d.a[p], e);
		d.n++;
	}
	
	if (d.n/d.M > 4){
		/*
		 * ridimensiona d.a
		 * */
		 d = dict_resize(d, d.M*2+1);
	}
	
	return d;
}

/* ritorna il puntate al node contenente l'item del dizionario con
 * chiave k. NULL se tale chiave non è presente nel dizionario */
node *dict_search(dict d, char *k){
	int p = h(d, k);
	node *q = d.a[p];
	
	while( q != NULL && strcmp(k, q->info.k) != 0){
		q = q->next;
	}
	
	return q;
}

/* Inizializza un dizionario vuoto con M liste*/
dict dict_init(int M){
	dict d;
	int i;
	d.a = malloc(sizeof(node*)*M);
	d.n = 0;
	d.M = M;
	for(i = 0; i < d.M; i++){
		d.a[i] = NULL;
	}
	return d;
}

/* Mostra il dizionario */
void print_dict(dict d){
	int i;
	for (i = 0; i < d.M; i++){
		printf("%d ", i);
		print_llist(d.a[i]);
		printf("\n");
	}
}

/*
 * Elimina dal dizionario l'elemento con chiave k (se esiste)
 * Restituisce 1 se k è una chiave, 0 altrimenti
 * 
 * */
int dict_del(dict d, char *k){
	int p = h(d, k);
	node *x, *q = dict_search(d, k);
	if( q == NULL){
		return 0;
	}
	
	if (d.a[p] == q){  /* cancellazione dalla testa della lista*/
		d.a[p] = q->next;
	} else {
		x = d.a[p];
		while ( x->next != q ){
			x = x->next;
		}
		x->next = q->next;
	}
	free(q);
	d.n--;
	return 1;
}

/********************************************************/
/********************************************************/
/********************************************************/


node *in0(node *nd, dict_item e){
	node *p = malloc(sizeof(node));
	
	p->info = e;
	p->next = nd;
	nd = p;
		
	return nd;
}

void print_llist(node *nd){
	node *p = nd;
	
	while( p != NULL ){
		printf("(\"%s\", %f) ", p->info.k, p->info.v);
		p = p->next; /*equivalente a p = (*p).next */
	}
}

dict dict_resize(dict d0, int new_M){
	dict d1 = dict_init(new_M);
	int i;
	node *q;
	for (i = 0; i < d0.M; i++){
		while(d0.a[i] != NULL){
			dict_set(d1, d0.a[i]->info);
			/* cancello il primo nodo di d.a[i]*/
			q = d0.a[i];
			d0.a[i] = q->next;
			free(q);
		}
	} 
	free(d0.a);
	return d1;
}

