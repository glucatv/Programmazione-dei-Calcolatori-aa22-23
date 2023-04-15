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


void main(){
	linked_list L = init();
	int e;
	
	for(e = 0; e < 10; e++){
		L = in0(L, (e+1)*11.1);
	}
		
	print_llist(L);
}

linked_list in0(linked_list L, float e){
	node *p = malloc(sizeof(node));
	
	p->v = e;
	p->next = L.a;
	L.a = p;
	L.n++;
	
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
}
