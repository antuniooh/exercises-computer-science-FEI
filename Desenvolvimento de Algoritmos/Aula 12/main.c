#include <stdio.h>

int fat (int i){
    if(i == 0 || i == 1)
        return 1;
    return i*fat(i-1);
}

void contagem (int i){
    if(i == 0) {
        printf("%d\n", 0);
        return;
    }
    printf("%d\n", i);
    contagem(i-1);
    //printf("%d\n", i); recursividade de ida e volta

}


int main() {
    //int x = fat(5);
    //printf("%d\n", x);

    //recurssão pode estourar  a memoria

    contagem(10);

    return 0;
}