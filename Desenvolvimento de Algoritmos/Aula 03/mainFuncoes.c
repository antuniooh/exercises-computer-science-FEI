#include <stdio.h>
#include <stdlib.h>

void contaAte(int n){
	int i;
	for(i=1; i <= n; i++){
		if(i == 15){
			return;
		}else
	    	printf("%d\n", i);
	}

	printf("acabei\n");
}

void imprimeMsg(){
	printf("Mensagem aqui!!\n");
}

int soma(int a, int b){
	return a+b;
}

void copia(const int *src, int *dst){
	*dst = *src;
}
void troca( int *a, int *b ){
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}

int main(int argc, char *argv[]) 
{
	int x=5;
	int y=10;
	troca( &x, &y);
	
	printf("%d\n",x);
	printf("%d\n",y);
	

	system("pause");
	return 0;
}


