#include <stdio.h>

#define NUM_COLUMNAS 3

int filaMayorSuma(int matriz[][NUM_COLUMNAS], int n_filas) {
    int max_suma = 0;
    int fila_max = 0;

    for (int i = 0; i < n_filas; i++) {
        int suma = 0;
        for (int j = 0; j < NUM_COLUMNAS; j++) {
            suma += matriz[i][j];
        }
        if (suma > max_suma) {
            max_suma = suma;
            fila_max = i;
        }
    }

    printf("La fila con mayor suma es la fila %d con una suma de %d.\n", fila_max, max_suma);
    return fila_max;
}

int main() {
    int matriz[][NUM_COLUMNAS] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int n_filas = sizeof(matriz) / sizeof(matriz[0]);

    filaMayorSuma(matriz, n_filas);

    return 0;
}