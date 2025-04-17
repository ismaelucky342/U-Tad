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

#include <iostream>
#include "../../includes/Agenda.h"

using namespace std;

void mostrarMenu() {
    cout << CYAN << "\n=== MENÚ DE AGENDA ===" << RESET << endl;
    cout << GREEN << "I" << RESET << " - Imprimir toda la tabla hash" << endl;
    cout << GREEN << "C" << RESET << " - Comprobar si un contacto existe" << endl;
    cout << GREEN << "V" << RESET << " - Ver nombre de un contacto" << endl;
    cout << GREEN << "A" << RESET << " - Añadir un contacto" << endl;
    cout << GREEN << "E" << RESET << " - Eliminar un contacto" << endl;
    cout << GREEN << "S" << RESET << " - Salir" << endl;
    cout << MAGENTA << "Seleccione una opción: " << RESET;
}

int main() {
    int capacidad;
    char opcion;
    long telefono;
    string nombre;

    cout << YELLOW << "Introduce la capacidad de la tabla: " << RESET;
    cin >> capacidad;

    Agenda agenda(capacidad);

    do {
        mostrarMenu();
        cin >> opcion;
        opcion = toupper(opcion);

        switch (opcion) {
            case 'I':
                cout << BLUE << "\n=== CONTENIDO DE LA AGENDA ===\n" << RESET;
                agenda.imprimir();
                break;

            case 'C':
                cout << YELLOW << "Número de teléfono del contacto: " << RESET;
                cin >> telefono;
                if (agenda.existeContacto(telefono)) {
                    cout << GREEN << "El contacto SÍ está en la agenda.\n" << RESET;
                } else {
                    cout << RED << "El contacto NO está en la agenda.\n" << RESET;
                }
                break;

            case 'V':
                cout << YELLOW << "Número de teléfono del contacto: " << RESET;
                cin >> telefono;
                cout << CYAN << "Nombre: " << agenda.getContacto(telefono) << "\n" << RESET;
                break;

            case 'A':
                cout << YELLOW << "Número de teléfono del contacto: " << RESET;
                cin >> telefono;
                cout << YELLOW << "Nombre del contacto: " << RESET;
                cin >> nombre;
                agenda.introducirContacto(telefono, nombre);
                break;

            case 'E':
                cout << YELLOW << "Número de teléfono del contacto: " << RESET;
                cin >> telefono;
                agenda.eliminarContacto(telefono);
                cout << RED << "Contacto eliminado (si existía).\n" << RESET;
                break;

            case 'S':
                cout << GREEN << "Saliendo del programa...\n" << RESET;
                break;

            default:
                cout << RED << "Opción incorrecta. Intente de nuevo.\n" << RESET;
                break;
        }

    } while (opcion != 'S');

    return 0;
}