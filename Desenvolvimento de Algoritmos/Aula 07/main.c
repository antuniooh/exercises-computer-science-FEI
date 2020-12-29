#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//Calcular o desvio padrao de n números
float * entraDadosUsuario(int *pn){
    puts("Quantos Numeros?");
    scanf("%d", &pn);
    float * v = malloc(sizeof(float) * *pn);

    int i;
    for(i=0; i< *pn; i++){
        scanf("%f", &v[i] );
    }
    return v;
}

float calcDesvio(float* a, int b){
    int i;
    float media = 0;
    for(i=0; i<b; i++)
        media += a[i];
    media /= b;

    float dp = 0;
    for(i=0; i<b; i++)
        dp += pow(a[i]-media, 2);
    dp /= b;
    dp = sqrt(dp);
    return dp;
}

int main() {
    int n;
    float *v = entraDadosUsuario(&n);
    float desvio = calcDesvio(v, n);
    printf("%f\n", desvio);

    free(v);
    return 0;
}