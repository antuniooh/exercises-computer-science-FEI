#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <locale.h>

struct Disciplina{
    char nomeDisc[40];
    char nomeProf[40];
};


struct Aluno{
    char nome[40];
    char RA[20];
    float N1;
    float N2;
    struct Disciplina* disc;
};

float calcMedia(struct Aluno a){
    return a.N1*0.4 + a.N2*0.6;
}
float notaNecessaria(struct Aluno a){
    float N3_N2 = (5.0 -0.4*a.N1)/0.6;
    float N3_N1 = (5.0 -0.6*a.N2)/0.4;

    if(N3_N1 < N3_N2)
        return N3_N1;
    else
        return N3_N2;

}
void imprimeDisciplina(struct Disciplina d){
    puts("Disciplina");
    printf("Nome: %s\n", d.nomeDisc);
    printf("Nome Prof: %s\n", d.nomeProf);

}

void imprimeAluno(struct Aluno a){
    puts("\nInformacoes");
    printf("Nome: %s\n", a.nome);
    printf("RA: %s\n", a.RA);
    printf("N1: %.1f\n", a.N1);
    printf("N2: %.1f\n", a.N2);
    imprimeDisciplina(*a.disc);
    if(calcMedia(a) >=5){
        puts("Aprovado");
        printf("Media: %.1f\n", calcMedia(a));
    } else{
        puts(":(");
        printf("Media Necessaria: %.1f\n", notaNecessaria(a));
    }

}

int main(int argc, char *argv[]){
    struct Aluno a1;
    strcpy(a1.nome, "Antonio Gustavo");
    strcpy(a1.RA, "22119001-0");
    a1.N1 = 0;
    a1.N2 = 5.6;

    struct Aluno a2;
    strcpy(a2.nome, "Julio Gustavo");
    strcpy(a2.RA, "22119001-0");
    a2.N1 = 10;
    a2.N2 = 5.6;

    struct Disciplina d1;
    strcpy(d1.nomeProf, "Toninho");
    strcpy(d1.nomeDisc, "Teoria dos Grafos");

    struct Disciplina d2;
    strcpy(d2.nomeProf, "Silmara");
    strcpy(d2.nomeDisc, "Calculo");

    a1.disc = &d1;
    a2.disc = &d2;

   strcpy(a1.disc->nomeDisc, "Mudou o Nome");

    imprimeAluno(a2);
    imprimeAluno(a1);



    return 0;
}
