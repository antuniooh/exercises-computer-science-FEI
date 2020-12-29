#include <stdio.h>

int main() {
    //entrada de valores = [unsigned/long] [float/double/char/int][nome]

    /*float x=0; //4 bytes
    float y =x+1; // 4bytes


    /*scanf("%f",&x);

    int a =x;

    printf("Parte Inteira: %d\n",a);

    //printf("%d", &x);

    //declaração de um ponteiro
    float *z = &x;
    float *a = &y;


    printf("%f\n",*z); // imprime o x
    printf("%f\n",*a); // imprime o y

    printf("%f\n",*(z-1)); // imprime o y

*/
   /* int a =1;
    int b =2;
    int c =3;
    int d =4;

    int *p = &c; // ponteiro tem tamanho 8 na arquitetura 64

    printf("%d\n",&a);
    printf("%d\n",&b);
    printf("%d\n",&c);
    printf("%d\n",&d);
    printf("%d\n",p);
    printf("%d\n",*p);

    //*p = 4 // altera o valor do c

    //como saber o tamanho do tipo de variavel = sizeof(tipo)*/

   //set(CMAKE_C_FLAGS -O0) - outro arquivo

    //declarar 5 variaveis inteiras, com zero, ,udar o valor de todas as variaveis com 3linhas
    /*int a =0;
    int b =0;
    int c =0;
    int d =0;
    int e =0;

    printf("%d\n",&a);
    printf("%d\n",&b);
    printf("%d\n",&c);
    printf("%d\n",&d);
    printf("%d\n",&e);

    int *p = &a;

    /*for (i = 0; i < 5; ++i)
    {
        *p = 10;
        p = (p -1);
    }*/

    /*for (p=&a; p != &p; p--)
    {
        *p = 10;
        p = (p -1);
    }

    printf("%d\n",a);
    printf("%d\n",b);
    printf("%d\n",c);
    printf("%d\n",d);
    printf("%d\n",e);*/

    float x = 0;
    float multiplo = 0;
    float *p = &multiplo;

    printf("Coloque o consumo em kwh\n");
    scanf("%f",&x);

    if(x >0 && x < 50)
       *p = 10;
    else if(x >= 50 && x < 300)
        *p = 30;
    else if( x >= 300)
        *p = 50;
    else
        puts("TEXTO FODA");


    printf("Total a pagar R$: %.2f\n", (x*multiplo));
    puts("TEXTO FODA");

    return 0;


    //ponteiro = endereço de onde está a variavel na memoria ram

    //possivel definir um escopo sem função

    //a memoria cresce de forma decresente
}