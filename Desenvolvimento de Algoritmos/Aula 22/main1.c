#include <stdlib.h>
#include <iup.h>
#include <stdio.h>

int f1() {
    return 1;
}

int f2() {
    return 2;
}

void imprime(  int (*p)() ){
    int res = p();
    printf("teste %d\n", res /*p()*/);
}

int soma(int a, int b){
    return a+b;
}

int impParametros(int a, int b,  int(*p)(int,int)   ){
    printf("a = %d; b = %d\n",a,b);
    printf("%d",p(a,b));
}

int main(int argc, char **argv)
{
    int (*p)();
    p = f2;
    imprime( p );
    //imprime ( f1 );
    impParametros(2,6, soma);

    return 0;
}