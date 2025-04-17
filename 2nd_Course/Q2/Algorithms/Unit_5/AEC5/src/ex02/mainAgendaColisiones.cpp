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
#include "Agenda.h"

using namespace std;

void mostrarMenu() {
    cout << CYAN << "\n===== AGENDA TELEFÓNICA =====\n" << RESET;
    cout << YELLOW << "I" << RESET << " - Imprimir agenda\n";
    cout << YELLOW << "C" << RESET << " - Comprobar contacto\n";
    cout << YELLOW << "V" << RESET << " - Ver contacto\n";
    cout << YELLOW << "A" << RESET << " - Añadir contacto\n";
    cout << YELLOW << "E" << RESET << " - Eliminar contacto\n";
    cout << YELLOW << "S" << RESET << " - Salir\n";
    cout << "Elige una opción: ";
}

int main() {
    int capacidad;
    char opcion;
    long telefono;
    string nombre;

    cout << "Introduce la capacidad de la tabla: ";
    cin >> capacidad;
    Agenda agenda(capacidad);

    do {
        mostrarMenu();
        cin >> opcion;
        opcion = toupper(opcion);

        switch (opcion) {
        case 'I':
            agenda.imprimir();
            break;
        case 'C':
            cout << "Introduce el número de teléfono: ";
            cin >> telefono;
            if (agenda.existeContacto(telefono))
                cout << GREEN << "El contacto SÍ está.\n" << RESET;
            else
                cout << RED << "El contacto NO está.\n" << RESET;
            break;
        case 'V':
            cout << "Introduce el número de teléfono: ";
            cin >> telefono;
            try {
                cout << "Nombre: " << agenda.getContacto(telefono) << endl;
            } catch (const exception& e) {
                cout << RED << "Error: " << e.what() << endl << RESET;
            }
            break;
        case 'A':
            cout << "Introduce el número de teléfono: ";
            cin >> telefono;
            cout << "Introduce el nombre: ";
            cin.ignore();
            getline(cin, nombre);
            agenda.introducirContacto(telefono, nombre);
            cout << GREEN << "Contacto añadido correctamente.\n" << RESET;
            break;
        case 'E':
            cout << "Introduce el número de teléfono: ";
            cin >> telefono;
            agenda.eliminarContacto(telefono);
            cout << RED << "Contacto eliminado (si existía).\n" << RESET;
            break;
        case 'S':
            cout << CYAN << "Saliendo de la agenda...\n" << RESET;
            break;
        default:
            cout << RED << "Opción no válida.\n" << RESET;
        }

    } while (opcion != 'S');

    return 0;
}
