#include <stdio.h>

#define NUM_FILAS 3
#define NUM_COLUMNAS 4

void transponeMatriz(int original[][NUM_COLUMNAS], int transpuesta[][NUM_FILAS]);
void imprimeMatriz(int filas, int columnas, int matriz[][columnas]);

void transponeMatriz(int original[][NUM_COLUMNAS], int transpuesta[][NUM_FILAS]) {
    for (int i = 0; i < NUM_FILAS; i++) {
        for (int j = 0; j < NUM_COLUMNAS; j++) {
            transpuesta[j][i] = original[i][j];
        }
    }
}

void imprimeMatriz(int filas, int columnas, int matriz[][columnas]) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int original[NUM_FILAS][NUM_COLUMNAS] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int transpuesta[NUM_COLUMNAS][NUM_FILAS];

    printf("Matriz original:\n");
    imprimeMatriz(NUM_FILAS, NUM_COLUMNAS, original);

    transponeMatriz(original, transpuesta);

    printf("\nMatriz transpuesta:\n");
    imprimeMatriz(NUM_COLUMNAS, NUM_FILAS, transpuesta);

    return 0;
}