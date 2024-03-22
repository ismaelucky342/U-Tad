#include <stdio.h>
#include <stdlib.h>

int b = 15; 
int *c = NULL; 
int *d = NULL; 

int main()
{
    int a = 15; 
    c = (int *)malloc(40);
    d = (int *)malloc(40);

    for(b = 0; b < a; b++)
    {
        printf("%d", c[b]);
    }
    
    for(b = 0; b < a; b++)
    {
         c[b] = d[b];
    }
    free(c);
    free(d);
    return 0;
}