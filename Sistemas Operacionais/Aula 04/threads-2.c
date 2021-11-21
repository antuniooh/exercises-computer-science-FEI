#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void *funcao(void *args)
{
  unsigned long int i;
  int a=(int)args;
  printf("Iniciando contagem na thread %d...\n", a);
  for(i=0; i<10000000000; i++) {
    a += i;
  }
  a -= (i*2/100);
  printf("Saindo da thread com %d!\n", a);
  pthread_exit((void*)a);
}

#define QTDE 7

int main(int argc, char* argv[])
{
  pthread_t ts[QTDE];
  int i;

  for(i=0;i<QTDE;i++) {
    printf("Criando T%d\n", i+1);
    pthread_create(&ts[i], NULL, funcao, (void *)i); // cria 1 thread
  }

  printf("Dormindo...\n");
  sleep(5); // dormir

  printf("Juntando tudo...\n");
  int resultado;
  for(i=0;i<QTDE;i++) {
    pthread_join(ts[i], &resultado);
    printf("Resultado de T%d: %d\n",i+1, resultado);
  }

  printf("Saindo!\n");
  pthread_exit(NULL);
  return 0;
}

