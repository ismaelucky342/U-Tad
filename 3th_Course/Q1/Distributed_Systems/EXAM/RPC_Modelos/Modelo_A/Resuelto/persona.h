#ifndef PERSONA_H
#define PERSONA_H

#include <string>

// Interfaz e implementación base (simulada)
class Persona {
public:
    virtual void setEdad(int edad) {}
    virtual int getEdad() { return 0; }
    virtual void setNombre(std::string nombre) {}
    virtual std::string getNombre() { return ""; }
    virtual ~Persona() {}
};

// Clase Proxy (Cliente)
class PersonaRemota : public Persona {
private:
    int serverSocket;
public:
    PersonaRemota(int socket) : serverSocket(socket) {}
    void setEdad(int edad) override;
    int getEdad() override;
    void setNombre(std::string nombre) override;
    std::string getNombre() override;
};

#endif
