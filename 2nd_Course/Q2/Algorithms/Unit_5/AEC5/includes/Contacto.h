#ifndef CONTACTO_H
#define CONTACTO_H

#include <string>

class Contacto {
private:
    long telefono;
    std::string nombre;

public:
    Contacto(long telefono, std::string nombre);
    long getTelefono() const;
    std::string getNombre() const;
    void setNombre(std::string nuevoNombre);
};

#endif
