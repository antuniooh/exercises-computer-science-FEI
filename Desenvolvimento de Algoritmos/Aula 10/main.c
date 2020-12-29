#include <stdio.h>

void CopiaString (char *dest, char *origem){
    int i;
    for (i = 0; origem[i] != 0 ; i++) {
        dest[i] = origem[i];
    }
}
void imprimeString(char* string){
    for (int i = 0; string[i] != 0 ; i++) {
        printf("%c", string[i]);
    }
    printf("\n");

}
void trocaApZ(char *string){
    for (int i = 0; string[i] != 0 ; i++) {
        if(string[i] == 'A'){
            string[i] = 'Z';
        }
        printf("%c", string[i]);
    }
    printf("\n");
}
void trocaMinuscula(char *string){
    for (int i = 0; string[i] != 0 ; i++) {
        if(string[i] >= 97 && string[i] <= 122){
            string[i] = ' ';
        }
        printf("%c", string[i]);
    }
    printf("\n");
}

int main() {
    //%d, "a" = indica o número na tabela asc
    char s[10];

    /*for (int i = 0; s[i] !=0 ; ++i) {
        printf("%c",s[i]);
    }*/

    CopiaString(s,"ABC");
    printf("%s\n", s);
    imprimeString("ABCDEDF");
    CopiaString(s,"ABCDAEF");
    trocaApZ(s);

    char a[100];
    //scanf("%s",s);
    //gets(s);
    fgets(s, 100,stdin);
    //printf("STRING DIGITADA: %s", s);
    trocaMinuscula(s);


    /*for (int i = 0; i < 256; ++i) {
        printf("%d e:  %c\n",i, i);
    }*/

    return 0;
}