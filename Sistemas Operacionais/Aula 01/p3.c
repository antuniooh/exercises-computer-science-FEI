#include <stdlib.h>
#include <stdio.h>

int v1;

void f(int v3){
    int v4;
    printf("Endereço de v3 = %p \n", &v3);
    printf("Endereço de v4 = %p \n", &v4);
    f(v3+1);
}

int main(){
    int v2;

    printf("Endereço de main() = %p \n", main);
    printf("Endereço de fmain() = %p \n", f);

    printf("Endereço de v1 = %p \n", &v1);
    printf("Endereço de v2 = %p \n", &v2);
    f(0);

    return 0;
}