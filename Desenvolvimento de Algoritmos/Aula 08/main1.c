#include <stdio.h>
#include <stdlib.h>

int** criaMatriz(int l, int c){
    int* *M = malloc(sizeof(int*) * l );
    int i;
    for(i=0; i < l; i++){
        int* linha = malloc(sizeof(int) * c);
        M[i] = linha;
    }

    return M;
}

void zeraMatriz(int* *M, int l, int c){
    int i;
    int j;
    for(i=0; i<l;i++) {
        for(j=0; j<c;j++) {
            M[i][j] = 0;
        }
    }
}

void imprimeMatriz(int* *M, int l, int c){
    int i;
    int j;
    for(i=0; i<l;i++) {
        for(j=0; j<c;j++) {
            printf("%-5d|", M[i][j]);
        }
        printf("\n");
    }
}

void preencheSequencia(int** M, int l, int c){
    int i;
    int j;
    int z = 1;
    for(i=0; i<l;i++) {
        for(j=0; j<c;j++) {
           M[i][j] = z++;
        }
    }
}

void destroiMatriz(int* *M, int l){
    int i;
    for(i=0; i<l; i++)
        free(M[i]);

    free(M); //último
}


int** multiplica(int* *M1, int* *M2,
        int nl1, int nc1, int nc2){
    int** R = criaMatriz(nl1, nc2);
    zeraMatriz(R, nl1, nc2);

    int i,a,b;
    for(a=0;a<nl1;a++){
        for(b=0;b<nc2;b++){
            for (i = 0; i < nc1; i++) {
                R[a][b] += M1[a][i] * M2[i][b];
            }
        }
    }
    return R;
}

void preencheContrario(int** M, int l, int c){
    int i;
    int j;
    int k=0;
    for(j=c-1; j>=0; j--){
        for(i=l-1; i>=0; i--){
            M[i][j] = k++;
        }
    }
}

void preencheBinario(int** M, int l, int c){
    int i,j;
    for(i=0;i<l;i++){
        for(j=0;j<l;j++) {
            if( (i+j) % 2 == 0 ){
                M[i][j] = 0;
            }else{
                M[i][j] = 1;
            }
        }
    }
}


void preencheBinario2(int** M, int l, int c){
    int i,j;
    for(i=0;i<l;i++){
        int inicio;
        if( i % 2 == 0 ) {
            inicio = 0;
        }else{
            inicio = 1;
        }
        for (j = 0; j < l; j++) {
            M[i][j] = inicio;
            if(inicio == 0){
                inicio = 1;
            }else{
                inicio = 0;
            }
        }
    }
}


int main() {
    int* *Matriz1 = criaMatriz(10,5);
    int* *Matriz2 = criaMatriz(4,2);
    preencheContrario(Matriz1, 10,5);
    imprimeMatriz(Matriz1, 10,5);
    /*
    preencheSequencia(Matriz2, 4,2);

    int* *resultado =
            multiplica(Matriz1, Matriz2, 3, 4, 2);

    imprimeMatriz(resultado, 3,2);
*/
    destroiMatriz(Matriz1, 5);
    destroiMatriz(Matriz2, 4);
   // destroiMatriz(resultado, 3);





    return 0;
}