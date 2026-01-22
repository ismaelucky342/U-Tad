/*
 * MODELO A - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Implementación: Persona.cpp
 * 
 * PARTE 1 DEL EXAMEN - Implementar clase remota Persona
 * 
 * PASOS A SEGUIR:
 * 
 * 1. INCLUIR EL ARCHIVO DE CABECERA
 *    - Añadir #include "Persona.h"
 * 
 * 2. CONSTRUCTOR POR DEFECTO
 *    - Inicializar nombre vacío
 *    - Inicializar edad a 0
 * 
 * 3. CONSTRUCTOR CON PARÁMETROS
 *    - Recibir nombre y edad
 *    - Asignar cada parámetro a su atributo correspondiente
 * 
 * 4. DESTRUCTOR
 *    - Dejar vacío o liberar recursos si fuera necesario
 * 
 * 5. IMPLEMENTAR GETTERS
 *    - getNombre(): devolver el atributo nombre
 *    - getEdad(): devolver el atributo edad
 * 
 * 6. IMPLEMENTAR SETTERS
 *    - setNombre(string): asignar el parámetro a nombre
 *    - setEdad(int): asignar el parámetro a edad
 * 
 * 7. MÉTODO ESCRIBIR A FICHERO
 *    - Crear un ofstream con el nombre del fichero
 *    - Escribir nombre en una línea
 *    - Escribir edad en otra línea
 *    - Cerrar el archivo
 * 
 * 8. MÉTODO LEER DE FICHERO
 *    - Crear un ifstream con el nombre del fichero
 *    - Leer nombre con getline
 *    - Leer edad con >>
 *    - Cerrar el archivo
 * 
 * 9. SOBRECARGA OPERADOR <<
 *    - Escribir en el stream: nombre y edad
 *    - Devolver el stream
 */

#include "Persona.h"

// PASO 2: Constructor por defecto
Persona::Persona() {
    nombre = "";
    edad = 0;
}

// PASO 3: Constructor con parámetros
Persona::Persona(string n, int e) {
    nombre = n;
    edad = e;
}

// PASO 4: Destructor
Persona::~Persona() {
    // Liberar recursos si fuera necesario
}

// PASO 5: Getters
string Persona::getNombre() const {
    return nombre;
}

int Persona::getEdad() const {
    return edad;
}

// PASO 6: Setters
void Persona::setNombre(string n) {
    nombre = n;
}

void Persona::setEdad(int e) {
    edad = e;
}

// PASO 7: Escribir a fichero
void Persona::escribirAFichero(string nombreFichero) {
    ofstream archivo(nombreFichero.c_str());
    archivo << nombre << endl;
    archivo << edad << endl;
    archivo.close();
}

// PASO 8: Leer de fichero
void Persona::leerDeFichero(string nombreFichero) {
    ifstream archivo(nombreFichero.c_str());
    getline(archivo, nombre);
    archivo >> edad;
    archivo.close();
}

// PASO 9: Sobrecarga operador <<
ostream& operator<<(ostream& os, const Persona& p) {
    os << p.nombre << ", " << p.edad << " años";
    return os;
}
