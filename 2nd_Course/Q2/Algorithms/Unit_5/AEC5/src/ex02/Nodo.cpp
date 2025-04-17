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

#include "../../includes/Nodo.h"

/**
 * Constructor de la clase Nodo.
 * @param contacto Objeto de tipo Contacto que se asignará al nodo.
 */
Nodo::Nodo(Contacto contacto) : contacto(contacto), siguiente(nullptr) {}

/**
 * Obtiene una referencia al objeto Contacto almacenado en el nodo.
 * @return Referencia al objeto Contacto.
 */
Contacto& Nodo::getContacto() {
    return contacto;
}

/**
 * Obtiene un puntero al siguiente nodo en la lista.
 * @return Puntero al siguiente nodo.
 */
Nodo* Nodo::getSiguiente() {
    return siguiente;
}

/**
 * Establece el puntero al siguiente nodo en la lista.
 * @param siguiente Puntero al nodo que será el siguiente.
 */
void Nodo::setSiguiente(Nodo* siguiente) {
    this->siguiente = siguiente;
}
