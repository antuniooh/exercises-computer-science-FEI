#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <math.h>

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

int main(){
    struct fracao f;

    puts("Digite o valor do numerador ");
    scanf("%d", &(f.numerador1));
    puts("Digite o valor do denominador ");
    scanf("%d", &(f.denominador1));
    puts("Digite o valor do numerador ");
    scanf("%d", &(f.numerador2));
    puts("Digite o valor do denominador ");
    scanf("%d", &(f.denominador2));

    int mmc = (f.denominador1*f.denominador2)/mdc(f.denominador1, f.denominador2);
    puts("A soma obtida e");
    printf("%d/%d\n", ((f.numerador1 * mmc)/f.denominador1) + (f.numerador2 * mmc)/f.denominador2 , mmc);
    puts("O Produto obtido e");
    printf("%d/%d", f.numerador1*f.numerador2,f.denominador1*f.denominador2);

    return 0;
}
