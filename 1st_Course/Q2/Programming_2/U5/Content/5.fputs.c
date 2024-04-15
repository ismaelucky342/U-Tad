#include <stdio.h>

int main(int argc, char argv[])
{
    FILE *fichDesc; 

    fichDesc = fopen("letras.txt", "w");
    fputs("Hola mundo", fichDesc);
    fclose(fichDesc);

   return(0);
}