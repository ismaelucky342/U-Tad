/*
 * MODELO D - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Implementación: Producto.cpp
 * 
 * PARTE 1 DEL EXAMEN - Implementar clase remota Producto
 * 
 * PASOS A SEGUIR:
 * 
 * 1. INCLUIR EL ARCHIVO DE CABECERA
 *    - Añadir #include "Producto.h"
 * 
 * 2. CONSTRUCTOR POR DEFECTO
 *    - Inicializar nombre vacío
 *    - Inicializar codigo vacío
 *    - Inicializar precio a 0.0
 * 
 * 3. CONSTRUCTOR CON PARÁMETROS
 *    - Recibir nombre, codigo y precio
 *    - Asignar cada parámetro a su atributo correspondiente
 * 
 * 4. DESTRUCTOR
 *    - Dejar vacío o liberar recursos si fuera necesario
 * 
 * 5. IMPLEMENTAR GETTERS
 *    - getNombre(): devolver el atributo nombre
 *    - getCodigo(): devolver el atributo codigo
 *    - getPrecio(): devolver el atributo precio
 * 
 * 6. IMPLEMENTAR SETTERS
 *    - setNombre(string): asignar el parámetro a nombre
 *    - setCodigo(string): asignar el parámetro a codigo
 *    - setPrecio(double): asignar el parámetro a precio
 * 
 * 7. MÉTODO ESCRIBIR A FICHERO
 *    - Crear un ofstream con el nombre del fichero
 *    - Escribir nombre en una línea
 *    - Escribir codigo en otra línea
 *    - Escribir precio en otra línea
 *    - Cerrar el archivo
 * 
 * 8. MÉTODO LEER DE FICHERO
 *    - Crear un ifstream con el nombre del fichero
 *    - Leer nombre con getline
 *    - Leer codigo con getline
 *    - Leer precio con >>
 *    - Cerrar el archivo
 * 
 * 9. SOBRECARGA OPERADOR <<
 *    - Escribir en el stream: nombre, codigo y precio
 *    - Devolver el stream
 */

#include "Producto.h"

// PASO 2: Constructor por defecto
Producto::Producto() {
    nombre = "";
    codigo = "";
    precio = 0.0;
}

// PASO 3: Constructor con parámetros
Producto::Producto(string n, string c, double p) {
    nombre = n;
    codigo = c;
    precio = p;
}

// PASO 4: Destructor
Producto::~Producto() {
    // Liberar recursos si fuera necesario
}

// PASO 5: Getters
string Producto::getNombre() const {
    return nombre;
}

string Producto::getCodigo() const {
    return codigo;
}

double Producto::getPrecio() const {
    return precio;
}

// PASO 6: Setters
void Producto::setNombre(string n) {
    nombre = n;
}

void Producto::setCodigo(string c) {
    codigo = c;
}

void Producto::setPrecio(double p) {
    precio = p;
}

// PASO 7: Escribir a fichero
void Producto::escribirAFichero(string nombreFichero) {
    ofstream archivo(nombreFichero.c_str());
    archivo << nombre << endl;
    archivo << codigo << endl;
    archivo << precio << endl;
    archivo.close();
}

// PASO 8: Leer de fichero
void Producto::leerDeFichero(string nombreFichero) {
    ifstream archivo(nombreFichero.c_str());
    getline(archivo, nombre);
    getline(archivo, codigo);
    archivo >> precio;
    archivo.close();
}

// PASO 9: Sobrecarga operador <<
ostream& operator<<(ostream& os, const Producto& p) {
    os << p.nombre << " [" << p.codigo << "] - " << p.precio << "€";
    return os;
}
