#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

double saldo;

void deposito(double valor)
{
  saldo += valor;
}

void saque(double valor)
{
  saldo -= valor;
}

void* muitos_depositos(void *args)
{
  size_t i;
  for(i=0;i<100000000;i++) {
    deposito(1.5);
  }
}

void* muitos_saques(void *args)
{
  size_t i;
  for(i=0;i<100000000;i++) {
    saque(1.0);
  }
}


int main()
{
  // Diversos depositos e saques - sem threads
  saldo = 0;
  muitos_depositos(NULL);
  muitos_saques(NULL);
  printf("Saldo final (sem threads)  : %lf\n", saldo);
 
  // Diversos depositos e saques com threads
  saldo = 0;
  pthread_t t1, t2;
  pthread_create(&t1, NULL, muitos_depositos, NULL);
  pthread_join(t1, NULL);

  pthread_create(&t2, NULL, muitos_saques, NULL);
  pthread_join(t2, NULL);
  printf("Saldo final (sync  threads): %lf\n", saldo);

  // Diversos depositos e saques - ao mesmo tempo!!!
  saldo = 0;
  pthread_create(&t1, NULL, muitos_depositos, NULL);
  pthread_create(&t2, NULL, muitos_saques, NULL);
  pthread_join(t1, NULL);
  pthread_join(t2, NULL);
  printf("Saldo final (*com* threads): %lf\n", saldo);
  
  return 0;
}
