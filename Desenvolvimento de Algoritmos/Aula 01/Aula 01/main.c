//linguagem compilada
//não há tipo dinamico de variavel, é estatico
//variaveis = int, float, char, double
/*unsigned long long int idade;
// dobra o lado, pois é negativo e positvio
//long dobra em cima do dobro

//string em c de 9 letras
char x[10];

//retono da função
int abc(){
    return 10;
}
int a  = abc();*/
//aspas duplas string, simples é caractere
#include <stdio.h>
#include <locale.h>

//ponto de entrada do programa
int main() {
    /*int x = 10;
    float y = 2.5;

    printf("%d \n%d \n", x, (x*2));
    printf("%.2f\n", y);
    printf("Oi!!!\n"); // \t = espaço
    printf("Hello, World!\n");*/

    setlocale(LC_ALL, "");
    /*float x =0;
    printf("Entre com o valor: ");
    scanf("%f",&x);

    printf("Resultado: %f",(x*2));*/


    /*if(x > 10){
        printf("Resultado: %f",(x*2));
    } else{
        printf("Resultado: %f",(x*3));
    }*/

    float x =0;
    while (1) {

        printf("Entre com o valor: ");
        scanf("%f", &x);

        if (x >= 0 && x <= 10)
            x *= 2;
        else if (x > 10 && x < 100)
            x *= 3;

        printf("Resultado: %.2f\n", x);
    }

    //y = (x==10)?30:20;

    return 0;
}