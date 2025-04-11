#include <iostream>
#include "Agenda.h" //Realizar libreria similar

using namespace std;

int main() {

	int capacidad; // Capacidad de la tabla hash
	char opcion; // Opcion de menu introducida por teclado

	long telefono; // Clave para algunas opciones
	string nombre; // Nombre del contacto para la opcion de meter


	cout << "Introduce la capacidad de la tabla: ";
	cin >> capacidad;

	//Crear agenda
	//Agenda agenda(capacidad);  Realizar funcion similar


	do {
		cin >> opcion;

		switch (opcion) {
		case 'I':
			//agenda.imprimir(); Realizar funcion similar
			break;
		case 'C':
			// Comprobar si est� un contacto
			cout << "Numero de telefono del contacto ";
			cin >> telefono;
			//if (agenda.existeContacto(telefono*))  Realizar funcion similar
			if(true)
				cout << "El contacto SI esta\n";
			else 
				cout << "El contacto NO esta\n";
			break;
		case 'V':
			// Ver contacto (obtener su nombre)
			cout << "Numero de telefono del contacto: ";
			cin >> telefono;
			//cout << "Nombre: " << agenda.getContacto(telefono) << endl; Realizar funcion similar
			break;
		case 'A':
			// A�adir un contacto
			cout << "Numero de telefono del contacto: ";
			cin >> telefono;
			cout << "Nombre del contacto: ";
			cin >> nombre;
			//agenda.introducirContacto(telefono, nombre); Realizar funcion similar
			break;
		case 'E':
			// Eliminar un contacto
			cout << "Numero de telefono del contacto: ";
			cin >> telefono;
			//agenda.eliminarContacto(telefono); Realizar funcion similar
			break;
		case 'S':
		        break;
		default:
			cout << "Opcion incorrecta\n";
			break;

		} // Fin switch

	} while (opcion != 'S'); 

	return 0;
}
