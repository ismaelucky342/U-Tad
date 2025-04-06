#include <stdio.h>

#define NUM_FILAS 4
#define NUM_COLUMNAS 4

void rellenaEspiral(int matriz[][NUM_COLUMNAS], int n_filas, int n_columnas) {
    int valor = 1;
    int inicioFila = 0, finFila = n_filas - 1;
    int inicioColumna = 0, finColumna = n_columnas - 1;

    while (inicioFila <= finFila && inicioColumna <= finColumna) {
        for (int i = inicioColumna; i <= finColumna; i++) {
            matriz[inicioFila][i] = valor++;
        }
        inicioFila++;

        for (int i = inicioFila; i <= finFila; i++) {
            matriz[i][finColumna] = valor++;
        }
        finColumna--;

        if (inicioFila <= finFila) {
            for (int i = finColumna; i >= inicioColumna; i--) {
                matriz[finFila][i] = valor++;
            }
            finFila--;
        }

        if (inicioColumna <= finColumna) {
            for (int i = finFila; i >= inicioFila; i--) {
                matriz[i][inicioColumna] = valor++;
            }
            inicioColumna++;
        }
    }
}

void imprimeMatriz(int matriz[][NUM_COLUMNAS], int n_filas, int n_columnas) {
    for (int i = 0; i < n_filas; i++) {
        for (int j = 0; j < n_columnas; j++) {
            printf("%3d ", matriz[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int matriz[NUM_FILAS][NUM_COLUMNAS];

    rellenaEspiral(matriz, NUM_FILAS, NUM_COLUMNAS);

    printf("Matriz en forma de espiral:\n");
    imprimeMatriz(matriz, NUM_FILAS, NUM_COLUMNAS);

    return 0;
}