#include <stdio.h>
#include <stdlib.h>

struct array_int {
	int *a;
	int n;
};
typedef struct array_int array_int;


array_int array_int_init(void);
array_int append_array( array_int, int );

void main(){
	array_int v = array_int_init();
	int i; 
	
	
	v = append_array(v, 10);
	

	for( i = 0 ; i < v.n; i++){
		printf("%d\n", v.a[i]);
	}
	
}

array_int array_int_init(void){
	array_int v = {NULL, 0};
	return v;
}

array_int append_array( array_int v, int e ){
	int i;
	int *a = malloc((v.n+1)*sizeof(int));
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < v.n; i++){
			a[i] = v.a[i]; // ORRORE :-) significa a[i] = x[i]
		}
		a[v.n] = e;
		v.n++;
		free(v.a);
		v.a = a;
	}
	
	
	return v;
}
