#include <stdio.h>

float media(int *vetor, int tam){
    int i;
    float soma=0;
    for(i=0;i<tam;i++){
        soma += vetor[i];
    }
    return soma/tam;
}

void imprime(int* v, int n){
    int i;
    for(i=0;i<n;i++)
        printf("%d ", v[i]);
    printf("\n");
}

int busca(int* p, int n, int val){
    int i;
    for(i=0;i<n;i++){
        if(p[i] == val)
            return i;
    }
    return -1;
}

int contaInter(int *v1, int *v2, int tam1, int tam2){
    int i;
    int total = 0;
    for(i=0;i<tam2; i++){
        int daVez = v2[i];
        int r = busca(v1, tam1, daVez);
        if(r != -1){
            printf("encontrado: %d\n", v1[r]);
            total++;
        }
    }
    return total;
}

int main() {
    int v[20];
    int v2[5];
    int i;
    for(i=0;i<20;i++)
        v[i] = (5*i*i-i+3)% 50;
    for(i=0;i<5;i++)
        v2[i] = (2*i*i-i+3)% 50;

    imprime(v, 20);
    imprime(v2, 5);
    int idx = busca(v, 20, 15);
    int comuns = contaInter(v,v2,20,5);
    //printf("o numero 15 ocorreu na posicao %d\n", idx);
    printf("%d\n", comuns);
    return 0;
}