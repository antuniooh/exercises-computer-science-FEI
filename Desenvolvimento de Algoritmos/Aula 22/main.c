#include <iup.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct Pessoa{
    int cod;
    char nome[100];
    int idade;
};

void troca(struct Pessoa *a, struct Pessoa *b){
    struct Pessoa temp = *a;
    *a = *b;
    *b = temp;
}

int ehMaiorIdade(struct Pessoa a, struct Pessoa b){
    return a.idade > b.idade;
}
int ehMaiorCod(struct Pessoa a, struct Pessoa b){
    return a.cod > b.cod;
}
int ehMaiorNome(struct Pessoa a, struct Pessoa b){
    return strcmp(a.cod ,b.cod);
}

void ordena(struct Pessoa *v, int n, int(*p)(struct Pessoa a, struct Pessoa b)){
    int i,j;
    for(i=0; i<n-1;i++){
        for(j=0; j<n-1;j++){
            //if( v[j] > v[j+1] ){
            if( p(v[j], v[j+1]) == 1 ){
                troca(v+j,v+j+1);
            }
        }
    }
}

void imprime(struct Pessoa* v, int n){
    int i;
    for (int j = 0; j < n; ++j) {
        printf("Cod: %d\n Nome: %s\n Idade: %d\n",
               v[j].cod, v[j].nome, v[j].idade);
    }
}

int main(int argc, char **argv){
    struct Pessoa v[] = {
            {1, "Guilherme", 32},
            {6, "João", 10},
            {3, "Vitor", 5},
            {4, "Destro", 50}
    };

    ordena(v, 4, ehMaiorNome);
    imprime(v, 4);

    return 0;
}