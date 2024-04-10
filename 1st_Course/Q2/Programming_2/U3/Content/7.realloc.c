#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Ingrese el tamaño inicial del arreglo: ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));

    if (arr == NULL) {
        printf("Error: No se pudo asignar memoria.");
        return 1;
    }

    printf("Tamaño inicial del arreglo en bytes: %zu\n", n * sizeof(int));

    int nuevo_tam;
    printf("Ingrese el nuevo tamaño del arreglo: ");
    scanf("%d", &nuevo_tam);

    arr = (int *)realloc(arr, nuevo_tam * sizeof(int));

    if (arr == NULL) {
        printf("Error: No se pudo reasignar memoria.");
        return 1;
    }

    printf("Nuevo tamaño del arreglo en bytes: %zu\n", nuevo_tam * sizeof(int));

    free(arr);
    
    return 0;
}


