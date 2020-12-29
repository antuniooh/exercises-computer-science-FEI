#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <locale.h>

struct sPonto {
    int numerador;
    int denominador;
};

struct Pontos{
    int n;
    struct sPonto v[100];
};

void adicionaPontos(struct Pontos * P, int n, FILE*f){
    P->n = n;
    fprintf(f, "Dado o poligono de %d vertices:\n", n);

    for (int i = 0; i < n; ++i) {
        puts("Digite o numerador e numerador");
        scanf("%d %d", &P->v[i].numerador, &P->v[i].denominador);
        fprintf(f, "x: %d\n", P->v[i].numerador);
        fprintf(f, "y: %d \n",P->v[i].denominador);
    }
}

float dist(struct sPonto x, struct sPonto y){
    float dist;
    dist = sqrt(pow(x.numerador - y.numerador,2) + pow(x.denominador - y.denominador,2));
    return dist;
}

void perimetro(struct Pontos p, int n, FILE *f){
    float soma=0;
    for (int i = 0; i < n-1; ++i) {
        soma+= dist(p.v[i], p.v[i+1]);
    }
    soma+=dist(p.v[0], p.v[n-1]);
    fprintf(f, "O perimetro e: %f \n",soma);
    puts("O perimetro e:");
    printf("%f", soma);
}

int main(int argc, char *argv[]){
    struct Pontos P;
    int n;
    FILE * f = fopen("PoligonoW.txt", "w");

    puts("Digite a quantidade de pontos");
    scanf("%d", &n);

    while(n <= 1){
        puts("ora ora");
        scanf("%d", &n);
    }

    adicionaPontos(&P, n, f);
    perimetro(P, n, f);


    return 0;
}
