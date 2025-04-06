#include <stdio.h>

#define NUM_FILAS 4
#define NUM_COLUMNAS 4

int esElementoPico(int matriz[][NUM_COLUMNAS], int f, int c) {
    int valor = matriz[f][c];

    // Check above
    if (f > 0 && matriz[f - 1][c] >= valor) {
        return 0;
    }
    // Check below
    if (f < NUM_FILAS - 1 && matriz[f + 1][c] >= valor) {
        return 0;
    }
    // Check left
    if (c > 0 && matriz[f][c - 1] >= valor) {
        return 0;
    }
    // Check right
    if (c < NUM_COLUMNAS - 1 && matriz[f][c + 1] >= valor) {
        return 0;
    }

    return 1; // It's a peak element
}

void imprimePico(int matriz[][NUM_COLUMNAS], int filas, int columnas) {
    printf("Elementos pico:\n");
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            if (esElementoPico(matriz, i, j)) {
                printf("Elemento pico en [%d][%d]: %d\n", i, j, matriz[i][j]);
            }
        }
    }
}

int main() {
    int matriz[NUM_FILAS][NUM_COLUMNAS] = {
        {10, 20, 15, 2},
        {21, 30, 14, 3},
        {7, 16, 32, 4},
        {5, 6, 8, 1}
    };

    imprimePico(matriz, NUM_FILAS, NUM_COLUMNAS);

    return 0;
}
