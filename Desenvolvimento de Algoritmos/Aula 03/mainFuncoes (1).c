#include <stdio.h>
#include <stdlib.h>

int maximo( const int *buffer , int n ){
	int i;
	int max=*buffer;
	for(i=1; i< n ; i++){
		if( *(buffer+i) > max )
		    max = *(buffer+i);
	}
	return max;
}

int main(int argc, char *argv[]) 
{
	int n;
	scanf("%d", &n);
	int *v = malloc(sizeof(int)*n);
	int i;
	for(i=0; i<n; i++){
		scanf("%d", v+i);
	}
	
	int m = maximo( v, n );
	printf("maior numero = %d\n", m);
	
	free(v);

	system("pause");
	return 0;
}


