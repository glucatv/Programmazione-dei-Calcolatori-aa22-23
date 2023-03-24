#include <stdio.h>

/*
 * Lista prototipi
 * */
char switch_case( char ); // va bene anche  char switch_case( char c );

void main(){
	char c = 'd', c_out;
	printf("%c - %c\n", c, switch_case(c) );
	
	c = 'E';
	printf("%c - %c\n", c, switch_case(c) );
	
	c = '0';
	c_out = switch_case(c);
	if( c_out == -1)
		printf("%c non e' una lettera\n", c);
	else
		printf("%c - %c\n", c, c_out );
}

char switch_case( char c ){
	if ( c >= 'A' && c <= 'Z' ){ // test se c e' maiuscolo
		return 'a' + c - 'A';
	} else if ( c >= 'a' && c <= 'z' ){ // test se c e' minuscolo
		return 'A' + c - 'a';
	} else {
		return -1;
	}
}
