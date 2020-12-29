#include <stdio.h>
//vetores é um area continua da memoria


float media(int *vetor, int N){
    int i;
    float soma =0;
    for (i = 0; i < N; ++i) {
        soma += vetor[i];
    }
    return (soma/N);
}

void retornar(int* vetor, int N){
    for (int i = 0; i < N; i++) {
        printf("%d  ", *(vetor+i)/*vetor[i]*/);
    }
}
int busca(int* vetor, int N, int x){
    for (int i = 0; i < N; i++) {
        if(vetor[i] == x){
            return i;
        }
    }
    return -1; // caso do erro
}
void ordenar(int *vetor, int N){
    int k, j, aux;

    //repetir o looping de comparação N vezes
    for (k = 1; k < N; k++) {
        for (j = 0; j < N - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                //auxiliar vira o maior valor
                aux = vetor[j];
                //o valor vira o menor q veio dps
                vetor[j] = vetor[j + 1];
                //o menor vira o maior
                vetor[j + 1] = aux;
            }
        }
    }
    //feedback da ordenação
    for (int i = 0; i < N; ++i) {
        printf("%d ", vetor[i]);
    }
}

int incidencias(int* v, int*v1, int N, int N2){
    int total=0, i,j;

    for (i = 0; i < N2; i++) {
        for(j = 0; j < N; j++){
            if(v[j] == v1[i]){
                total+=1;
            }
        }
    }
    return total;

    /* possibilidade de usar a função busca*/


}



int main() {
    //int idades[10];
    //possivel inicilizar idades[50] = {1,2,2...} ou idades[50] = {0}
    //ou numeros[] = {1,2,3,3,5,8}

    /*int i;
    //[inicialiazção][condicuionakl][implemento]
    for (i = 0; i < 10; ++i) {
        idades[i] =0;
    }
    printf("%d\n",idades[0]);


    int j;
    for (j = 0; j <10 ; ++j) {

    }
    printf("%d\n", j);//imprime 10

    //while(1);la~ço infinito
    //while (1<10){i++;}*/

    /*do{
        printf("%d",i);
    }while (i<10);*///primeiro executa e dps ve se volta, logo há um erro no primeiro caso - usado para validação

    /*for (int i = 0; i < 10; ++i) {
        idades[i]=0;
    }
    for (int j = 0; j < 10; ++j) {
        printf("Entre com a idade: ");
        scanf("%d",&idades[j]);
    }
    for (int k = 0; k < 10; ++k) {
        printf("idades[%d]: %d\n",k+1,idades[k]);
    }*/

    /*int i;
    for (i = 0; i < 10; i++) {
          int x;
          do{
              printf("Entre com a idade de %d: ", i+1);
              scanf("%d\n",&x);
          } while(x < 0);
          idades[i] = x;
      }

    float t=0;
    for (int k = 0; k < 10; k++) {
        t+= idades[k]*1.0;
    }
    printf("Media: %.2f\n", (t/10.));

    //system(pause);

    //stack overflow, estourar a memoria, pode ser devido a vetor*/

    int v[20];
    int v2[5];

    int i;
    int j;

    for (i = 0; i < 20; i++) {
        v[i] = (5*i*i-i+3)%50;
    }

    for (j = 0; j < 5; j++) {
        v2[j] = (2*j*j-j+3)%50;
    }

    /*printf("%d\n", *(v+1));//imprime o valor
    printf("%d\n", v); // oimprime o ponteiro*/


    /*float resultado = media(v,20);
    printf("%.1f", resultado);*/
    retornar(v, 20);
    retornar(v2, 5);


   /* int idx = busca(v, 20, 15);
    printf("\nO numero 15 ocorreu na posicao: %d\n",idx);
    ordenar(v, 20);*/

    int a = incidencias(v, v2, 20, 5);
    printf("\ntotal de incidencias: %d\n", a);

    //v[0] = *v ou v[1] = *(v+1)
    // v[i] = i ou *(v+i) = i


    return 0;
}