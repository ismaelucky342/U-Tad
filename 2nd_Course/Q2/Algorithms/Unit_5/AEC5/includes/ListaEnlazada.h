#ifndef LISTAENLAZADA_H
#define LISTAENLAZADA_H

#include "Nodo.h"

class ListaEnlazada {
private:
    Nodo* cabeza;

public:
    ListaEnlazada();
    ~ListaEnlazada();

    void insertar(Contacto contacto);
    Nodo* buscar(long telefono);
    bool eliminar(long telefono);
};

#endif
