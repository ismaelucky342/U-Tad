#include "mensaje.h"
#include "animacion.h"
#include <stdlib.h>
#include <stdio.h>

int main() {
    Mensaje mensaje;
    int velocidad, tamanioVentana;

    leerMensaje(&mensaje);
    configurarAnimacion(&velocidad, &tamanioVentana);

    animarTexto(mensaje, velocidad, tamanioVentana);

    free(mensaje.text);

    return 0;
}