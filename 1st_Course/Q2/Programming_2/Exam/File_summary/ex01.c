#include <stdio.h>

int main() {
    FILE *origen = fopen("origen.txt", "r"); //open read 
    if (origen == NULL) {
        printf("No se pudo abrir el archivo de origen\n");
        return 1;
    }

    FILE *destino = fopen("destino.txt", "w"); //open write in destination
    if (destino == NULL) {
        printf("No se pudo abrir el archivo de destino\n");
        fclose(origen);
        return 1;
    }

    int ch;
    while ((ch = fgetc(origen)) != EOF) { //copy char by char to destination
        fputc(ch, destino);
    }

    fclose(origen); //close all
    fclose(destino);
    return 0;
}
