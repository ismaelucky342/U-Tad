/*Ejercicio: Escribe un programa que pida un número y diga si es par o impar*/
#include <stdio.h>

int main() {
    int num;

    printf("Ingrese un número: ");
    scanf("%d", &num);

    if (num % 2 == 0) {
        printf("El número es par.\n");
    } else {
        printf("El número es impar.\n");
    }

    return 0;
}
