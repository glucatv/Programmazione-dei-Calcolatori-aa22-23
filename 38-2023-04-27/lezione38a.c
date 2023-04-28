#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float *crea_matrice(int, int);
void stampa_matrice(float*, int, int);
void stampa_posizione(float*, int, int);


void main(){
	float *m = crea_matrice(4, 7);
	
	stampa_matrice(m, 4, 7);
	
	stampa_posizione(m, 7, 9);

}

float *crea_matrice(int nr, int nc){
	float *mt = malloc(sizeof(float)*nr*nc);
	int r, c;
	
	if (mt == NULL){
		return NULL;
	}
	
	for( r = 0; r < nr; r++){
		for( c = 0; c < nc; c++){
			/* in posizione (r,c) scrivere r*c+1 */
			mt[nc*r+c] = r*c+1;
		}
	}
	
	return mt;
}

void stampa_matrice(float *mt, int nr, int nc){
	int r, c;
		
	for( r = 0; r < nr; r++){
		for( c = 0; c < nc; c++){
			/* in posizione (r,c) scrivere r*c+1 */
			printf("%4.1f ", mt[nc*r+c] );
		}
		printf("\n");
	}
}

/*
 * mt è una matrice di nc colonne memorizzata per righe
 * p è un indice in mt
 * 
 * Stampa l'elemento in posizione p di mt e le sue coordinate (riga, colonna)
 * nella matriche rappresentata da mt
 * */
void stampa_posizione(float *mt, int nc, int p){
	int c, r;
	
	c = p%nc;
	r = p/nc;
	
	printf("\nM[%d, %d] = %.1f\n", r, c, mt[p]);
}
