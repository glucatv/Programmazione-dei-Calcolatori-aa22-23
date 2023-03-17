#include <stdio.h>
#include <math.h>

float radice_quadrata( float x, float eps ){
	float g = x/2;
	int c = 0, max_iter = 1000;
	while ( fabs( g*g-x ) > eps && c < max_iter  ){
		 g = 0.5 * ( g + x/g );
		 c++; // equivalente a c+= 1; esiste anche c--
	}
	return g;
}

void test_char(){
	char c;
	
	for(c = 'a'; c <= 'z'; c++)
		printf("Il codice ASCII di %c e' %d\n", c, c);
}

void main(){
    int x;
	float y, eps = 0.00000001;
 
	for( x = 2; x < 12; x++){
		y = radice_quadrata(x, eps);	
		printf("La radice quadrata di %d e' %.5f\n", x, y);
		
		
		if ( fabs(y*y - x) > eps  ) {
			printf("Raggiunto numero massimo di iterazioni\n"); // blocco da un'unica istruzione, non necessita {}
		} else
			printf("|y*y - x| <= eps\n");
	}
	
	test_char();
}

/*
 *  Operatori logici
 * 		&& and
 * 		|| or
 * 		!  not  
 * 
 * 
 * 	Operatori relazionali
 * 		==, !=
 * 		>, <, <=, >=
 * 
 * */
 
 
 
 /*
  * for(istr0; cond;  istr1){
  * 	blocco;
  * }
  * 
  * equivale a
  * 
  * istr0;
  * while( cond ){
  * 	blocco;
  * 	istr1;
  * }
  * 
  * */
