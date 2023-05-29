#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void zip(int *a, int na, int *b, int nb, int ***z, int *nz);
char *reverse_string(char *a);
int **enumerate(int *a, int na);

void main(){
	int x[] = {0, 1, 4, 5, 7};
	int y[] = {7, 0, 3, 9};
	int **xy;
	int i, nxy;
	
	zip(x, sizeof(x)/sizeof(int), y, sizeof(y)/sizeof(int), &xy, &nxy );


	printf("[");
	for( i = 0; i < nxy; i++){
		printf("(%d, %d) ", xy[i][0], xy[i][1]);
	}
	printf("]\n");


	char *a = reverse_string("programma");
	printf("%s\n", a);
	
	
	int n = sizeof(x)/sizeof(int);
	int **ex = enumerate(x, n);
	
	printf("[");
	for( i = 0; i < n; i++){
		printf("(%d, %d) ", ex[i][0], ex[i][1]);
	}
	printf("]\n");
}

void zip(int *a, int na, int *b, int nb, int ***z, int *nz){
	int i;
	*nz = na;
	if (nb < na)
		*nz = nb;
	int **tz;
	
	tz = malloc( (*nz)*sizeof(int*) );
	
	for( i = 0; i < *nz; i++){
		/* definiamo z[i] */
		/* z[i] deve essere un array di dimensione 2 */
		tz[i] = malloc(2*sizeof(int));
		tz[i][0] = a[i];
		tz[i][1] = b[i];
	}
	
	*z = tz; 
}


char *reverse_string(char *a){
	int i, n = strlen(a);
	char *ra = malloc((n+1)*sizeof(char));
	
	for(i = 0; i < n; i++){
		ra[n-i-1] = a[i];
	}
	
	ra[n] = '\0';
	
	return ra;
}

int **enumerate(int *x, int nx){
	int i, **out = malloc(nx*sizeof(int*));
	
	for(i = 0; i < nx; i++){
		out[i] = malloc(2*sizeof(int));
		out[i][0] = i;
		out[i][1] = x[i];
	}
	
	return out;
}


