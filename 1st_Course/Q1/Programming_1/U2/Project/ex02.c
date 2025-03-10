/*Ejercicio: Escribe un programa que pida al usuario su nombre y edad, y luego los muestre*/
#include <stdio.h>

int main() {
    char nombre[50];
    int edad;

    printf("Ingrese su nombre: ");
    scanf("%s", nombre);
    printf("Ingrese su edad: ");
    scanf("%d", &edad);

    printf("Hola, %s! Tienes %d años.\n", nombre, edad);

    return 0;
}
