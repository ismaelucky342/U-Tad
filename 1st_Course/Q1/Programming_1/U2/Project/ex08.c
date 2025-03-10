/*Ejercicio: Crea una estructura Persona con nombre y edad, luego crea una variable de tipo Persona y muestra sus datos.*/
#include <stdio.h>

struct Persona {
    char nombre[50];
    int edad;
};

int main() {
    struct Persona p1;

    printf("Ingrese su nombre: ");
    scanf("%s", p1.nombre);
    printf("Ingrese su edad: ");
    scanf("%d", &p1.edad);

    printf("Nombre: %s\n", p1.nombre);
    printf("Edad: %d\n", p1.edad);

    return 0;
}
