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

#include "../../includes/ListaEnlazada.h"

/** Constructor de la clase ListaEnlazada.
 *  Inicializa la cabeza de la lista como un puntero nulo.
 */
ListaEnlazada::ListaEnlazada() : cabeza(nullptr) {}

/** Destructor de la clase ListaEnlazada.
 *  Libera la memoria de todos los nodos en la lista.
 */
ListaEnlazada::~ListaEnlazada() {
    Nodo* actual = cabeza;
    while (actual) {
        Nodo* siguiente = actual->getSiguiente();
        delete actual; // Libera la memoria del nodo actual.
        actual = siguiente; // Avanza al siguiente nodo.
    }
}

/** Inserta un nuevo contacto al inicio de la lista.
 *  @param contacto El contacto que se desea insertar.
 */
void ListaEnlazada::insertar(Contacto contacto) {
    Nodo* nuevo = new Nodo(contacto); // Crea un nuevo nodo con el contacto.
    nuevo->setSiguiente(cabeza); // El nuevo nodo apunta al nodo actual de la cabeza.
    cabeza = nuevo; // Actualiza la cabeza para que apunte al nuevo nodo.
}

/** Busca un nodo en la lista por el número de teléfono.
 *  @param telefono El número de teléfono del contacto a buscar.
 *  @return Un puntero al nodo que contiene el contacto, o nullptr si no se encuentra.
 */
Nodo* ListaEnlazada::buscar(long telefono) {
    Nodo* actual = cabeza;
    while (actual) {
        if (actual->getContacto().getTelefono() == telefono) {
            return actual; // Retorna el nodo si se encuentra el contacto.
        }
        actual = actual->getSiguiente(); // Avanza al siguiente nodo.
    }
    return nullptr; // Retorna nullptr si no se encuentra el contacto.
}

/** Elimina un nodo de la lista por el número de teléfono.
 *  @param telefono El número de teléfono del contacto a eliminar.
 *  @return true si el nodo fue eliminado, false si no se encontró.
 */
bool ListaEnlazada::eliminar(long telefono) {
    Nodo* actual = cabeza;
    Nodo* anterior = nullptr;

    while (actual) {
        if (actual->getContacto().getTelefono() == telefono) {
            if (anterior) {
                anterior->setSiguiente(actual->getSiguiente()); // Salta el nodo actual.
            } else {
                cabeza = actual->getSiguiente(); // Actualiza la cabeza si es el primer nodo.
            }
            delete actual; // Libera la memoria del nodo eliminado.
            return true; // Indica que el nodo fue eliminado.
        }
        anterior = actual; // Guarda el nodo actual como anterior.
        actual = actual->getSiguiente(); // Avanza al siguiente nodo.
    }
    return false; // Retorna false si no se encontró el nodo.
}
