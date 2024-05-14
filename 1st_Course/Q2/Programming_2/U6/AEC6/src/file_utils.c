#include "file_utils.h"

int contarLineas(FILE *archivo) {
    int contador = 0;
    char caracter;

    while ((caracter = fgetc(archivo)) != EOF) {
        if (caracter == '\n') {
            contador++;
        }
    }

    return contador;
}
