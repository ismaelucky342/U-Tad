#ifndef DATA_UTILS_H
#define DATA_UTILS_H

#include <stdio.h>
#include <stdlib.h>


typedef struct {
    int dia;
    int mes;
    int anio;
    int hora;
    float velocidad;
} Datos;

void leeDatosStruct(FILE *archivo, Datos *datos, int numLineas);
void guardarDatosBinario(Datos *datos, int numLineas);
void leerRegistroBinario();

#endif /* DATA_UTILS_H */
