#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <locale.h>

int main(int argc, char *argv[]){

   FILE* f = fopen("arq.txt","r");

   float x;
   fscanf(f," %*f",&x);
   printf("Lido: %f", x);

   /*char nomeArquivo[100];
    for (int i = 0; i < 1000; ++i) {
        sprintf(nomeArquivo, "meuArquivo%d.txt", i + 1);
        FILE *f = fopen(nomeArquivo, "w");
        for (int i = 0; i < 10000; ++i) {
            fprintf(f, "contagem %d \n", i);
        }
        fclose(f);

    }*/

    //fprintf(f, "%d %f\n", 1, 0.5);
    fclose(f);

    return 0;
}
