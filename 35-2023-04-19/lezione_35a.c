#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
	char *v;
	struct node *next;
};
typedef struct node node;

struct linked_list {
	node *a; /* punta al primo elemento della sequenza*/
	int n;
};
typedef struct linked_list linked_list;

void print_llist(linked_list);
linked_list in0(linked_list, char*);
linked_list init(void);
node *search(linked_list, int);
linked_list insert(linked_list, int, char*);
linked_list delete(linked_list, int);
linked_list del0(linked_list);
linked_list move_to_tail(linked_list L);


void main(int dim, char *args[]){
	linked_list L = init();
	linked_list p = init();
	int i;
	
	for(i = 1; i < dim; i++){
		 if ( L.a == NULL ){
			L = insert(L, 0, args[i]);
			p.a = L.a;
			p.n = 1;
		 } else {
			 p = insert(p, 1, args[i]);
			 p.n = 1;
			 L.n++;
			 p.a = p.a->next;
		 }
	}
	
	L = move_to_tail(L);	
	print_llist(L);
}

linked_list move_to_tail(linked_list L) {
	node *p, *q;
	if(L.n > 1) {
		p = search(L, L.n-1);
		q = L.a;
		L.a = L.a->next;
		p->next = q;
		q->next = NULL;
	}
	return L;
}


linked_list delete(linked_list L, int pos){
	node *q, *p;
	if (pos > 0 && pos < L.n){
		q = search(L, pos-1);
		p = q->next;
		q->next = p->next;
		free(p->v);
		free(p);
		L.n--;
	} else if ( pos == 0 && L.n > 0) {
		L = del0(L);
	}
	
	return L;
}

linked_list insert(linked_list L, int pos, char *e){
	node *q, *p;
	if (pos > 0 && pos <= L.n) {
		q = search(L, pos-1);
		p = malloc(sizeof(node));
		p->v = malloc(sizeof(char)*(strlen(e)+1));
		p->v = strcpy(p->v, e);
		p->next = q->next;
		q->next = p;
		L.n++;
	} else if ( pos == 0) {
		L = in0(L, e);
	}
	
	return L;
}


linked_list in0(linked_list L, char *e){
	node *p = malloc(sizeof(node));
	
	p->v = malloc(sizeof(char)*(strlen(e)+1));
	p->v = strcpy(p->v, e);
	
	p->next = L.a;
	L.a = p;
	L.n++;
	
	return L;
}

linked_list del0(linked_list L){
	node *p;
	if (L.n > 0 ){
		p = L.a;
		L.a = p->next;
		free(p->v);
		free(p);
		L.n--;
	}
	return L;
}

void print_llist(linked_list L){
	node *p = L.a;
	
	while( p != NULL ){
		printf("\"%s\"\n", (*p).v);
		p = p->next; /*equivalente a p = (*p).next */
	}
}

linked_list init(void) {
	linked_list L = {NULL, 0};
	return L;
}

/*
 * Restituisce il puntatore al node in posizione pos di L. NULL se
 * la posizione pos non esiste
 * */
node *search(linked_list L, int pos){
	node *p = L.a;
	int c = 0;
	
	while( p != NULL && c < pos ){
		p = p->next;
		c++;
	}
	
	return p;
}
