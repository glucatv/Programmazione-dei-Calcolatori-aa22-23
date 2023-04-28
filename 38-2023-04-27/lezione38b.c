#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float **crea_matrice(int, int);
void stampa_matrice(float**, int, int);


void main(int dim, char *args[]){
	float *a = malloc(sizeof(float)*(dim-2));
	int nc, nr, i;
	float f;
	
	float **mt;
	
	if ( sscanf(args[1], "%d", &nc) < 1 ){
		printf("Stringa di help\n");
		return;
	}
	
	for ( i = 2; i < dim; i++){
		if ( sscanf(args[i], "%f", &f) == 1){
			a[i-2] = f;
		} else {
			a[i-2] = 0;
		}
	}
	
	nr = (dim-2)/nc;
	if ( (dim-2)%nc != 0 )
		nr++;

}

float **crea_matrice(int nr, int nc){
	float **mt = malloc(sizeof(float*)*nr);
	int r, c, j;
	
	if (mt == NULL){
		return NULL;
	}
	
	for(r = 0; r < nr; r++){
		mt[r] = malloc(sizeof(float)*nc);
		
		if (mt[r] == NULL){
			
			for( j = 0; j < r; j++){
				free(mt[j]);
			}
			
			free(mt);
			
			return NULL;
		}
		
		for( c = 0; c < nc; c++){
			mt[r][c] = r*c+1;
		}
	}
	
	return mt;
}

void stampa_matrice(float **mt, int nr, int nc){
	int r, c;
		
	for( r = 0; r < nr; r++){
		for( c = 0; c < nc; c++){
			printf("%4.1f ", mt[r][c] );
		}
		printf("\n");
	}
}


