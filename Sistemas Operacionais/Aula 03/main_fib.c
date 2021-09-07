#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale.h>
#include <time.h>

int fib(int n)                             
  {                                          
    if (n <= 1) return n;                                 
    else return fib(n - 1) + fib(n - 2);                             
}   

int main() {

    int n;
    n = 10;
    printf("\nSérie de Fibonacci:\n\n");

    printf("Iniciando\n");
    struct timespec tis;
    timespec_get(&tis, TIME_UTC);
    char buff[100];
    strftime(buff, sizeof buff, "%D %T", gmtime(&tis.tv_sec));
    printf("Current time: %s.%09ld UTC\n", buff, tis.tv_nsec);
    printf("%d\n", fib(n));

    printf("Saindo!\n");
    struct timespec tis_fn;
    timespec_get(&tis_fn, TIME_UTC);
    strftime(buff, sizeof buff, "%D %T", gmtime(&tis_fn.tv_sec));
    printf("Current time: %s.%09ld UTC\n", buff, tis_fn.tv_nsec);
    printf("Diff time: %09ld UTC\n", (tis_fn.tv_nsec - tis.tv_nsec));

}