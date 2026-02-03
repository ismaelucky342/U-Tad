#pragma once
#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

class Vehiculo {

private:
    string marca;
    string modelo;
    int anio;
    int kilometraje;
public:

    /**
    * @brief Constructor por defecto
    */
    Vehiculo();

    /**
    * @brief Constructor con parámetros
    * @param marca
    * @param modelo
    * @param anio
    * @param kilometraje
    */
    Vehiculo(string marca, string modelo, int anio, int kilometraje);
    
    /**
    * @brief Destructor por defecto
    */
    ~Vehiculo();

    /**
    * Getter/Setter para parámetros
    */
    void setMarca(string marca);
    string getMarca();
    void setModelo(string modelo);
    string getModelo();
    void setAnio(int anio);
    int getAnio();
    void setKilometraje(int kilometraje);
    int getKilometraje();

    /**
    * Métodos para leer/escribir un vehículo a un archivo de texto
    */
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);

    /**
    * Operador para mostrar por terminal los datos del vehículo formateados
    */
    friend ostream& operator << (ostream& out, const Vehiculo& v);
};
