/*Ejercicio: Escribe un programa que almacene 5 números en un arreglo y los imprima.*/
#include <stdio.h>

int main() {
    int numeros[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 5; i++) {
        printf("Número %d: %d\n", i + 1, numeros[i]);
    }

    return 0;
}
