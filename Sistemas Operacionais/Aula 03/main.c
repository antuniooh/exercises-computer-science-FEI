#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

int fib(int n)
{
  if (n <= 1)
    return n;
  return fib(n-1) + fib(n-2);
}

void *runner(void *n){
	pthread_exit(fib((int)n));
}


int main(int argc, char* argv[])
{
  pthread_t ts;
  pthread_t ts2;
  int i=11;

  printf("Iniciando\n");
  struct timespec tis;
  timespec_get(&tis, TIME_UTC);
  char buff[100];
  strftime(buff, sizeof buff, "%D %T", gmtime(&tis.tv_sec));
  printf("Current time: %s.%09ld UTC\n", buff, tis.tv_nsec);

  printf("Starting of the program...\n");
  pthread_create(&ts, NULL, runner, (void *)i-1); // cria 1 thread
  pthread_create(&ts2, NULL, runner, (void *)i-2); // cria 1 thread

  printf("Juntando tudo...\n");
  int resultado, resultado2;
  pthread_join(ts, &resultado);
  printf("Resultado de fibonacci de %d: %d\n", 10, resultado);

  printf("Saindo!\n");
  struct timespec tis_fn;
  timespec_get(&tis_fn, TIME_UTC);
  strftime(buff, sizeof buff, "%D %T", gmtime(&tis_fn.tv_sec));
  printf("Current time: %s.%09ld UTC\n", buff, tis_fn.tv_nsec);
  printf("Diff time: %09ld UTC\n", (tis_fn.tv_nsec - tis.tv_nsec));

  pthread_exit(NULL);
  return 0;
}
