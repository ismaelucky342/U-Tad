#ifndef NODO_H
#define NODO_H

#include "Contacto.h"

class Nodo {
private:
    Contacto contacto;
    Nodo* siguiente;

public:
    Nodo(Contacto contacto);
    Contacto& getContacto();
    Nodo* getSiguiente();
    void setSiguiente(Nodo* siguiente);
};

#endif
