#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void *funcao(void *args)
{
  unsigned long int i;
  int a=0;
  printf("Iniciando contagem na thread...\n");
  for(i=0; i<10000000000; i++) {
    a += i;
  }
  a -= (i*2/100);
  printf("Saindo da thread!\n");
  pthread_exit(NULL);
}

int main(int argc, char* argv[])
{
  pthread_t t1, t2;

  printf("Criando T1\n");
  pthread_create(&t1, NULL, funcao, NULL); // cria 1 thread

  printf("Criando T2\n");
  pthread_create(&t2, NULL, funcao, NULL); // cria 1 thread

  printf("Dormindo...\n");
  sleep(5); // dormir

  printf("Juntando tudo...\n");
  pthread_join(t1, NULL);
  pthread_join(t2, NULL);

  printf("Saindo da main!\n");
  pthread_exit(NULL);
}

