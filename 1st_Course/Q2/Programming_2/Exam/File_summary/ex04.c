#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nombre[50];
    int edad;
    float salario;
} Persona;

int main() {
    FILE *file = fopen("personas.dat", "rb");

    if (file == NULL)
    {
        printf("No se pudo abrir el archivo\n");
        return 1;
    }
    
    Persona persona; 
    while (fread(&persona, sizeof(Persona), 1, file))
    {
        printf("Nombre: %s\n", persona.nombre);
        printf("Edad: %d\n", persona.edad);
        printf("Salario: %.2f\n\n", persona.salario);
    }

    fclose(file);
    return 0;
}
