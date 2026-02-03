#pragma once
#include "utils.h"
#include "vehiculo.h"

using namespace std;

typedef enum{
	VehiculoFD,        // constructor por defecto
	VehiculoFP,        // constructor con parametros
	VehiculoFDe,       // destructor de vehiculo
	setMarcaF,         // métodos set/get
	setModeloF,
	setAnioF,
	setKilometrajeF,
	getMarcaF,
	getModeloF,
	getAnioF,
	getKilometrajeF,
	ostreamOpF,        // método "operator <<"
	escribirAFicheroF, // método para escribir datos a fichero
	leerDeFicheroF,    // método para leer datos de fichero
	ackMSG             // mensaje extra de confirmación
}vehiculoMSGTypes;

class GestorClientes{
	
	public:
	// Usado por el cliente
	// Mapa para almacenar y buscar datos de conexión
		static inline map<Vehiculo*,connection_t > connections;
	// Usado por el servidor
	// Mapa para almacenar y buscar vehículos reservados por clientes
		static inline map<int,Vehiculo > clients; 
	// Método usado por el servidor para gestionar peticiones de invocación
	// de métodos recibido de programas tipo cliente.
		static void atiendeCliente(int clientId);
};
