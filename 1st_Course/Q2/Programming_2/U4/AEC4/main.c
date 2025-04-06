#include <stdio.h>
#include <stdlib.h>
#include "funciones.h"

int main() {
    char* mensaje = leeLineaDinamica();
    printf("Mensaje ingresado: %s\n", mensaje);
    
    char* mensaje_mayusculas = cambiaMayusculas(mensaje);
    printf("Mensaje en mayúsculas: %s\n", mensaje_mayusculas);

    char* mensaje_encriptado = encriptaMensaje(mensaje_mayusculas);
    printf("Mensaje encriptado: %s\n", mensaje_encriptado);

    char* datos_encriptados = encuentraDatos(mensaje_encriptado);
    printf("Datos encriptados: %s\n", datos_encriptados);

    char* datos_decodificados = decodificaDatos(datos_encriptados);
    printf("Datos decodificados: %s\n", datos_decodificados);

    free(mensaje);
    free(mensaje_mayusculas);
    free(mensaje_encriptado);
    free(datos_encriptados);
    free(datos_decodificados);

    return 0;
}

