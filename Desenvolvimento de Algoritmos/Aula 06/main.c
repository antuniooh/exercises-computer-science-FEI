#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void imprimir(int *vetor,int N){
    //feedback da ordenação
    for (int i = 0; i < N; ++i) {
        printf("%d ", vetor[i]);
    }
}


void reverso(int *v, int N){
    int i;

    for (i = 0; i < N/2 ; i++) {
        int temp = v[i];
        v[i] = v[N-1-i];
        v[N-1-i] = temp;
    }
}


float y(float x){
    return x*x;
}

//free - devolve o espaço = free(#pointer)
//malloc - deposita no heap

int* aloca(int n, int x){
   int *p = malloc(sizeof(int)*n);
    for (int i = 0; i < n; ++i) {
        p[i] = x;
    }
    return p;
}

double desvio(int n){
    int *p = malloc(sizeof(int)*n);
    double media=0, desvio=0;

    //armazenoutodo mundo no mallco e calcula a média
    for (int i = 0; i < n; i++) {
        scanf("%d ", p+i);
        media += p[i];
    }
    media/=n;

    for (int i = 0; i < n; ++i) {
        desvio = sqrt(pow(p[i]-media,2))/n;
    }
    return desvio;



}

int main() {
    /*int v[] = {1,3,2,5,9,7};
    int n1=6;

    reverso(v,n1);
    imprimir(v,n1);*/


    /*double i;
    double total =0;
    double h =0.0001;
    for (i = 0; i < 5 ; i+=h) {
        double area = ((y(i)+y(i+h))*h)/2;
        total+=area;
    }
    printf("total: %f\n",total);*/


    /*int *p;
    p = malloc(sizeof(int)*10);
    *p = 10;

    //malloc é sequencial

    for (int i = 0; i < 10; ++i) {
        *(p+i)=0;
        p[i] = 0;
    }

    printf("%d\n",*p);
    free(p); //desaloca tudo*/

    //criar um programa que pergunte por N números e populer a area dinamica
    /*int n,i;
    printf("Quantidade de números desejados: ");
    scanf("%d",&n);
    int *p = malloc(sizeof(int)*n);
    for (i = 0; i < n; ++i) {
        scanf("%d",p+i);
        //&p[i]
    }
*/
    //imprimir os números
    /*for (i = 0; i < n; ++i) {
        printf("%d ",*(p+i));
        //p[i]
    }

    free(p);*/

   /* int n =10, x=2;
    int *v = aloca(n,x);

    free(v);*/

   int n;
    printf("Quantidade de números desejados: ");
    scanf("%d",&n);

    double d =desvio(n);
    printf("%f",d);

    return 0;
}