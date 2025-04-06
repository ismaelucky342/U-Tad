#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 256

// Ejercicio que cubre apertura de archivos, lectura, escritura y varias funciones relacionadas

// Función para abrir un archivo y devolver el puntero de archivo
FILE *open_file(const char *filename, const char *mode) {
    FILE *file = fopen(filename, mode);
    if (file == NULL) {
        perror("Error abriendo el archivo");
        exit(EXIT_FAILURE);
    }
    return file;
}

// Función para escribir una cadena en el archivo usando fputs
void write_using_fputs(FILE *file, const char *str) {
    if (fputs(str, file) == EOF) {
        perror("Error escribiendo en el archivo con fputs");
        exit(EXIT_FAILURE);
    }
}

// Función para leer un carácter del archivo usando fgetc
void read_char_using_fgetc(FILE *file) {
    int ch = fgetc(file);
    if (ch == EOF) {
        if (feof(file)) {
            printf("Fin de archivo alcanzado\n");
        } else {
            perror("Error leyendo un carácter del archivo");
            exit(EXIT_FAILURE);
        }
    } else {
        printf("Carácter leído: %c\n", (char)ch);
    }
}

// Función para leer una línea del archivo usando fgets
void read_line_using_fgets(FILE *file) {
    char buffer[MAX_LINE_LENGTH];
    if (fgets(buffer, sizeof(buffer), file) == NULL) {
        if (feof(file)) {
            printf("Fin de archivo alcanzado\n");
        } else {
            perror("Error leyendo una línea del archivo");
            exit(EXIT_FAILURE);
        }
    } else {
        printf("Línea leída: %s", buffer);
    }
}

// Función para imprimir el contenido de un archivo usando printf
void print_file_contents(FILE *file) {
    rewind(file); // Reposicionar el puntero al inicio del archivo
    char buffer[MAX_LINE_LENGTH];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
}

// Función para demostrar el uso de getc y feof
void read_using_getc(FILE *file) {
    rewind(file);
    int ch;
    while ((ch = getc(file)) != EOF) {
        putchar(ch);
    }
    if (feof(file)) {
        printf("\nFin de archivo alcanzado usando getc.\n");
    }
}

// Función para demostrar la escritura y lectura de un archivo con putc
void write_and_read_with_putc(const char *filename) {
    FILE *file = open_file(filename, "w+");

    const char *str = "Este es un ejemplo de uso de putc.\n";
    while (*str) {
        putc(*str++, file);  // Escribir caracter por caracter
    }

    rewind(file);  // Volver al inicio para leer
    printf("Contenido del archivo:\n");
    read_using_getc(file);

    fclose(file);
}

int main() {
    const char *filename = "example.txt";

    // Abriendo archivo
    FILE *file = open_file(filename, "w+");

    // Escribir en el archivo usando fputs
    write_using_fputs(file, "Hola, este es un ejemplo de fputs.\n");

    // Escribir en el archivo usando putc
    fputs("Este es un segundo ejemplo usando fputs.\n", file);

    // Cerrar archivo después de escritura
    fclose(file);

    // Abrir archivo para lectura
    file = open_file(filename, "r");

    // Leer y mostrar contenido usando fgetc
    printf("Leyendo archivo con fgetc:\n");
    read_char_using_fgetc(file);

    // Leer línea por línea usando fgets
    printf("\nLeyendo líneas con fgets:\n");
    read_line_using_fgets(file);

    // Mostrar todo el contenido usando printf y rewind
    printf("\nContenido completo del archivo:\n");
    print_file_contents(file);

    // Leer usando getc
    printf("\nLeyendo con getc:\n");
    read_using_getc(file);

    // Cerrar el archivo
    fclose(file);

    // Uso de putc para escribir y luego leer
    write_and_read_with_putc(filename);

    // Rewind para volver al principio del archivo y probar feof
    file = open_file(filename, "r");
    rewind(file);
    if (feof(file)) {
        printf("Estamos al final del archivo después de rewind.\n");
    }

    fclose(file);

    return 0;
}
