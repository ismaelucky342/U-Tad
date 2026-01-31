#pragma once
#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

class Persona {

private:
    string nombre;
    int edad;
public:

    /**
    * @brief Constructor por defecto
    */

    Persona();

    /**
    * @brief Constructor con parámetros, recibe los parámetros "nombre" y "edad"
    * @param nombre
    * @param edad
    */
    Persona(string nombre, int edad);
    
    /**
    * @brief Destructor por defecto
    */
    ~Persona();

    /**
    * Getter/Setter para parámetros edad y nombre
    */
    void setEdad(int edad);
    int getEdad();
    void setNombre(string nombre);
    string getNombre();

    /**
    * Métodos para leer/escribir una persona a un archivo de texto. Reciben
    * por parámetros el nombre del fichero
    */
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);

    /**
    * Operador para mostrar por terminal los datos de la persona formateados
    */
    friend ostream& operator << (ostream& out, const Persona& c);
};