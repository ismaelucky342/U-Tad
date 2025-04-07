#ifndef AGENDA_H
#define AGENDA_H

#include <string>
using namespace std;

class Agenda {
private:
    int capacidad;
    string* nombres;
    long* telefonos;
    bool* ocupados;

    int obtenerPosicion(long telefono);

public:
    Agenda(int capacidad);
    ~Agenda();

    bool existeContacto(long telefono);
    string getContacto(long telefono);
    void introducirContacto(long telefono, string contacto);
    void eliminarContacto(long telefono);
    void imprimir(); // NO IMPLEMENTAR, ya la maneja el corrector
};

#endif
