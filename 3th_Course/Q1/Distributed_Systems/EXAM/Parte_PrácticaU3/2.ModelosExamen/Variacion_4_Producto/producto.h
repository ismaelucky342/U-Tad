#pragma once
#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

class Producto {

private:
    string nombre;
    double precio;
    int stock;
    string categoria;
public:

    /**
    * @brief Constructor por defecto
    */
    Producto();

    /**
    * @brief Constructor con parámetros
    * @param nombre
    * @param precio
    * @param stock
    * @param categoria
    */
    Producto(string nombre, double precio, int stock, string categoria);
    
    /**
    * @brief Destructor por defecto
    */
    ~Producto();

    /**
    * Getter/Setter para parámetros
    */
    void setNombre(string nombre);
    string getNombre();
    void setPrecio(double precio);
    double getPrecio();
    void setStock(int stock);
    int getStock();
    void setCategoria(string categoria);
    string getCategoria();

    /**
    * Métodos para leer/escribir un producto a un archivo de texto
    */
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);

    /**
    * Operador para mostrar por terminal los datos del producto formateados
    */
    friend ostream& operator << (ostream& out, const Producto& p);
};
