#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid;
    int status;

    printf("Eu sou o processo pai: meu PID = %d\n", getpid());

    if ((pid = fork()) < 0) {
        printf("O PID do filho = %d\n", pid);
        perror("fork");
        exit(1);
    }

    if (pid == 0)
        exit(0);

    printf("O PID do filho = %d\n", pid);
    sleep(10);

    while(1){

    }

    return 0;
}