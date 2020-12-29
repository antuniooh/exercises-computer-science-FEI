#include <stdio.h>
#include <stdlib.h>

/* Soma Fração */

struct sPonto{
    int n;
    int d;
};


void leiaPonto(struct sPonto *p){
    printf("Digite o valor do numerador:\n ");
    scanf("%d", &( (*p).n ) );
    printf("Digite o valor do denominador:\n ");
    scanf("%d", &( (*p).d )  );
    printf("%d/%d\n", (*p).n, p->d);

}

int mmc(struct sPonto p, struct sPonto q){
    int i = 1, a = p.d, b = q.d;
    while (a*i%b != 0){
        i++;
    }
    return a*i;


}

void imprimePonto( struct sPonto p){
    printf("numerador: %d\n", p.n  );
    printf("denominador: %d\n", p.d  );
    printf("%d/%d\n", p.n, p.d);
}


struct sPonto
somafrac( struct sPonto p, struct sPonto q ){
    struct sPonto ret;
    int m = mmc(p, q);
    ret.n = m*(p.n)/(p.d) + m*(q.n)/(q.d); /* a/b + c/d = mmc(b,c)*a/b + mmc(b,c)*c/d */
    ret.d = m;
    return ret;
}

struct sPonto
prodfrac( struct sPonto p, struct sPonto q ){
    struct sPonto ret;
    ret.n = (p.n)*(q.n);
    ret.d = (p.d)*(q.d);
    return ret;
}

int main(int argc, char *argv[])
{
    struct sPonto p1;
    struct sPonto p2;


    printf("Fracoes: \n\n");

    leiaPonto( &p1 );
    leiaPonto( &p2 );

    printf("A soma eh:\n");
    imprimePonto(somafrac(p1,p2));

    printf("=============\n\n");

    printf("O produto eh:\n");
    imprimePonto(prodfrac(p1,p2));


    system("pause");
    return 0;
}
