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
            printf("%10d ", M[i][j]);
        }
        printf("\n");
    }
}
int** multiplicar(int **M1, int l1, int c1,int **M2, int c2) {
    int **MR = matriz(l1, c2);//primeiro com o ultimo
    zera(MR, l1,c2);

    int i,a,b;
    for (a = 0; a < l1; a++) {
        for (b = 0; b < c2; b++) {
            for (i = 0; i < c1; i++) {
                MR[a][b] += M1[a][i] * M2[i][b];
            }
        }
    }
    return MR;
}
void sequencia(int **M, int l, int c){
    int i,j;
    int z =1;
    for (i = 0; i < l; i++) {
        for (j = 0; j < c; j++) {
            M[i][j] = z++;

        }
    }
}

void preencher(int **M, int l, int c){
    int i,j;
    int z =0;

    for (j = c-1; j >= 0 ; j--) {
        for (i = l-1; i >= 0; i--) {
            M[i][j] = z++;
        }
    }
}
void preencherZeroUm(int **M, int l, int c) {
    int i,j;

    for (i = 0; i < l; i++) {
        for (j = 0; j < c ; j++) {
            if((i+j)%2 ==0)
                M[i][j] = 0;
            else
                M[i][j] = 1;
        }
    }
}


int main() {

    /*int **M = malloc(sizeof(int *) * 2);

    {
        int *L1 = malloc(sizeof(int) * 3);
        for (int i = 1, j = 0; i < 4, j < 3; ++i, j++) {
            L1[j] = i;
        }

        int *L2 = malloc(sizeof(int) * 3);
        for (int i = 4, j = 0; i < 7, j < 3; ++i, j++) {
            L2[j] = i;
        }
        M[0] = L1;
        M[1] = L2;
    }*/
    //for(int i- 0; i < 100; i++) M[i] = malloc....


    int **p = matriz(5,10);
    zera(p, 5,10);
    sequencia(p,5,10);
    //imprime(p, 5,10);
    destroi(p,5);

    //cria as duas matrizes
    int **M1 = matriz(3,4);
    sequencia(M1,3,4);
    imprime(M1, 3,4);
    puts("");

    int **M2 = matriz(4,2);
    sequencia(M2,4,2);
    imprime(M2,4,2);
    puts("");

    //matriz resultante
    int **M3 = multiplicar(M1,3,4,M2,2);
    imprime(M3, 3,2);
    puts("");

    destroi(M1,3);
    destroi(M2,4);
    destroi(M3,3);

    //matriz nova
    int **M = matriz(4,5);
    preencher(M,4,5);
    imprime(M,4,5);
    puts("");
    destroi(M,4);


    int **M4 = matriz(4,4);
    preencherZeroUm(M4,4,4);
    imprime(M4,4,4);
    destroi(M4,4);



    //(a[0])[i]
    return 0;
}