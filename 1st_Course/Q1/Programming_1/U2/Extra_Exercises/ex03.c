/*Ejercicio: Escribe un programa que lea dos números enteros y muestre su suma, resta, multiplicación y división*/
#include <stdio.h>

int main() {
    int a, b;
    
    printf("Ingrese el primer número: ");
    scanf("%d", &a);
    printf("Ingrese el segundo número: ");
    scanf("%d", &b);

    printf("Suma: %d\n", a + b);
    printf("Resta: %d\n", a - b);
    printf("Multiplicación: %d\n", a * b);
    
    if (b != 0) {
        printf("División: %.2f\n", (float)a / b);
    } else {
        printf("Error: No se puede dividir por cero.\n");
    }

    return 0;
}
