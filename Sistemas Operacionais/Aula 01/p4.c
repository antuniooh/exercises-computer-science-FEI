#include <stdlib.h>
#include <stdio.h>

int v1;

int main(){
    int v2;
    int *v3 = malloc(sizeof(int));

    v3[100] = 4;

    return 0;
}