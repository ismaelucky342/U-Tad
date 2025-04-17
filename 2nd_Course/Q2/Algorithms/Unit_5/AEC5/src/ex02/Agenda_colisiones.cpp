/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        02/04/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    17/04/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

#include "../../includes/AgendaColisiones.h"
#include <iostream>
#include <stdexcept>

using namespace std;

/**
 * Constructor con parámetros.
 * Reserva espacio para un vector de listas enlazadas de tamaño "capacidad".
 * Complejidad temporal: O(capacidad)
 * Complejidad espacial: O(capacidad)
 */
Agenda::Agenda(int capacidad) {
    if (capacidad <= 0) {
        throw invalid_argument("La capacidad debe ser mayor que 0.");
    }
    this->capacidad = capacidad;
    this->n = 0;
    this->tabla = new ListaEnlazada[capacidad];
}

/**
 * Destructor.
 * Libera la memoria asignada dinámicamente al vector de listas.
 * Complejidad temporal: O(capacidad)
 * Complejidad espacial: O(1)
 */
Agenda::~Agenda() {
    delete[] tabla;
}

/**
 * Función hash para calcular la posición en la tabla.
 * Usa el resto de la división entre el teléfono y la capacidad.
 * Complejidad temporal: O(1)
 * Complejidad espacial: O(1)
 */
int Agenda::obtenerPosicion(long telefono) {
    return telefono % capacidad;
}

/**
 * Comprueba si un contacto existe por teléfono.
 * Precondición: teléfono >= 0
 * Complejidad temporal: O(L), siendo L el tamaño de la lista en la posición hash
 */
bool Agenda::existeContacto(long telefono) {
    int pos = obtenerPosicion(telefono);
    return tabla[pos].buscar(telefono) != nullptr;
}

/**
 * Devuelve el nombre del contacto con el teléfono indicado.
 * Lanza excepción si no existe.
 * Complejidad temporal: O(L)
 */
string Agenda::getContacto(long telefono) {
    int pos = obtenerPosicion(telefono);
    Nodo* nodo = tabla[pos].buscar(telefono);
    if (nodo == nullptr) {
        throw runtime_error("Contacto no encontrado.");
    }
    return nodo->getContacto().getNombre();
}

/**
 * Introduce un nuevo contacto.
 * Si ya existe, actualiza su nombre.
 * Complejidad temporal: O(L)
 */
/**
 * @brief Introduce un contacto en la agenda. Si el contacto ya existe, actualiza su nombre.
 * 
 * @param telefono Número de teléfono del contacto.
 * @param nombre Nombre del contacto.
 * 
 * La función busca la posición correspondiente al número de teléfono en la tabla hash.
 * Si el contacto ya existe en esa posición, actualiza su nombre. 
 * Si no existe, lo inserta como un nuevo contacto y aumenta el contador de contactos.
 */
void Agenda::introducirContacto(long telefono, string nombre) {
    int pos = obtenerPosicion(telefono);
    Nodo* nodo = tabla[pos].buscar(telefono);
    if (nodo != nullptr) {
        nodo->getContacto().setNombre(nombre);
    } else {
        tabla[pos].insertar(Contacto(telefono, nombre));
        n++;
    }
}

/**
 * Elimina un contacto con el teléfono indicado.
 * No hace nada si el contacto no existe.
 * Complejidad temporal: O(L)
 */
void Agenda::eliminarContacto(long telefono) {
    int pos = obtenerPosicion(telefono);
    if (tabla[pos].eliminar(telefono)) {
        n--;
    }
}

/**
 * Imprime la agenda.
 * No se implementa porque el corrector la proporciona.
 */
void Agenda::imprimir() {
    // No implementar
}
