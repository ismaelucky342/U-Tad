/*
 * MODELO B - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Implementación: Libro.cpp
 * 
 * PARTE 1 DEL EXAMEN - Implementar clase remota Libro
 * 
 * PASOS A SEGUIR:
 * 
 * 1. INCLUIR EL ARCHIVO DE CABECERA
 *    - Añadir #include "Libro.h"
 * 
 * 2. CONSTRUCTOR POR DEFECTO
 *    - Inicializar titulo vacío
 *    - Inicializar autor vacío
 *    - Inicializar numPaginas a 0
 * 
 * 3. CONSTRUCTOR CON PARÁMETROS
 *    - Recibir titulo, autor y numPaginas
 *    - Asignar cada parámetro a su atributo correspondiente
 * 
 * 4. DESTRUCTOR
 *    - Dejar vacío o liberar recursos si fuera necesario
 * 
 * 5. IMPLEMENTAR GETTERS
 *    - getTitulo(): devolver el atributo titulo
 *    - getAutor(): devolver el atributo autor
 *    - getNumPaginas(): devolver el atributo numPaginas
 * 
 * 6. IMPLEMENTAR SETTERS
 *    - setTitulo(string): asignar el parámetro a titulo
 *    - setAutor(string): asignar el parámetro a autor
 *    - setNumPaginas(int): asignar el parámetro a numPaginas
 * 
 * 7. MÉTODO ESCRIBIR A FICHERO
 *    - Crear un ofstream con el nombre del fichero
 *    - Escribir titulo en una línea
 *    - Escribir autor en otra línea
 *    - Escribir numPaginas en otra línea
 *    - Cerrar el archivo
 * 
 * 8. MÉTODO LEER DE FICHERO
 *    - Crear un ifstream con el nombre del fichero
 *    - Leer titulo con getline
 *    - Leer autor con getline
 *    - Leer numPaginas con >>
 *    - Cerrar el archivo
 * 
 * 9. SOBRECARGA OPERADOR <<
 *    - Escribir en el stream: titulo, autor y numPaginas
 *    - Devolver el stream
 */

#include "Libro.h"

// PASO 2: Constructor por defecto
Libro::Libro() {
    titulo = "";
    autor = "";
    numPaginas = 0;
}

// PASO 3: Constructor con parámetros
Libro::Libro(string t, string a, int n) {
    titulo = t;
    autor = a;
    numPaginas = n;
}

// PASO 4: Destructor
Libro::~Libro() {
    // Liberar recursos si fuera necesario
}

// PASO 5: Getters
string Libro::getTitulo() const {
    return titulo;
}

string Libro::getAutor() const {
    return autor;
}

int Libro::getNumPaginas() const {
    return numPaginas;
}

// PASO 6: Setters
void Libro::setTitulo(string t) {
    titulo = t;
}

void Libro::setAutor(string a) {
    autor = a;
}

void Libro::setNumPaginas(int n) {
    numPaginas = n;
}

// PASO 7: Escribir a fichero
void Libro::escribirAFichero(string nombreFichero) {
    ofstream archivo(nombreFichero.c_str());
    archivo << titulo << endl;
    archivo << autor << endl;
    archivo << numPaginas << endl;
    archivo.close();
}

// PASO 8: Leer de fichero
void Libro::leerDeFichero(string nombreFichero) {
    ifstream archivo(nombreFichero.c_str());
    getline(archivo, titulo);
    getline(archivo, autor);
    archivo >> numPaginas;
    archivo.close();
}

// PASO 9: Sobrecarga operador <<
ostream& operator<<(ostream& os, const Libro& l) {
    os << l.titulo << " de " << l.autor << " (" << l.numPaginas << " pags)";
    return os;
}
