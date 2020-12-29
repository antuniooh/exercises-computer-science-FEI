#include <stdio.h>
#include <string.h>

void concatenar(char *s1, char* s2){
    int i, j;
    for (i= 0; s1[i] !=0; i++) ;

    for (j = 0; s2[j] != 0; j++) {
        s1[i+j] = s2[j];
        //i++;
    }
    s1[i+j] = 0;
}

int main() {
    char s1[1000] = "2 4 5";
    char s2[1000] = "DEFGH";

   // concatenar(s1,s2);

   /* strcat(s1,s2); // concatena
    strncat(s1,s2, 2); // numero de letras que eu desejo concatenar

    int * i = strstr(s2, "GH"); // encontrar a posição de onde acontece (retorna ponteiro)
    printf("%s\n", i);

    int  t = strlen(s2); // retorna o tamanho
    printf("%d\n", t);

    strcpy(s1, s2); // destino e origem
    strncpy(s1, s2, 2);*/


   //sprintf(s1 , "%d %s %f", 2, "JJJJK", 0.5); // será mandado para dentro da string
   //sprintf(s1 , "%s\n%s", s1, s2);

   int x;
   sscanf(s1, " %d", &x); // ler o primeiro numero - %*d (ignora)
    printf("%d\n", x);




    printf("%s\n", s1);


    return 0;
}