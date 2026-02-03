#include "gestorClientes.h"
#include <sstream>      

void GestorClientes::atiendeCliente(int clientId){
	bool salir=false;
	vector<unsigned char> buffer;
	
	while(!salir)
	{
		recvMSG(clientId,buffer);
		auto tipo=unpack<vehiculoMSGTypes>(buffer);
		
		switch(tipo){
			case VehiculoFD:{
				Vehiculo v;
				clients[clientId]=v;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case VehiculoFP:{
				string marca, modelo;
				int anio, kilometraje;
				
				marca.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)marca.data(),(int)marca.size());
				
				modelo.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)modelo.data(),(int)modelo.size());
				
				anio=unpack<int>(buffer);
				kilometraje=unpack<int>(buffer);
				
				Vehiculo v(marca, modelo, anio, kilometraje);
				clients[clientId]=v;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case VehiculoFDe:{
				clients.erase(clientId);
				salir=true;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setMarcaF:{
				string marca;
				marca.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)marca.data(),(int)marca.size());
				clients[clientId].setMarca(marca);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setModeloF:{
				string modelo;
				modelo.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)modelo.data(),(int)modelo.size());
				clients[clientId].setModelo(modelo);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setAnioF:{
				int anio;
				anio=unpack<int>(buffer);
				clients[clientId].setAnio(anio);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setKilometrajeF:{
				int kilometraje;
				kilometraje=unpack<int>(buffer);
				clients[clientId].setKilometraje(kilometraje);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case getMarcaF:{
				string marca=clients[clientId].getMarca();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)marca.size());
				packv(buffer,(char*)marca.data(),(int)marca.size());
			}break;
			
			case getModeloF:{
				string modelo=clients[clientId].getModelo();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)modelo.size());
				packv(buffer,(char*)modelo.data(),(int)modelo.size());
			}break;
			
			case getAnioF:{
				int anio=clients[clientId].getAnio();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,anio);
			}break;
			
			case getKilometrajeF:{
				int kilometraje=clients[clientId].getKilometraje();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,kilometraje);
			}break;
			
			case ostreamOpF:{
				std::ostringstream ss;
				ss << clients[clientId];
				string result = ss.str();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)result.size());
				packv(buffer,(char*)result.data(),(int)result.size());
			}break;
			
			case escribirAFicheroF:{
				string fichero;
				fichero.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)fichero.data(),(int)fichero.size());
				clients[clientId].escribirAFichero(fichero);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case leerDeFicheroF:{
				string fichero;
				fichero.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)fichero.data(),(int)fichero.size());
				clients[clientId].leerDeFichero(fichero);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case ackMSG:
			default:
			{
				cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
			}break;
		};
		sendMSG(clientId,buffer);
	}
	closeConnection(clientId);
}
