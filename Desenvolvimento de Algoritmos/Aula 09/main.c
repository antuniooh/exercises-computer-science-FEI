#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <math.h>

int* * matriz(int linha, int coluna){
    int * *M = malloc(sizeof(int*)*linha);

    int i;
    for(i= 0; i < linha; i++)
       M[i] = malloc(sizeof(int*)*coluna);

    return M;
}
void zera(int **M, int l, int c){
    int i,j;
    for (i = 0; i < l; i++) {
        for (j = 0; j <c ; j++) {
            M[i][j] = 0;
        }
    }
}
void destroi (int **M, int l){
    for (int i = 0; i < l; ++i) {
        free(M[i]);
    }
}
void imprime(int **M, int l, int c){
    for (int i = 0; i < l; ++i) {
        for (int j = 0; j < c; ++j) {
            printf("%5d ", M[i][j]);
        }
        printf("\n");
    }
}
void preencherDiagonal1(int **M, int l) {
    int i,j;
    /*for (i = 0; i < l; i++) {
        for (j = i; j < l ; j++) {
            M[i][j] = 1;
        }
    }*/
    for (int k = 0; k < l; ++k) {
        for (int m = 0; m < l; ++m) {
            if(m >= k)
                M[k][m] = 1;
            else
                M[k][m] = 0;
        }
    }
}
void preencherDiagonal2(int **M, int l) {
    int i,j;
    /*for (i = 0; i < l; i++) {
        for (j = i; j < l ; j++) {
            M[i][j] = 1;
        }
    }*/
    for (int k = 0; k < l; ++k) {
        for (int m = 0; m < l; ++m) {
            if(m < l-k)
                M[k][m] = 1;
            else
                M[k][m] = 0;
        }
    }
}
void preencherDiagonal3(int **M, int l) {
    int i,j;
    for (i = 0; i < l; ++i) {
        for (j= 0; j < l; ++j) {
            if(j >= i && j < l-i)
                M[i][j] = 1;
            else
                M[i][j] = 0;
        }
    }
}

float distancia (float x1, float y1, float x2, float y2){
    float dist = sqrt(pow((x1-x2),2) + pow((y1-y2),2));
    return dist;
}

void preencher(float *x, float *y, int n){
    int i;
    for (i = 0; i < n; i++) {
        printf("Insira o ponto %d:", i+1);
        scanf("%f %f\n", x+i, y+i);
    }
}

void imprimir(float *x, float*y, int n){
    for (int j = 0; j < n; ++j) {
        printf("Ponto %d: (%.2f, %.2f) \n", j+1, x[j], y[j]);
    }
}

int maisProximo(float *xs, float *ys, int n, float xrel, float yrel){
    int idx =0;
    float distI = distancia(xs[0],ys[0],xrel,yrel);

    for (int i = 0; i < n; ++i) {
        float dist = distancia(xs[i],ys[i],xrel,yrel);

        if(dist < distI){
            distI = dist;
            i = idx;
        }
    }
    return idx;

}

int main() {
    int n;
    puts("Digite a quantidade de numeros:");
    scanf("%d", &n);

    float *xs = malloc(sizeof(float)*n);
    float *ys = malloc(sizeof(float)*n);

    preencher(xs,ys, n);
    imprimir(xs,ys,n);

    int indice = maisProximo(xs, ys, n, 0, 0);
    printf("Mais proximo %d\n", indice);

    free(xs); free(ys);


    return 0;
}