#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nombre[50];
    int edad;
    float salario;
} Persona;

void pedirDatos(Persona *p) {
    printf("Nombre: ");
    scanf("%49s", p->nombre);
    printf("Edad: ");
    scanf("%d", &(p->edad));
    printf("Salario: ");
    scanf("%f", &(p->salario));
}

int main() {
    FILE *file = fopen("personas.dat", "wb");
    if (file == NULL) {
        printf("No se pudo abrir el archivo\n");
        return 1;
    }

    int n;
    printf("Número de personas: ");
    scanf("%d", &n);

    Persona *personas = malloc(n * sizeof(Persona));
    for (int i = 0; i < n; i++) {
        printf("Persona %d\n", i + 1);
        pedirDatos(&personas[i]);
        fwrite(&personas[i], sizeof(Persona), 1, file);
    }

    free(personas);
    fclose(file);
    return 0;
}
