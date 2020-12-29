#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float distancia(float x1, float y1, float x2, float y2){
    float s=0;
    s += (y2-y1)*(y2-y1);
    s += (x2-x1)*(x2-x1);
    return sqrt(s);
}

void preenchePontos(float *x, float *y, int n){
    int i;
    for(i=0; i<n;i++){
        printf("Insira o ponto %d:\n", i+1);
        scanf("%f", x+i);
        scanf("%f", y+i);
    }
}

void imprimePontos(float *x, float *y, int n){
    int i;
    for(i=0; i<n;i++){
        printf("Ponto %d: (%.2f, %.2f) \n",
               i+1, x[i], y[i]);
        //i+1, *(x +i), *(y+i));
    }
}


int maisProximo(float *xs, float* ys,
                int n, float xrel, float yrel){

    int idx = 0;
    float dist_idx = distancia(xs[0],ys[0], xrel, yrel);
    int i=0;
    for(i=0; i < n;i++ ){
        float dist = distancia(xs[i],ys[i], xrel, yrel);
        if( dist < dist_idx  ){
            dist_idx = dist;
            idx = i;
        }
    }
    return idx;
}

int main() {
    int n;
    puts("quantos pontos? ");
    scanf("%d", &n);
    float *xs = malloc(sizeof(float) * n);
    float *ys = malloc(sizeof(float) * n);
    preenchePontos(xs, ys, n);
    int pos = maisProximo(xs, ys, n, 0,0);
    imprimePontos(xs, ys, n);
    printf("mais proximo da origem %d\n", pos);
/*
    float d = distancia(3,4,0,0);
    printf("%.2f\n", d );
*/
    free(xs);
    free(ys);
    return 0;
}