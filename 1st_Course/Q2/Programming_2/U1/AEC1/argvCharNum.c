#include<stdio.h>

int main(int argc, char *argv[])
{
    int  i = argc;
    char aux = **argv; 

    for(i = 0;  i <= argc -1 ; i++) {
        printf("arg %d: %s\n", i , argv[i]);
    }    
   return 0;
}