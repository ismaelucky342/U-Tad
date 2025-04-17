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

#include "../../includes/Agenda.h"

using namespace std;

/**
 * Constructor de la clase Agenda.
 * @param capacidad Capacidad máxima de la agenda.
 */
Agenda::Agenda(int capacidad) {
    this->capacidad = capacidad;
    nombres = new string[capacidad];
    telefonos = new long[capacidad];
    ocupados = new bool[capacidad];

    for (int i = 0; i < capacidad; i++) {
        ocupados[i] = false;
    }
}

/**
 * Destructor de la clase Agenda.
 * Libera la memoria dinámica utilizada.
 */
Agenda::~Agenda() {
    delete[] nombres;
    delete[] telefonos;
    delete[] ocupados;
}

/**
 * Obtiene la posición en la agenda para un número de teléfono.
 * @param telefono Número de teléfono.
 * @return Posición calculada en la agenda.
 */
int Agenda::obtenerPosicion(long telefono) {
    return telefono % capacidad;
}

/**
 * Verifica si un contacto existe en la agenda.
 * @param telefono Número de teléfono del contacto.
 * @return true si el contacto existe, false en caso contrario.
 */
bool Agenda::existeContacto(long telefono) {
    int pos = obtenerPosicion(telefono);
    return ocupados[pos] && telefonos[pos] == telefono;
}

/**
 * Obtiene el nombre del contacto asociado a un número de teléfono.
 * @param telefono Número de teléfono del contacto.
 * @return Nombre del contacto o "Contacto no encontrado" si no existe.
 */
string Agenda::getContacto(long telefono) {
    int pos = obtenerPosicion(telefono);
    if (ocupados[pos] && telefonos[pos] == telefono) {
        return nombres[pos];
    } else {
        return "Contacto no encontrado";
    }
}

/**
 * Introduce un nuevo contacto en la agenda.
 * @param telefono Número de teléfono del contacto.
 * @param contacto Nombre del contacto.
 */
void Agenda::introducirContacto(long telefono, string contacto) {
    int pos = obtenerPosicion(telefono);
    if (!ocupados[pos]) {
        nombres[pos] = contacto;
        telefonos[pos] = telefono;
        ocupados[pos] = true;
    } else {
        cout << "Colisión detectada: no se puede insertar el contacto." << endl;
    }
}

/**
 * Elimina un contacto de la agenda.
 * @param telefono Número de teléfono del contacto a eliminar.
 */
void Agenda::eliminarContacto(long telefono) {
    int pos = obtenerPosicion(telefono);
    if (ocupados[pos] && telefonos[pos] == telefono) {
        ocupados[pos] = false;
    }
}

/**
 * Imprime la agenda.
 * Nota: Este método no está implementado.
 */
void Agenda::imprimir() {
   // no implementar
}