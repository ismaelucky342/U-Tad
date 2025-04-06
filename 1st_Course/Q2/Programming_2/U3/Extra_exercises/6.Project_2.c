#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM_BLOQUE 10

// Función para leer una línea de manera dinámica
char *leeLineaDinamica(int *TamLinea);

int main(int argc, char *argv[]) {
    char *nombre = NULL;
    char **ListaNombres = NULL;
    int NumeroAlumnos = 0, i = 0, j = 0, TamanioLinea = 0, TamanioLineaTotal = 0;

    printf("¿Cuántos alumnos hay en la clase?\n");
    scanf("%d", &NumeroAlumnos);
    while (getchar() != '\n');

    // Primera reserva para guardar todos los punteros a los nombres
    ListaNombres = (char **)malloc(NumeroAlumnos * sizeof(char *));
    for (i = 0; i < NumeroAlumnos; i++) {
        printf("Introduce un nombre:\n");
        nombre = leeLineaDinamica(&TamanioLinea);
        printf("El nombre es: %s\n", nombre);
        TamanioLineaTotal += TamanioLinea;

        // Segunda reserva para cada nombre
        ListaNombres[i] = (char *)malloc(TamanioLinea);
        j = 0;
        do {
            ListaNombres[i][j] = nombre[j];
            j++;
        } while (nombre[j] != '\0');
        ListaNombres[i][j] = '\0';
    }

    for (i = 0; i < NumeroAlumnos; i++) {
        printf("El nombre [%d] es: %s\n", i, ListaNombres[i]);
    }

    // Liberar memoria
    for (i = 0; i < NumeroAlumnos; i++) {
        free(ListaNombres[i]);
    }
    free(ListaNombres);

    return 0;
}

// Función para leer una línea de manera dinámica
char *leeLineaDinamica(int *TamLinea) {
    int tamBuffer = TAM_BLOQUE;
    char *linea = (char *)malloc(TAM_BLOQUE);
    int numCaracteres = 0;
    char c = 0;

    c = getchar();
    while (c != '\n') {
        linea[numCaracteres] = c;
        numCaracteres++;

        if (numCaracteres == tamBuffer) {
            tamBuffer += TAM_BLOQUE;
            linea = (char *)realloc(linea, tamBuffer);
        }

        c = getchar();
    }

    linea[numCaracteres] = '\0';
    *TamLinea = tamBuffer;
    return linea;
}
