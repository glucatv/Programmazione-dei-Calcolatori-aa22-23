#include <stdio.h>


void incrementa_int(int*);

void main(){
	int n = 1, m = 10, x = 10;
	float f;
	int d;
	char s[256] = "(123;456.788)";
	incrementa_int( &x );
	printf("%d\n", x);
	
	
	/*d = scanf("(%d;%d)", &n, &m);
	printf("%d, %d, %d\n", n, m, d);*/
	
	/*scanf("%s", s);
	printf("%s\n", s);*/
	
	d = sscanf(s, "(%d;%f)", &n, &f);
	printf("%d, %f, %d\n", n, f, d);
}

void incrementa_int(int *z){
	(*z)++;
}
