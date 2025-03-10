/*Ejercicio: Escribe una función que reciba dos números y devuelva su suma*/
#include <stdio.h>

int sumar(int a, int b) {
    return a + b;
}

int main() {
    int x, y;
    
    printf("Ingrese dos números: ");
    scanf("%d %d", &x, &y);

    printf("La suma es: %d\n", sumar(x, y));

    return 0;
}
