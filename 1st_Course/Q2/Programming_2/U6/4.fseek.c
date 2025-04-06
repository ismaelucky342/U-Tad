#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE * f;
    f = fopen("filename.txt","r");
    char c1 = getc(f);

    printf("1- El caracter actual del fichero es (byte numero): %c \n",c1);
    // ahora invocamos fseek para movernos al septimo caracter desde el inicio
    fseek(f,7,SEEK_SET);
    // repetimos el mismo codigo anterior
    char c2 = getc(f);
    printf("2- El caracter actual del fichero es (byte numero): %c \n",c2);

    return 0;
}