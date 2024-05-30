#include<stdio.h>

#include <stdio.h>

int main() {
    FILE *file = fopen("archivo.txt", "w"); // open file for write
    if (file == NULL) {
        printf("No se pudo abrir el archivo\n");
        return 1;
    }

    fputs("Hola, mundo!\n", file); //write 

    fclose(file);
    return 0;
}


