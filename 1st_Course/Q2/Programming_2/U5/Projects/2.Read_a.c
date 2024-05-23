#include <stdio.h>

int main() {
    FILE *fp;
    char buffer[256]; // Buffer para almacenar cada línea del archivo

    // Intentar abrir el archivo "a.txt" en modo de lectura
    fp = fopen("a.txt", "r");

    if (fp != NULL) {
        // Leer el archivo línea por línea
        while (fgets(buffer, sizeof(buffer), fp) != NULL) {
            // Imprimir cada línea leída en la consola
            printf("%s", buffer);
        }
        // Cerrar el archivo después de la lectura
        fclose(fp);
    } else {
        // Imprimir mensaje de error si no se pudo abrir el archivo
        printf("ERROR: No se pudo abrir el archivo 'a.txt'.\n");
    }

    return 0;
}
