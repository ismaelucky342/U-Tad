/*
 * MODELO B - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Clase: Libro
 * 
 * QUE TE DAN EN EL EXAMEN:
 * - Este archivo Libro.h con la declaración de la clase
 * 
 * QUE TE PIDEN:
 * - Implementar en Libro.cpp:
 *   1. Constructor por defecto
 *   2. Constructor con parámetros
 *   3. Destructor
 *   4. Getters (getTitulo, getAutor, getNumPaginas)
 *   5. Setters (setTitulo, setAutor, setNumPaginas)
 *   6. Método escribirAFichero
 *   7. Método leerDeFichero
 *   8. Sobrecarga del operador <<
 */

#ifndef LIBRO_H
#define LIBRO_H

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class Libro {
private:
    string titulo;
    string autor;
    int numPaginas;

public:
    // Constructores y destructor
    Libro();
    Libro(string titulo, string autor, int numPaginas);
    ~Libro();
    
    // Getters
    string getTitulo() const;
    string getAutor() const;
    int getNumPaginas() const;
    
    // Setters
    void setTitulo(string titulo);
    void setAutor(string autor);
    void setNumPaginas(int numPaginas);
    
    // Métodos de fichero
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);
    
    // Sobrecarga operador <<
    friend ostream& operator<<(ostream& os, const Libro& l);
};

#endif // LIBRO_H
