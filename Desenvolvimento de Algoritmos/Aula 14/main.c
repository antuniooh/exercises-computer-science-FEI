#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define MAX 1000 // todo lugar que houver max será substituido por 1000

struct pessoa{
    char nome[80];
    int idade;
    char endereco[80];
    char cep[20];
};

void inicializaPessoa(struct pessoa* pp){
    (*pp).idade = 0;
    strcpy((*pp).nome, "");
    strcpy((*pp).endereco, "");
    strcpy((*pp).cep, "");
}

void imprimePessoa(struct pessoa pessoa){
    printf("Nome: %s\n", pessoa.nome);
    printf("Endereco: %s\n", pessoa.endereco);
    printf("Cep: %s\n", pessoa.cep);
    printf("Idade: %d\n", pessoa.idade);
    puts("======================");
}

void usuarioPreenche(struct pessoa* pp){
    puts("Digite o nome: ");
    gets((*pp).nome);
    puts("Digite o endereco: ");
    gets((*pp).endereco);
    puts("Digite o cep: ");
    gets((*pp).cep);
    puts("Digite a idade: ");
    scanf("%d", &((*pp).idade));
    fflush(stdin);
}

struct ponto{
    float x;
    float y;
};
struct circulo{
    struct ponto centro;
    float raio;
};

int main() {
    struct pessoa p[100];
    /*p.idade = 10;
    strcpy(p.nome, "GUILHER");
    strcpy(p.endereco, "JSJJSJS");*/
    //inicializaPessoa(&p);
    usuarioPreenche(&p[0]);
    imprimePessoa(p[0]);

    struct circulo c;
    c.centro.x = 4;
    c.centro.y = 8;
    c.raio = 5;

    return 0;
}