#include <stdio.h>
#include <stdlib.h>

void change_array(int x[], int n);
int *copy_array( int *x, int n );
int *append_array( int *x, int n, int e );

void main(){
	int d[15] = {0, 10, 20, 30, 40};
	int i, len_d = sizeof(d)/sizeof(int);
	int *p;
	int b[10] = {1,2};
	int len_b = sizeof(b)/sizeof(int);
	int len_p;
	
	
	change_array(d, len_d);
	for(i = 0; i < len_d; i++){
		printf("%d, ", d[i]);
	}
	printf("\n");
	
	p = copy_array(d, len_d);
	len_p = len_d;
	if (p != NULL) {
		for(i = 0; i < len_d; i++){
			printf("%d, ", p[i]);
		}
		printf("\n");
	} else {
		printf("Errore di memoria\n");
	}
	p = append_array(p, len_p, 100);
	len_p++;
	if (p != NULL) {
		for(i = 0; i < len_p; i++){
			printf("%d, ", p[i]);
		}
		printf("\n");
	} else {
		printf("Errore di memoria\n");
	}
}

int *append_array( int *x, int n, int e ){
	int i;
	int *a = malloc((n+1)*sizeof(int));
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < n; i++){
			a[i] = x[i]; // ORRORE :-) significa a[i] = x[i]
		}
		a[n] = e;
	}
	free(x);
	return a;
}

int *copy_array( int *x, int n ){ // equivalente a (int x[], int n)
	int i;
	int *a = malloc(n*sizeof(int));
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < n; i++){
			(a+i)[0] = x[i]; // ORRORE :-) significa a[i] = x[i]
		}
	}
	
	return a;
}


void change_array(int x[], int n){
	int i;
	for (i = 0; i < n; i++){
		x[i] = 10*i;
	}
}
