#pragma once
#include "utils.h"
#include "producto.h"

using namespace std;

typedef enum{
	ProductoFD,        // constructor por defecto
	ProductoFP,        // constructor con parametros
	ProductoFDe,       // destructor de producto
	setNombreF,        // métodos set/get
	setPrecioF,
	setStockF,
	setCategoriaF,
	getNombreF,
	getPrecioF,
	getStockF,
	getCategoriaF,
	ostreamOpF,        // método "operator <<"
	escribirAFicheroF, // método para escribir datos a fichero
	leerDeFicheroF,    // método para leer datos de fichero
	ackMSG             // mensaje extra de confirmación
}productoMSGTypes;

class GestorClientes{
	
	public:
	// Usado por el cliente
	// Mapa para almacenar y buscar datos de conexión
		static inline map<Producto*,connection_t > connections;
	// Usado por el servidor
	// Mapa para almacenar y buscar productos reservados por clientes
		static inline map<int,Producto > clients; 
	// Método usado por el servidor para gestionar peticiones de invocación
	// de métodos recibido de programas tipo cliente.
		static void atiendeCliente(int clientId);
};
