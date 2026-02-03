#pragma once
#include "utils.h"
#include "cuentaBancaria.h"

using namespace std;

typedef enum{
	CuentaBancariaFD,    // constructor por defecto
	CuentaBancariaFP,    // constructor con parametros
	CuentaBancariaFDe,   // destructor de cuenta
	setTitularF,         // métodos set/get
	setSaldoF,
	setNumeroCuentaF,
	getTitularF,
	getSaldoF,
	getNumeroCuentaF,
	ostreamOpF,          // método "operator <<"
	escribirAFicheroF,   // método para escribir datos a fichero
	leerDeFicheroF,      // método para leer datos de fichero
	ackMSG               // mensaje extra de confirmación
}cuentaBancariaMSGTypes;

class GestorClientes{
	
	public:
	// Usado por el cliente
	// Mapa para almacenar y buscar datos de conexión
		static inline map<CuentaBancaria*,connection_t > connections;
	// Usado por el servidor
	// Mapa para almacenar y buscar cuentas reservadas por clientes
		static inline map<int,CuentaBancaria > clients; 
	// Método usado por el servidor para gestionar peticiones de invocación
	// de métodos recibido de programas tipo cliente.
		static void atiendeCliente(int clientId);
};
