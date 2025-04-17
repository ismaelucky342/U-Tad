#ifndef AGENDA_H
#define AGENDA_H

#include <string>
#include <iostream>
#include <cctype> 
#include <cstdlib> 
#include <ctime> 
#include <iomanip> 

#define RED     "\033[1;31m"
#define GREEN   "\033[1;32m"
#define CYAN    "\033[1;36m"
#define YELLOW  "\033[1;33m"
#define RESET   "\033[0m"
#define BLUE    "\033[1;34m"
#define MAGENTA "\033[1;35m"

using namespace std;

class Agenda {
private:
    int capacidad;
    string* nombres;
    long* telefonos;
    bool* ocupados;

public:
    Agenda(int capacidad);                    
    ~Agenda();                                 
    int obtenerPosicion(long telefono);        
    bool existeContacto(long telefono);        
    string getContacto(long telefono);        
    void introducirContacto(long telefono, string contacto); 
    void eliminarContacto(long telefono);     
    void imprimir();                           
};

#endif
