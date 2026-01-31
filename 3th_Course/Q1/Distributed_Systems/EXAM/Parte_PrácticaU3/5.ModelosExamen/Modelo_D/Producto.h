/*
 * MODELO D - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Clase: Producto
 * 
 * QUE TE DAN EN EL EXAMEN:
 * - Este archivo Producto.h con la declaración de la clase
 * 
 * QUE TE PIDEN:
 * - Implementar en Producto.cpp:
 *   1. Constructor por defecto
 *   2. Constructor con parámetros
 *   3. Destructor
 *   4. Getters (getNombre, getCodigo, getPrecio)
 *   5. Setters (setNombre, setCodigo, setPrecio)
 *   6. Método escribirAFichero
 *   7. Método leerDeFichero
 *   8. Sobrecarga del operador <<
 */

#ifndef PRODUCTO_H
#define PRODUCTO_H

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class Producto {
private:
    string nombre;
    string codigo;
    double precio;

public:
    // Constructores y destructor
    Producto();
    Producto(string nombre, string codigo, double precio);
    ~Producto();
    
    // Getters
    string getNombre() const;
    string getCodigo() const;
    double getPrecio() const;
    
    // Setters
    void setNombre(string nombre);
    void setCodigo(string codigo);
    void setPrecio(double precio);
    
    // Métodos de fichero
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);
    
    // Sobrecarga operador <<
    friend ostream& operator<<(ostream& os, const Producto& p);
};

#endif // PRODUCTO_H
