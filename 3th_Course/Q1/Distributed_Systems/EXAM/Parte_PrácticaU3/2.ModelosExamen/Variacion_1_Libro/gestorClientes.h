#pragma once
#include "utils.h"
#include "libro.h"

using namespace std;

typedef enum{
	LibroFD,        // constructor por defecto
	LibroFP,        // constructor con parametros
	LibroFDe,       // destructor de libro
	setTituloF,     // métodos set/get
	setAutorF,
	setNumPaginasF,
	getTituloF,
	getAutorF,
	getNumPaginasF,
	ostreamOpF,     // método "operator <<"
	escribirAFicheroF,  // método para escribir datos a fichero
	leerDeFicheroF,     // método para leer datos de fichero
	ackMSG          // mensaje extra de confirmación
}libroMSGTypes;

class GestorClientes{
	
	public:
	// Usado por el cliente
	// Mapa para almacenar y buscar datos de conexión
		static inline map<Libro*,connection_t > connections;
	// Usado por el servidor
	// Mapa para almacenar y buscar libros reservados por clientes
		static inline map<int,Libro > clients; 
	// Método usado por el servidor para gestionar peticiones de invocación
	// de métodos recibido de programas tipo cliente.
		static void atiendeCliente(int clientId);
};
