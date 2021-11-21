#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct
{
    int start;
    int end;
} Primos;

int limite = 100;
int valor = 1;
int resultado = 0;

void *primo(void *args)
{
    Primos *scope = (Primos *)args;

    for (int i = scope->start; i < scope->end; i++)
    {
        if (valor % i == 0)
        {
            resultado += 1;
        }
    }
}

int main()
{
    for (; valor <= limite; valor++)
    {
        if (valor < 5)
        {
            resultado = (valor == 4) ? 2 : 1;
        }
        else
        {
            pthread_t t1, t2;
            int first = (int)(valor / 4);
            int second = (int)(valor / 2);

            Primos part1 = {1, first};
            Primos part2 = {first, second};

            pthread_create(&t1, NULL, primo, &part1);
            pthread_create(&t2, NULL, primo, &part2);
            pthread_join(t1, NULL);
            pthread_join(t2, NULL);
        }

        if (resultado == 1)
        {
            printf("o NÚMERO É PRIMO: %d\n", valor);
        }
        resultado = 0;
    }
    return 0;
}
