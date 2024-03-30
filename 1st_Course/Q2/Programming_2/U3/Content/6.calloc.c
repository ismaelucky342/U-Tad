#include <stdio.h>
#include <stdlib.h>

int main() {
    
    int n;
    printf("Ingrese el tamaño del arreglo: ");
    scanf("%d", &n);

    int *arr = (int *)calloc(n, sizeof(int));

    if (arr == NULL) {
        printf("Error: No se pudo asignar memoria.");
        return 1;
    }
    printf("Tamaño del arreglo en bytes: %zu\n", n * sizeof(int));

    free(arr);
    return 0;
}
