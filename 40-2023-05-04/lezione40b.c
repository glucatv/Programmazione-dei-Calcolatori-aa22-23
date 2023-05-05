#include <stdio.h>
#include <stdlib.h>
#include <string.h>

union item {
	int i_val;
	float f_val;
	char *s_val;
};
typedef union item item;

struct s_item {
	char type; // 'i' i_val , 'f' f_val, 'p' s_val
	item u;
};
typedef struct s_item s_item;

char contains(char *a, char c);

void main(int dim, char *args[]){
	s_item *a = malloc(sizeof(s_item)*(dim-1));
	int i;
	
	for(i = 1; i < dim; i++){
		if ( contains(args[i], '.') == 0 && sscanf(args[i], "%d", &(a[i-1].u.i_val)) == 1)
			a[i-1].type = 'i';
		else if ( sscanf(args[i], "%f", &(a[i-1].u.f_val)) == 1)
			a[i-1].type = 'f';
		else {
			a[i-1].u.s_val = args[i];
			a[i-1].type = 'p';
		}
	}
	
	for(i = 0; i < dim-1; i++){
		if (a[i].type == 'i')
			printf("%d\n", a[i].u.i_val);
		else if (a[i].type == 'f')
			printf("%f\n", a[i].u.f_val);
		else
			printf("%s\n", a[i].u.s_val);
	}
	
}

char contains(char *a, char c){
	int i = 0;
	while(a[i] != '\0'){
		if (a[i] == c)
			return 1;
		i++;
	}
	return 0;
}
