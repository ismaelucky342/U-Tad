#ifndef AGENDACOLISIONES_H
#define AGENDACOLISIONES_H

#include <string>
#include "ListaEnlazada.h"

#define RED     "\033[1;31m"
#define GREEN   "\033[1;32m"
#define CYAN    "\033[1;36m"
#define YELLOW  "\033[1;33m"
#define RESET   "\033[0m"
#define BLUE    "\033[1;34m"
#define MAGENTA "\033[1;35m"


class Agenda {
private:
    int capacidad;
    int n;
    ListaEnlazada* tabla;

    int obtenerPosicion(long telefono);

public:
    Agenda(int capacidad);
    ~Agenda();

    bool existeContacto(long telefono);
    std::string getContacto(long telefono);
    void introducirContacto(long telefono, std::string contacto);
    void eliminarContacto(long telefono);
    void imprimir(); // No se implementa
};

#endif
