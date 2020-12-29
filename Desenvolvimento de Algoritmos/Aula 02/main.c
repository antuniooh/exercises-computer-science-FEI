#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{

	float soma=0;
	int n=0;
	int atual=0;
	
	while(atual != -1){
		scanf("%d", &atual);
		soma+=atual;
		n++;
	}
	soma=soma+1;
	n=n-1;
	if(n>0){
		float media = soma/n;
		printf("%f\n", media);
	}else{
        printf("nenhum numero!!!\n");
	}

	system("pause");	
	return 0;
}
