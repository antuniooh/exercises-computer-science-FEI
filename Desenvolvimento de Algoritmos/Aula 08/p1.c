#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

        int i;
        float ** m =malloc(sizeof(float*) * 7);
        for (i = 0; i < 7; ++i) {
            m[i] = malloc(sizeof(float)*4);
        }

        int j;
        int x = 1;
        for (i = 0; i < 7; ++i) {
            for (j = 0; j < 4; ++j) {
                m[i][j] = x++;
            }
        }


        for (i = 0; i < 7; ++i) {
            for (j = 0; j < 4; ++j) {
                printf("%-6.1f  ", m[i][j]);
            }
            puts("");
        }


        for (i = 0; i < 7; ++i) {
            free(m[i]);
        }
        free(m);    

}
