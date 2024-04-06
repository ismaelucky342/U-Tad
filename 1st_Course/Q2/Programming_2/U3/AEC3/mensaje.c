#include "mensaje.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void leerMensaje(Mensaje *mensaje) {
    char buffer[100];
    printf("Ingrese el mensaje a animar: ");
    fgets(buffer, sizeof(buffer), stdin);
    mensaje->length = strlen(buffer);
    mensaje->text = (char *)malloc(mensaje->length * sizeof(char));
    strcpy(mensaje->text, buffer);
}
