#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
	float v;
	struct node *next;
};
typedef struct node node;

struct linked_list {
	node *a; /* punta al primo elemento della sequenza*/
	int n;
};
typedef struct linked_list linked_list;

void print_llist(linked_list);
linked_list in0(linked_list, float);
linked_list init(void);
node *search(linked_list, int);
linked_list insert(linked_list, int, float);
linked_list delete(linked_list, int);
linked_list del0(linked_list);


void main(){
	linked_list L = init();
	int e;
	node *p0, *p4, *pu, *pf;
	
	for(e = 0; e < 10; e++){
		L = in0(L, (e+1)*11.1);
	}
		
	print_llist(L);
	
	p0 = search(L, 0);
	p4 = search(L, 4);
	pu = search(L, L.n-1);
	pf = search(L, L.n*2);
	
	printf("%f, %f, %f, ", p0->v, p4->v, pu->v);
	if (pf == NULL)
		printf("NULL\n");
		
	L = insert(L, 1, 1);
	L = insert(L, L.n, L.n);
	L = insert(L, 4, 4.0);
	L = insert(L, 100000, 3.14);
	L = insert(L, 0, 2.71);
	
	print_llist(L);
	
	printf("--------------------------\n");
	
	L = delete(L, 4);
	L = delete(L, 0);
	L = delete(L, L.n-1);
	L = delete(L, L.n);
	
	print_llist(L);
}

linked_list delete(linked_list L, int pos){
	node *q, *p;
	if (pos > 0 && pos < L.n){
		q = search(L, pos-1);
		p = q->next;
		q->next = p->next;
		free(p);
		L.n--;
	} else if ( pos == 0 && L.n > 0) {
		L = del0(L);
	}
	
	return L;
}

linked_list insert(linked_list L, int pos, float e){
	node *q, *p;
	if (pos > 0 && pos <= L.n) {
		q = search(L, pos-1);
		p = malloc(sizeof(node));
		p->v = e;
		p->next = q->next;
		q->next = p;
		L.n++;
	} else if ( pos == 0) {
		L = in0(L, e);
	}
	
	return L;
}


linked_list in0(linked_list L, float e){
	node *p = malloc(sizeof(node));
	
	p->v = e;
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
		free(p);
		L.n--;
	}
	return L;
}

void print_llist(linked_list L){
	node *p = L.a;
	
	while( p != NULL ){
		printf("%f\n", (*p).v);
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
