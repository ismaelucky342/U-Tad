/*Ejercicio: Escribe un programa que imprima los números del 1 al 10 usando un while y luego con un for*/
#include <stdio.h>

int main() {
    int i = 1;

    printf("Usando while:\n");
    while (i <= 10) {
        printf("%d ", i);
        i++;
    }
    printf("\n");

    printf("Usando for:\n");
    for (i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    printf("\n");

    return 0;
}
