/*
 * MODELO C - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Implementación: Estudiante.cpp
 * 
 * PARTE 1 DEL EXAMEN - Implementar clase remota Estudiante
 * 
 * PASOS A SEGUIR:
 * 
 * 1. INCLUIR EL ARCHIVO DE CABECERA
 *    - Añadir #include "Estudiante.h"
 * 
 * 2. CONSTRUCTOR POR DEFECTO
 *    - Inicializar nombre vacío
 *    - Inicializar matricula vacía
 *    - Inicializar notaMedia a 0.0
 * 
 * 3. CONSTRUCTOR CON PARÁMETROS
 *    - Recibir nombre, matricula y notaMedia
 *    - Asignar cada parámetro a su atributo correspondiente
 * 
 * 4. DESTRUCTOR
 *    - Dejar vacío o liberar recursos si fuera necesario
 * 
 * 5. IMPLEMENTAR GETTERS
 *    - getNombre(): devolver el atributo nombre
 *    - getMatricula(): devolver el atributo matricula
 *    - getNotaMedia(): devolver el atributo notaMedia
 * 
 * 6. IMPLEMENTAR SETTERS
 *    - setNombre(string): asignar el parámetro a nombre
 *    - setMatricula(string): asignar el parámetro a matricula
 *    - setNotaMedia(float): asignar el parámetro a notaMedia
 * 
 * 7. MÉTODO ESCRIBIR A FICHERO
 *    - Crear un ofstream con el nombre del fichero
 *    - Escribir nombre en una línea
 *    - Escribir matricula en otra línea
 *    - Escribir notaMedia en otra línea
 *    - Cerrar el archivo
 * 
 * 8. MÉTODO LEER DE FICHERO
 *    - Crear un ifstream con el nombre del fichero
 *    - Leer nombre con getline
 *    - Leer matricula con getline
 *    - Leer notaMedia con >>
 *    - Cerrar el archivo
 * 
 * 9. SOBRECARGA OPERADOR <<
 *    - Escribir en el stream: nombre, matricula y notaMedia
 *    - Devolver el stream
 */

#include "Estudiante.h"

// PASO 2: Constructor por defecto
Estudiante::Estudiante() {
    nombre = "";
    matricula = "";
    notaMedia = 0.0;
}

// PASO 3: Constructor con parámetros
Estudiante::Estudiante(string n, string m, float nota) {
    nombre = n;
    matricula = m;
    notaMedia = nota;
}

// PASO 4: Destructor
Estudiante::~Estudiante() {
    // Liberar recursos si fuera necesario
}

// PASO 5: Getters
string Estudiante::getNombre() const {
    return nombre;
}

string Estudiante::getMatricula() const {
    return matricula;
}

float Estudiante::getNotaMedia() const {
    return notaMedia;
}

// PASO 6: Setters
void Estudiante::setNombre(string n) {
    nombre = n;
}

void Estudiante::setMatricula(string m) {
    matricula = m;
}

void Estudiante::setNotaMedia(float nota) {
    notaMedia = nota;
}

// PASO 7: Escribir a fichero
void Estudiante::escribirAFichero(string nombreFichero) {
    ofstream archivo(nombreFichero.c_str());
    archivo << nombre << endl;
    archivo << matricula << endl;
    archivo << notaMedia << endl;
    archivo.close();
}

// PASO 8: Leer de fichero
void Estudiante::leerDeFichero(string nombreFichero) {
    ifstream archivo(nombreFichero.c_str());
    getline(archivo, nombre);
    getline(archivo, matricula);
    archivo >> notaMedia;
    archivo.close();
}

// PASO 9: Sobrecarga operador <<
ostream& operator<<(ostream& os, const Estudiante& e) {
    os << e.nombre << " [" << e.matricula << "] - Nota: " << e.notaMedia;
    return os;
}
