#include <stdio.h>
#include <stdlib.h>

struct array_int {
	int *a;
	int n;
};
typedef struct array_int array_int;


array_int array_int_init(void);
array_int array_int_append( array_int, int );
void array_int_print(array_int);

void main(){
	array_int v = array_int_init();
	int i, n = 14; 
	
	for(i = 0; i < n; i++){ // O(n^2)
		v = array_int_append(v, i*10);
	}
	
	array_int_print(v);
}

array_int array_int_init(void){ // O(1)
	array_int v = {NULL, 0};
	return v;
}

array_int array_int_append( array_int v, int e ){ // O(v.n) 
	int i;
	int *a = malloc((v.n+1)*sizeof(int));
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < v.n; i++){
			a[i] = v.a[i]; 
		}
		a[v.n] = e;
		v.n++;
		free(v.a);
		v.a = a;
	}
	
	return v;
}

void array_int_print(array_int v){ // O(v.n)
	int i;
	
	printf("[");
	for( i = 0 ; i < v.n; i++){
		printf("%d,", v.a[i]);
	}
	printf("]\n");
}
