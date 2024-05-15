#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char Name[20];
    int age; 
    float altura; 
} Persona;

int main(int argc, char *argv[]) {
    //menu opcional
    if (argc != 2) {
        printf("Uso: %s <cantidad_de_personas>\n", argv[0]);
        return 1;
    }

    int cantidad_personas = atoi(argv[1]);
    Persona *personas = malloc(cantidad_personas * sizeof(Persona)); 
    if (personas == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        return 1;
    }

    for (int i = 0; i < cantidad_personas; i++) {
        printf("Ingrese el nombre de la persona %d: ", i + 1);
        scanf("%19s", personas[i].Name); // Use %19s to avoid buffer overflow
        printf("Ingrese la edad de la persona %d: ", i + 1);
        scanf("%d", &personas[i].age); // Correct field usage
        printf("Ingrese la altura de la persona %d (en metros): ", i + 1);
        scanf("%f", &personas[i].altura); // Correct field usage
    }

    FILE *archivo = fopen("personas.dat", "wb");
    if (archivo == NULL) {
        printf("Error al abrir el archivo para escritura.\n");
        return 1;
    }
    fwrite(personas, sizeof(Persona), cantidad_personas, archivo);
    fclose(archivo);

    // Leer los datos del archivo binario y mostrarlos por pantalla
    archivo = fopen("personas.dat", "rb");
    if (archivo == NULL) {
        printf("Error al abrir el archivo para lectura.\n");
        return 1;
    }

    printf("\nDatos de las personas guardados en el archivo:\n");
    printf("---------------------------------------------\n");
    Persona persona_leida;
    while (fread(&persona_leida, sizeof(Persona), 1, archivo) == 1) {
        printf("Nombre: %s, Edad: %d, Altura: %.2f m\n", persona_leida.Name, persona_leida.age, persona_leida.altura); // Correct order of fields
    }
    fclose(archivo);

    // Liberar memoria asignada para el array de personas
    free(personas);

    return 0;
}
