#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int PA (int i){
    if(i == 0 || i == 1)
        return 1;
    return i+ PA(i-1);
}

int digitos(int i){
    if(i < 10)
        return 1;
    return digitos(i/10)+1;
}

int produto(int a, int b){
    if(b == 1)
        return a;
    return a+ produto(a,b-1);
}
float potencia(float a, float b){
    if(b == 1)
        return a;
    else if(b == 0)
        return 1;
    else if (b < 0){
        return 1/potencia(a, abs(b));
    }
    return a*potencia(a,b-1);
}

int mdc(int a, int b){
    if(a%b == 0){
        return b;
    }
    return mdc(b, a%b);
}
int haloi(int i){
    if(i == 1)
        return i;
    return potencia(2, haloi(i-1));
}


int main() {
    //int x = fat(5);
    //printf("%d\n", x);

    //recurssão pode estourar  a memoria
    //setlocale (LC_ALL, "Portuguese")

    //int x = PA(100);
    //printf("%d\n",x);

    /*int x;
    scanf("%d", &x);
    int d = digitos(x);
    printf("%d\n", d);*/

    int p = produto(100, 65);
    printf("%d\n", p);

    float pot = potencia(2,-3);
    printf("%f\n", pot);

    int m = mdc(23732, 180);
    printf("%d\n", m);,

    int i = haloi(5);
    printf("%d\n", i);



    //system("nome do arquivo")

    return 0;
}