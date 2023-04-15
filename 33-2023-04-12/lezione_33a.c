#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct object {
	char type; // 'i', 'c' ed 's' per int, char e stringa
	void *pointer;
};
typedef struct object object;

struct list {
	object *a;
	int n; /*dimensione di a*/
};
typedef struct list list;

object new_int(int);
object new_char(char);
object new_string_alias(char*);
object new_string_clone(char*);
void print_list(list);

void main(){
	list L = {NULL, 10};
	L.a = malloc(sizeof(object)*L.n);
	
	char a[] = "programmazione";
	
	L.a[0] = new_int(4);
	L.a[1] = new_char('x');
	L.a[2] = new_string_alias("questa non è una lista python");
	L.a[3] = new_string_clone(a);
	
	a[0] = 'P'; 

	print_list(L);
}

void print_list(list L){
	int i;

	printf("[");
	for(i = 0; i < L.n; i++){
		if( L.a[i].type == 'i' )
			printf("%d ", *((int*)L.a[i].pointer));
		else if ( L.a[i].type == 'c' )
			printf("%c ", *((char*)L.a[i].pointer));
		else printf("\"%s\" ", (char*)L.a[i].pointer );
	}
	printf("]\n");
}


object new_int(int v){
	object ob = {'i', NULL};
	ob.pointer = malloc(sizeof(int));
	*((int*)ob.pointer) = v;
	return ob;
}

object new_char(char v){
	object ob = {'c', NULL};
	ob.pointer = malloc(sizeof(char));
	*((char*)ob.pointer) = v;
	return ob;
}

object new_string_alias(char *v){
	object ob = {'s', NULL};
	ob.pointer = v; /* ob.pointer è un alias, complessità temporale e spaziale  O(1)  */
	/*
	ob.pointer = malloc(sizeof(char));
	*((char*)ob.pointer) = v;*/
	return ob;
}

object new_string_clone(char *v){
	object ob = {'s', NULL}; /* ob.pointer contiene una copia, complessità temporale e spaziale  O(strlen(v))  */
	ob.pointer = malloc(sizeof(char)*(strlen(v)+1));
	ob.pointer = strcpy(ob.pointer, v);
	return ob;
}
