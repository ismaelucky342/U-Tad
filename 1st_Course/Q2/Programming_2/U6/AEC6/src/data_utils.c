#include "data_utils.h"

void leeDatosStruct(FILE *archivo, Datos *datos, int numLineas) {
    char buffer[100];
    fgets(buffer, 100, archivo); // Consumir la primera línea que contiene los nombres de los campos

    for (int i = 0; i < numLineas; i++) {
        fscanf(archivo, "%d/%d/%d,%d,%f", &datos[i].dia, &datos[i].mes, &datos[i].anio, &datos[i].hora, &datos[i].velocidad);
    }
}

void guardarDatosBinario(Datos *datos, int numLineas) {
    FILE *archivo;
    archivo = fopen("datos.bin", "wb");

    if (archivo == NULL) {
        printf("Error al abrir el archivo binario.\n");
        exit(1);
    }

    fwrite(datos, sizeof(Datos), numLineas, archivo);
    fclose(archivo);
}

void leerRegistroBinario() {
    FILE *archivo;
    int indice;

    printf("Ingrese el número de registro a leer: ");
    scanf("%d", &indice);

    archivo = fopen("datos.bin", "rb");
    if (archivo == NULL) {
        printf("Error al abrir el archivo binario.\n");
        exit(1);
    }

    fseek(archivo, indice * sizeof(Datos), SEEK_SET);

    Datos registro;
    fread(&registro, sizeof(Datos), 1, archivo);

    printf("Registro leído:\n");
    printf("Fecha: %d/%d/%d\n", registro.dia, registro.mes, registro.anio);
    printf("Hora: %d\n", registro.hora);
    printf("Velocidad: %.4f\n", registro.velocidad);

    fclose(archivo);
}
