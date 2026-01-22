/*
 * MODELO A - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Clase: Persona
 * 
 * QUE TE DAN EN EL EXAMEN:
 * - Este archivo Persona.h con la declaración de la clase
 * 
 * QUE TE PIDEN:
 * - Implementar en Persona.cpp:
 *   1. Constructor por defecto
 *   2. Constructor con parámetros
 *   3. Destructor
 *   4. Getters (getNombre, getEdad)
 *   5. Setters (setNombre, setEdad)
 *   6. Método escribirAFichero
 *   7. Método leerDeFichero
 *   8. Sobrecarga del operador <<
 */

#ifndef PERSONA_H
#define PERSONA_H

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class Persona {
private:
    string nombre;
    int edad;

public:
    // Constructores y destructor
    Persona();
    Persona(string nombre, int edad);
    ~Persona();
    
    // Getters
    string getNombre() const;
    int getEdad() const;
    
    // Setters
    void setNombre(string nombre);
    void setEdad(int edad);
    
    // Métodos de fichero
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);
    
    // Sobrecarga operador <<
    friend ostream& operator<<(ostream& os, const Persona& p);
};

#endif // PERSONA_H
