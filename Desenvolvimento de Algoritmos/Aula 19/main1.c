#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <locale.h>

int mdc(int a, int b) {
    if (a % b == 0) {
        return b;
    }
    return mdc(b, a % b);
}

struct fracao {
    int numerador1;
    int denominador1;
    int numerador2;
    int denominador2;
};

int main(int argc, char *argv[]){
    struct fracao F;

    FILE* f = fopen("arq.txt","r");

    fscanf(f," %d",&F.numerador1);
    fscanf(f," %d",&F.denominador1);
    fscanf(f," %d",&F.numerador2);
    fscanf(f," %d",&F.denominador2);

    FILE* f1 = fopen("arq1.txt","w");

    int mmc = (F.denominador1*F.denominador2)/mdc(F.denominador1, F.denominador2);
    fprintf(f1, "A soma obtida e\n");
    fprintf(f1, "%d/%d\n", ((F.numerador1 * mmc)/F.denominador1) + (F.numerador2 * mmc)/F.denominador2 , mmc);
    fprintf(f1,"=======================\n");
    fprintf(f1,"O Produto obtido e\n");
    fprintf(f1,"%d/%d", F.numerador1*F.numerador2,F.denominador1*F.denominador2);

    fclose(f);
    fclose(f1);

    return 0;
}
