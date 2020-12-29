#include <stdio.h>
//uso de . para divisão de valores inteiros

int soma(int a, int b){
    return (a+b);
}
//função sem retorno
void digaoi(int N){
    for (int i = 0; i < N; i++)
        if (N < 2) {
            break;
            //return 1;//ele também sai da função
        }else {
            printf("Ola\n");
        }

};
//declaração de função é diferene de implementação
int sub(int, int);
//é possivel implemnetar dpos do main, desde que tenha sido declarado

void zeraInt(int* x){
    *x=0; //não altera o valor original, apenas nesse escopo, pois o valor é copiado
}

void troca(int* x, int* y){
    int temp =*x;
    *x = *y;
    *y = temp;
}
int menor(int x , int y){
   if(x < y){
       return x;
   } else if( x > y){
       return y;
   }
}

int main() {
   /* printf("Hello, World!\n");

    int x = soma(1,2);
    int a = soma(soma(1,2),2);
    printf("%d\n",x);
    digaoi(50);
   int z =10;
   zeraInt(&z);
   printf("%d\n",z);*/

   /*int a =55;
   int b = 2;

   troca(&a, &b);

   printf("A= %d B= %d\n", a, b);*/


   int a =10;
   int b =50;
   int resp = menor(a, b);
   printf("%d\n",resp);

   return 0;

    //[tipo do retorno] [nome função] ([tipo e nome paramtros])


}