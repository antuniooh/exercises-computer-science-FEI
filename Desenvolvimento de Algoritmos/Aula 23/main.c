#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct Ponto{
    int x;
    int y;
};
int retorna2(){
    return 2;
}
int retorna3(){
    return 3;
}

int comparaX(struct Ponto* a, struct Ponto* b, int (*pfn)()){
    return a->x == b->x*pfn();
}
int comparaY(struct Ponto* a, struct Ponto* b, int (*pfn)()){
    return a->y == b->y*pfn();
}

int comparaLonge(struct Ponto a, struct Ponto b){
    return 0;
}

int busca( struct Ponto *v, int n, struct Ponto k, int (*pRegra) (struct Ponto*, struct Ponto*,int(*pfn)() ), int(*pfnFora)()){
    int i;
    for(i=0; i < n; i++){
        if(pRegra(&v[i], &k, pfnFora) == 1){
            return i;
        }
    }
    return -1;
}



int main(int argc, char **argv){

    struct Ponto v[] = {{1,1},{6,5},{4,0},{1,2},{7,4},{8,8}};
    struct Ponto b = {1,0};
    int idx1 = busca(v,6,b, comparaX, retorna2);
    int idx2 = busca(v,6,b, comparaY, retorna3);

    printf("%d\n", idx1);
    printf("%d\n", idx2);


    return 0;
}