#ifndef MENSAJE_H
#define MENSAJE_H

typedef struct {
    char *text;
    int length;
} Mensaje;

void leerMensaje(Mensaje *mensaje);

#endif
