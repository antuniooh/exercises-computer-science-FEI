#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
    printf("tam float eh: %d\n", sizeof(float));
	int n;
	scanf("%d", &n);
	float *b1 = malloc(sizeof(float)*n);
	float *b2 = malloc(sizeof(float)*n);
	float *b3 = malloc(sizeof(float)*n);
	
	int i;
	for(i=0; i<n;i++){
		scanf("%f", b1+i);
		scanf("%f", b2+i);
		b3[i] = b2[i]+b1[i];
		printf("%f ", b3[i]);
	}
	printf("\n");
	
	
	free(b1);
	free(b2);
	free(b3);

	system("pause");	
	return 0;
}
