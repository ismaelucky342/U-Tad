#include <stdio.h>

#define NUM_COLUMNAS 5

int numeroMasFrecuente(int matriz[][NUM_COLUMNAS], int n_filas);

int main() {
    int matriz[3][NUM_COLUMNAS] = {
        {1, 2, 3, 4, 5},
        {5, 1, 2, 3, 4},
        {3, 4, 5, 1, 2}
    };

    int n_filas = 3;
    int resultado = numeroMasFrecuente(matriz, n_filas);

    printf("El número más frecuente en la matriz es: %d\n", resultado);

    return 0;
}

int numeroMasFrecuente(int matriz[][NUM_COLUMNAS], int n_filas) {
    int frecuencia[101] = {0}; // Suponiendo que los números están en el rango 0-100
    int max_frecuencia = 0;
    int numero_frecuente = 0;

    for (int i = 0; i < n_filas; i++) {
        for (int j = 0; j < NUM_COLUMNAS; j++) {
            int num = matriz[i][j];
            frecuencia[num]++;
            if (frecuencia[num] > max_frecuencia) {
                max_frecuencia = frecuencia[num];
                numero_frecuente = num;
            }
        }
    }

    return numero_frecuente;
}
