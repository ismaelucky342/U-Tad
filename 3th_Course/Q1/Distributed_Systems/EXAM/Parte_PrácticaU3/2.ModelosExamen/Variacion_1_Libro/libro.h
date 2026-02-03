#pragma once
#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

class Libro {

private:
    string titulo;
    string autor;
    int numPaginas;
public:

    /**
    * @brief Constructor por defecto
    */
    Libro();

    /**
    * @brief Constructor con parámetros, recibe "titulo", "autor" y "numPaginas"
    * @param titulo
    * @param autor
    * @param numPaginas
    */
    Libro(string titulo, string autor, int numPaginas);
    
    /**
    * @brief Destructor por defecto
    */
    ~Libro();

    /**
    * Getter/Setter para parámetros
    */
    void setTitulo(string titulo);
    string getTitulo();
    void setAutor(string autor);
    string getAutor();
    void setNumPaginas(int numPaginas);
    int getNumPaginas();

    /**
    * Métodos para leer/escribir un libro a un archivo de texto
    */
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);

    /**
    * Operador para mostrar por terminal los datos del libro formateados
    */
    friend ostream& operator << (ostream& out, const Libro& l);
};
