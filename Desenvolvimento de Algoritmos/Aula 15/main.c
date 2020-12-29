#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <math.h>

void move_disco(int d, char ori, char dest, char aux){
    if (d==1){
        printf("Mover disco %d de %c para %c \n", d, ori, dest );}
    else{
        move_disco(d-1, ori, aux, dest);
        printf("Mover disco %d de %c para %c \n", d, ori, dest);
        move_disco(d-1, aux, dest, ori);
    }
}
void fibonnaci(int n){
    long long int vetor[n];
    vetor[0] = 1;
    vetor[1] = 1;
    //cria o vetor base
    for (int i = 2; i <= n; i++)
    {
        vetor[i] = ((vetor[i-1]) + (vetor[i-2]));
    }

    for(int a = 0; a <= n-1; a++)
    {
        printf("%lld ",vetor[a] );
    }
    printf("\n");
}
void fibonnaci2(int n){
    int a = 1;
    int b = 1;
    printf("%d ", a);
    printf("%d ", b);

    for (int i = 2; i < n; i++)
    {
        int result = (a) + (b);
        a = b;
        b = result;
        printf("%d ", result);
    }
    printf("\n");
}
int fibonnaci3(int n){
    if(n == 1 || n == 2)
        return 1;
    fibonnaci3(n-1) + fibonnaci3(n-2);
}

struct data{
    int dia;
    char mes[20];
    int ano;
};

struct ponto{
    float x;
    float y;
};

struct reta{
    float a;
    float b;
    float c;
};

void conferirReta(struct reta r1, struct reta r2){
    if(r1.a == r2.a || (r1.a *r2.b) - (r1.b*r2.a) == 0)
        printf("Paralelas");
    else {
       float x = (r1.b - r2.b)/ (r1.a - r2.a);
        float y = (r1.a * x + r1.b);
       printf("Concorrentes no ponto (%f,%f)", x,y);

    }
}

void triangulo(struct ponto p1, struct ponto p2,struct ponto p3){
    float D1 = sqrt((pow((p1.x - p2.x),2) + (pow((p1.y - p2.y),2))));
    float D2 = sqrt((pow((p2.x - p3.x),2) + (pow((p2.y - p3.y),2))));
    float D3 = sqrt((pow((p1.x - p3.x),2) + (pow((p1.y - p3.y),2))));
    float Maior, Soma;

    printf("Lados formados: %.2f %.2f %.2f\n", D1, D2, D3);

    if(D1 > D2 && D1 > D3) {
        Maior = D1;
        Soma = pow(D2,2) + pow(D3,2);
    }
    else if(D3 > D2 && D3 > D1) {
        Maior = D3;
        Soma = pow(D2,2) + pow(D1,2);
    }
    else if(D2 > D1 && D2 > D1) {
        Maior = D2;
        Soma = pow(D1,2) + pow(D3,2);
    }


    if(pow(Maior, 2) == Soma)
        printf("Retangulo\n");
    else if (pow(Maior, 2) > Soma)
        printf("Obtusangulo\n");
    else if(pow(Maior, 2) < Soma)
        printf("Acutangulo\n");

}


int main(){
    /*int discos;
    printf("Digite o numero de discos: \n ");
    scanf("%d", &discos);
    move_disco(discos, 'A', 'C', 'B');
    fibonnaci(4);
    fibonnaci2(6);
    int a = fibonnaci3(6);

       int n, i;

    printf("Digite um numero inteiro positivo: \n" );
    scanf(" %d", &n);


    for(i=1; i<=n; i++)
      printf("0 %d numero de fibonacci eh: %d\n", i, fibonacci(i));


    system("fibonacci");

    return 0;

    }

#include <stdio.h>
#include <stdlib.h>

    /*int main()
    {
        int f0, f1, f2, n, i;
        do
        { printf("Insira um inteiro positivo: \n");
            scanf("%d", &n);
        }
        while ( n <= 2 );
        printf("Os primeiros %d numeros de Fibonacci sao:\n 1, 1", n);

        f0=1; f1=1; i=3;
        do
        { f2=f0+f1;
            printf(", %d", f2);
            f0=f1; f1=f2; i=i+1;
        }
        while ( i <= n );
        printf("\n \n");

        system("fibonacci_do_while");

        return 0;
    }
     */


    /*struct data dia;
    printf("Digite o dia: ");
    scanf(" %d", &dia.dia);
    printf("Digite o mes: ");
    scanf(" %s", &dia.mes);
    printf("Digite o ano: ");
    scanf(" %d", &dia.ano);

    printf("Dia: %d\n", dia.dia);
    printf("Mes: %s\n", dia.mes);
    printf("Ano: %d\n", dia.ano);*/

    /*struct ponto p1;
    struct ponto p2;

    printf("Digite o x do P1: ");
    scanf(" %d", &p1.x);
    printf("Digite o y do P1: ");
    scanf(" %d", &p1.y);
    printf("Digite o x do P2: ");
    scanf(" %d", &p2.x);
    printf("Digite o y do P2: ");
    scanf(" %d", &p2.y);

    printf("A soma em X %d e em Y %d", (p1.x + p2.x),(p1.y + p2.y));*/

    /* Soma Pontos */

   /* struct sPonto{
        float x;
        float y;
    };


    void leiaPonto(struct sPonto *p){
        printf("Digite o valor de x:\n ");
        scanf("%f", &( (*p).x ) );
        printf("Digite o valor de y:\n ");
        scanf("%f", &( (*p).y )  );

    }


    void imprimePonto( struct sPonto p){
        printf("x: %f\n", p.x  );
        printf("y: %f\n", p.y  );
    }



    struct sPonto
    somaPontos( struct sPonto p1, struct sPonto p2, struct sPonto p3 ){
        struct sPonto ret;
        ret.x = p1.x + p2.x + p3.x;
        ret.y = p1.y + p2.y + p3.y;
        return ret;
    }



    int main(int argc, char *argv[])
    {
        struct sPonto p1;
        struct sPonto p2;
        struct sPonto p3;
        struct sPonto p4;

        leiaPonto( &p1 );
        leiaPonto( &p2 );
        leiaPonto( &p3 );
        p4 = somaPontos(p1,p2,p3);
        imprimePonto(p4);*/

   /* struct reta r1;
    struct reta r2;
    printf("Digite o coeficiente angular e linear da R1: ");
    scanf(" %f %f", &r1.a, &r1.b);
    printf("Digite o coeficiente angular e linear da R2: ");
    scanf(" %f %f", &r2.a, &r2.b);

    conferirReta(r1, r2);*/
    /* retas */

   /* struct sReta{
        float a;
        float b;
    };


    void leiaReta(struct sReta *p){
        printf("A equação da reta é y = ax + b\n");
        printf("Digite o valor do coeficiente angular a:\n ");
        scanf("%f", &( (*p).a ) );
        printf("Digite o valor do coeficiente linear b:\n ");
        scanf("%f", &( (*p).b )  );

    }


    void imprimeReta( struct sReta p){
        printf("Coeficiente Angular a: %f\n", p.a  );
        printf("Coeficiente  Linear b: %f\n", p.b  );
    }

    void Retas (struct sReta r, struct sReta s){
        struct sReta t;
        if (r.a==s.a)
            printf("Retas Paralelas. \n");
        else{
            printf("Retas Concorrentes. \n");
            t.a = (r.b-s.b)/(s.a-r.a);
            t.b = ((s.a)*(r.b)-((s.b)*(r.a)))/(s.a-r.a);
            printf("O ponto de intersecção é: (%f, %f)\n", t.a, t.b);

        }*/


    struct ponto p1;
    struct ponto p2;
    struct ponto p3;

    printf("P1: ");
    scanf(" %f %f", &p1.x, &p1.y);
    printf("P2: ");
    scanf(" %f %f", &p2.x, &p2.y);
    printf("P3: ");
    scanf(" %f %f", &p3.x, &p3.y);

    triangulo(p1, p2, p3);

    return 0;
}
