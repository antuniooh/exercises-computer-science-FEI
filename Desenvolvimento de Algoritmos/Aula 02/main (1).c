#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) 
{
	int *x=NULL;
	int n;
	do{
		printf("Digite quantos numeros\n");
		scanf("%d", &n);
	}while(n <= 0 || n > 10);
	x = malloc(4*n);

	//x já alocado
	int i;
	int num;
	for(i=0; i<n; i++){
		scanf("%d",  x+i );
		printf("val digitado: %d\n",  *(x+i)  );
	}

	float soma=0;
	for(i=0; i<n;i++){
		soma += *(x+i);
	}
	float media = soma/n;

	soma = 0;
	for(i=0; i<n;i++){
		int xi = *(x+i);
		float parcela = (xi - media)*(xi - media);
		soma += parcela;
	}
	float std = sqrt(soma/n);
	printf("media: %f\n", media);
	printf("desvio: %f\n", std);
	
	
	free(x);
	
	system("pause");	
	return 0;
}
