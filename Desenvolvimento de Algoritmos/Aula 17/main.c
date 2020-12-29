#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale.h>


struct sPonto{
    float r;
    float i;
};

void leiaPonto(struct sPonto *p){
    printf("Digite o valor da parte real:\n ");
    scanf("%f", &((*p).r));
    printf("Digite o valor da parte imaginaria:\n ");
    scanf("%f", &((*p).i ) );
    printf("%f + (%f)i\n", (*p).r, p->i);
}

void imprimePonto( struct sPonto p){
    printf("%f + (%f)i\n", (p).r, p.i);
}

struct sPonto adicao( struct sPonto p, struct sPonto q ){
    struct sPonto ret;
    ret.r = p.r + q.r;
    ret.i = p.i + q.i;
    return ret;
}
struct sPonto multiplicacao( struct sPonto p, struct sPonto q ){
    struct sPonto ret;
    ret.r = (p.r * q.r) - (p.i* q.i) ;
    ret.i = (p.r * q.i) + (p.i * q.r);
    return ret;
}
struct sPonto divisao( struct sPonto p, struct sPonto q ){
    struct sPonto ret;
    ret.r = ((p.r * q.r) + (p.i* q.i))/(((q.r)*(q.r)) + ((q.i)*(q.i))) ;
    ret.i = ((p.i * q.r) - (p.r * q.i))/(((q.r)*(q.r)) + ((q.i)*(q.i)));
    return ret;
}

void modulo(struct sPonto p){
    float res;
    res = sqrt(pow(p.r, 2) + pow(p.i, 2));
    printf("O modulo e: %f\n",res);
}
void argumento(struct sPonto p){
    float res;
    res = (p.r)/(p.i);
    printf("O argumento e o arcTg: %f\n",res);
}
struct sPonto conjugado( struct sPonto p) {
    struct sPonto ret;
    ret.r = p.r;
    ret.i = -p.i;
    return ret;
};

/*struct sPonto
prodfrac( struct sPonto p, struct sPonto q ){
    struct sPonto ret;
    ret.n = (p.n)*(q.n);
    ret.d = (p.d)*(q.d);
    return ret;
}*/

int menu(){
    int op;
    puts("====================");
    puts("1 - Adicao");
    puts("2 - Multiplicacao");
    puts("3 - Divisao");
    puts("4 - Modulo z1");
    puts("5 - Modulo z2");
    puts("6 - Argumento z1");
    puts("7 - Argumento z2");
    puts("8 - Conjugado z1");
    puts("9 - Conjugado z2");
    printf("Opcao > ");
    scanf(" %d", &op);
    return op;

}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL, "Portuguese");

    struct sPonto p1;
    struct sPonto p2;

    int op;

    printf("Números Complexos: \n\n");

    leiaPonto( &p1 );
    leiaPonto( &p2 );

    op = menu();
    while(1) {
        if (op == 1) {
            imprimePonto(adicao(p1, p2));
            op = menu();
        } else if (op == 2) {
            imprimePonto(multiplicacao(p1, p2));
            op = menu();
        } else if (op == 3) {
            imprimePonto(divisao(p1, p2));
            op = menu();
        } else if (op == 4) {
            modulo(p1);
            op = menu();
        } else if (op == 5) {
            modulo(p2);
            op = menu();
        } else if (op == 6) {
            argumento(p1);
            op = menu();
        } else if (op == 7) {
            argumento(p2);
            op = menu();
        } else if (op == 8) {
            imprimePonto(conjugado(p1));
            op = menu();
        } else if (op == 9) {
            imprimePonto(conjugado(p2));
            op = menu();
        } else {
            puts("Valor invalido, fechando o sistema...");
            break;
        }
    }
    system("pause");

    return 0;
}
