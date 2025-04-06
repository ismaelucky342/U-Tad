#include <stdio.h>
#include <stdlib.h>

int b = 15; 
int *c = NULL; 

void main(int argc, char *argv[])
{
    c = (int *)malloc(40); 
    if (c == NULL){
        printf("Memory allocation failed!\n");
    }else{
        int a = 10; 
        for (b = 0; b < a; b++){
            c[b] = b ; 
        }
        int *pc = c; 
        for(b = 0; b < a; b++, pc++){
            printf("%d ", *pc);
            printf("%d ", c[b]);
            printf("%d ", *(c+b));
        }
    }
    free(c);
}