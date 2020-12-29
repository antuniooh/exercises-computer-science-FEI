#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <math.h>

float * entraDadosUsuario(int *pn){
    puts("Quantos Numeros?");
    scanf("%d",&pn);
    //*pn = num (numero inteiro criado na hora)

    float *v = malloc(sizeof(int)* *pn);

    for (int i = 0; i < *pn; ++i) {
        scanf("%f\n",&v[i]);
        //scanf("%f\n",v+i);
    }

    return v;
}

float calcDesvio(float *a, int b){
    int i;
    float media=0;
    for (i = 0; i < b; ++i) {
        media+=a[i];
    }
    media/=b;

    float dp=0;
    for (i = 0;i  <b ; i++) {
        dp += pow(a[i]-media,2);
    }
    dp/=b;
    dp=sqrt(dp);
    return dp;

}

int main() {
    int n;
    float *v = entraDadosUsuario(&n);
    float desvio = calcDesvio(v, n);
    printf("%f\n",desvio);

    //system("ipconfig")

    return 0;
}