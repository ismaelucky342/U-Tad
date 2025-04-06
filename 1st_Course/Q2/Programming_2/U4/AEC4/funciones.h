#ifndef FUNCIONES_H
#define FUNCIONES_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* leeLineaDinamica();
char* cambiaMayusculas(char* cadena_leida);
char* encriptaMensaje(char* cadena_mayusculas);
char* encuentraDatos(char* cadena_encriptada);
char* decodificaDatos(char* cadena_encriptada_datos);
char tablaEncriptacion(char letra);

#endif /* FUNCIONES_H */
