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

#include "../../includes/Contacto.h"

/* Constructor de la clase Contacto
// @param telefono Número de teléfono del contacto
// @param nombre Nombre del contacto*/
Contacto::Contacto(long telefono, std::string nombre) {
    this->telefono = telefono; 
    this->nombre = nombre;
}

// Método getter para obtener el número de teléfono del contacto
// @return Número de teléfono del contacto
long Contacto::getTelefono() const {
    return telefono;
}

// Método getter para obtener el nombre del contacto
// @return Nombre del contacto
std::string Contacto::getNombre() const {
    return nombre;
}

// Método setter para modificar el nombre del contacto
// @param nuevoNombre Nuevo nombre del contacto
void Contacto::setNombre(std::string nuevoNombre) {
    nombre = nuevoNombre;
}
