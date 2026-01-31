/*
 * MODELO C - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Clase: Estudiante
 * 
 * QUE TE DAN EN EL EXAMEN:
 * - Este archivo Estudiante.h con la declaración de la clase
 * 
 * QUE TE PIDEN:
 * - Implementar en Estudiante.cpp:
 *   1. Constructor por defecto
 *   2. Constructor con parámetros
 *   3. Destructor
 *   4. Getters (getNombre, getMatricula, getNotaMedia)
 *   5. Setters (setNombre, setMatricula, setNotaMedia)
 *   6. Método escribirAFichero
 *   7. Método leerDeFichero
 *   8. Sobrecarga del operador <<
 */

#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H

#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class Estudiante {
private:
    string nombre;
    string matricula;
    float notaMedia;

public:
    // Constructores y destructor
    Estudiante();
    Estudiante(string nombre, string matricula, float notaMedia);
    ~Estudiante();
    
    // Getters
    string getNombre() const;
    string getMatricula() const;
    float getNotaMedia() const;
    
    // Setters
    void setNombre(string nombre);
    void setMatricula(string matricula);
    void setNotaMedia(float notaMedia);
    
    // Métodos de fichero
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);
    
    // Sobrecarga operador <<
    friend ostream& operator<<(ostream& os, const Estudiante& e);
};

#endif // ESTUDIANTE_H
