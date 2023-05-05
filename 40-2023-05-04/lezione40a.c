#include <stdio.h>
#include <stdlib.h>

union nome_union {
	char c_val;
	int i_val;
	float f_val;
};


void main(){
	union {
		char c_val;
		int i_val;
		float f_val;
	} u;
	
	union nome_union u0;

	u.i_val = 8;
	
	printf("%d\n", u.i_val);
	
	u.c_val = 'a';
	printf("%c\n", u.c_val);

	u0.f_val = 3.14;
	printf("%f\n", u0.f_val);
	
	printf("%d\n", u0.i_val);

}




