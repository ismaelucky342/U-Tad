#pragma once
#include "utils.h"
#include "persona.h"

using namespace std;

typedef enum{
	PersonaFD, //constructor por defecto
	PersonaFP, //constructor con parametros
	PersonaFDe,//destructor de persona
	setEdadF, //métodos set/get
	setNombreF,
	getEdadF,
	getNombreF,
	ostreamOpF,//método "operator <<"
	escribirAFicheroF,//método para escribir datos a fichero
	leerDeFicheroF,//método para leer datos de fichero
	ackMSG //mensaje extra de confirmación
}personaMSGTypes;

class GestorClientes{
	
	public:
	//Usado por el cliente
	//Mapa para almacenar y buscar datos de conexión
		static inline map<Persona*,connection_t > connections;
	//Usado por el servidor
	//Mapa para almacenar y buscar personas reservadas por clientes
		static inline map<int,Persona > clients; 
	//Método usado por el servidor para gestionar peticiones de invocación
	//de métodos recibido de programas tipo cliente.
	//Cada nuevo cliente conectado al sistema lleva asociado un "clientId" que 
	//se usará en sus comunicaciones
		static void atiendeCliente(int clientId);
};

