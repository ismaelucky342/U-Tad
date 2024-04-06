#include "animacion.h"
#include "mensaje.h"
#include <stdio.h>
#include <unistd.h>

void configurarAnimacion(int *velocidad, int *tamanioVentana) {
    printf("Ingrese la velocidad de desplazamiento (en milisegundos): ");
    scanf("%d", velocidad);
    printf("Ingrese el tamaño de la ventana de visualizacion: ");
    scanf("%d", tamanioVentana);
}

void animarTexto(Mensaje mensaje, int velocidad, int tamanioVentana) {
    int i, j;

    for (i = 0; i < mensaje.length + tamanioVentana; i++) {
        for (j = 0; j < tamanioVentana; j++) {
            if (j + i < mensaje.length) {
                putchar(mensaje.text[j + i]);
            } else {
                putchar(' ');
            }
        }
        fflush(stdout);
        usleep(velocidad * 1000);
        printf("\r");
    }
}
