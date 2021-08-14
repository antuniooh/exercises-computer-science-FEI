#include <stdlib.h>
#include <stdio.h>

int main(){
    int *s1;

    while(1){
        s1 = (int *) malloc (sizeof(int) * 100000000);
        printf("%p\n", (void*) s1);
    }

    return 0;
}