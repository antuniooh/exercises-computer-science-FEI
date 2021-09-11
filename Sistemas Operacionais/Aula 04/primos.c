#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct
{
    int start;
    int end;
} Primos;

int valor = 29;
int resultado = 0;

void *primo(void *args)
{
    Primos* scope = (Primos*) args;

    for (int i = scope->start; i <= scope->end; i++){
        if(valor%i == 0){
            resultado+=1;
        }
    }
}


int main()
{
    pthread_t t1, t2;
    int first = (int)(valor/4);
    int second = (int)(valor/2);

    Primos part1 = {2, first};
    Primos part2 = {first, second};



    pthread_create(&t1, NULL, primo, &part1);
    pthread_create(&t2, NULL, primo, &part2);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    if (resultado == 0){
        printf("o NÚMERO É PRIMO: %d\n", valor);
    } else{
        printf("o NÚMERO NÃO É PRIMO: %d\n", valor);
    }

    return 0;
}
