#include<stdio.h>
#include<string.h>

typedef struct Grades {
    int  math;
    int  english;
    int  science;
} Grades; 

typedef struct Student {
    char name[10];
    char surname[15]; 
    char ID[8];
    Grades grades; 
} Student;

int main() {
    // Definir un array de estudiantes
    Student students[5] = {
        {"John", "Doe", "1234567", {90, 85, 88}},
        {"Jane", "Smith", "2345678", {88, 92, 85}},
        {"Alice", "Johnson", "3456789", {95, 90, 92}},
        {"Bob", "Williams", "4567890", {82, 88, 85}},
        {"Eva", "Brown", "5678901", {90, 85, 90}}
    };

    char searchID[8];
    printf("Inserte el ID del estudiante: ");
    scanf("%s", searchID);

    // Buscar el estudiante por ID
    int found = 0;
    for (int i = 0; i < 5; i++) {
        if (strcmp(students[i].ID, searchID) == 0) {
            printf("Información del estudiante:\n");
            printf("Nombre: %s\n", students[i].name);
            printf("Apellido: %s\n", students[i].surname);
            printf("ID: %s\n", students[i].ID);
            printf("Notas:\n");
            printf("  Matemáticas: %d\n", students[i].grades.math);
            printf("  Inglés: %d\n", students[i].grades.english);
            printf("  Ciencias: %d\n", students[i].grades.science);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("No se encontró ningún estudiante con ese ID.\n");
    }

    return 0;
}
