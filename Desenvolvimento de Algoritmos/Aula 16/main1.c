#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <math.h>

struct Data{
    int dia;
    int mes;
    int ano;
};

struct Data criadata(int dia, int mes, int ano){
    struct Data d;
    d.dia = dia;
    d.mes = mes;
    d.ano =ano;
    return d;

}

struct Receita{
    struct Data data;
    float valor;
    char cliente[200];
};

struct Livro{
    struct Receita receita[100];
    int n;
};
int menu(){
    puts("MINHA RIQUEZA");
    puts("=================");
    puts("1 - Insere");
    puts("2 - Remove");
    puts("3 - Imprime");
    puts("Else Sai!");
    int op;
    scanf("%d",&op);
    return op;
}
void tiraEnter(char *s){
    for (int i = 0; s[i] != '\n' ; ++i) {
        s[i] = 0;
    }
}

struct Receita perguntaUsuarioReceita(){
    struct Receita r;

    puts("Entre com os dados da receita: ");
    puts("Valor: ");
    scanf("%f", &(r.valor));
    puts("Data: ");
    scanf("%d %d %d", &(r.data.dia),&(r.data.mes), &(r.data.ano));
    fflush(stdin);//limpa o enter do buffer que foi deixado
    puts("Cliente: ");
    fgets(r.cliente, 200, stdin);
    tiraEnter(r.cliente);
    puts("Obrigado!");

    return r;
}

void cadastraReceita(struct Livro* l){
    struct Receita nova = perguntaUsuarioReceita();
    (*l).receita[(*l).n] = nova;
    (*l).n++;
    //l->receita == (*l).receita
}

void imprimeReceita(struct Receita r){
    puts("Imprimindo receita");
    printf("Nome: %s\n", r.cliente); //vem com o enter do fgets, possivel percorrer a string e tirar o \n
    printf("Valor: %f\n", r.valor);
    printf("Data: %d/%d/%d\n", r.data);

}

void imprimeLivro(struct Livro l) {
    int i;
    for (int i = 0; i < l.n; i++) {
        imprimeReceita(l.receita[i]);
        puts("--------------------");
    }
}

void removeReceita(struct Livro* l){
    puts("Qual posicao");
    int pos;
    scanf("%d", &pos);
    pos--;
    int i;
    for (i = pos; i < l->n - 1; ++i) {
        l->receita[i] =  l->receita[i+1];
    }
    l->n--;
}

int main(){
    struct Livro l;
    l.n = 0;
    while (1){
        int op = menu();

        if (op == 1){
            cadastraReceita(&l);
        }
        else if (op == 2){
            removeReceita(&l);
        }
        else if (op == 3){
            //imprimeReceita(l.receita[0]);
            imprimeLivro(l);
        }
        else {
            break;
        }
    }


  /*struct Receita r[100];
  r[0].data = criadata(2,10,2019);
  r[0].valor = 2500;
*/
    return 0;
}
