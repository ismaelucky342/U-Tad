#include <stdio.h>
#include <stdlib.h>
#include "file_utils.h"
#include "data_utils.h"

int main() {
    FILE *archivo;
    int numLineas;

    // Abrir el archivo de texto
    archivo = fopen("datos.txt", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    // Contar el número de líneas en el archivo
    numLineas = contarLineas(archivo);
    rewind(archivo); // Volver al principio del archivo

    // Crear un array de estructuras del tamaño adecuado
    Datos *datos = (Datos *)malloc(numLineas * sizeof(Datos));

    // Leer los datos del archivo y guardarlos en el array de estructuras
    leeDatosStruct(archivo, datos, numLineas);

    // Cerrar el archivo de texto
    fclose(archivo);

    // Guardar los datos en un archivo binario
    guardarDatosBinario(datos, numLineas);

    // Leer un registro desde el archivo binario y mostrarlo
    leerRegistroBinario();

    // Liberar la memoria asignada al array de estructuras
    free(datos);

    return 0;
}
