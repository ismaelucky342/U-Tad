#include "gestorClientes.h"
#include <sstream>      

void GestorClientes::atiendeCliente(int clientId){
	bool salir=false;
	vector<unsigned char> buffer;
	
	while(!salir)
	{
		recvMSG(clientId,buffer);
		auto tipo=unpack<productoMSGTypes>(buffer);
		
		switch(tipo){
			case ProductoFD:{
				Producto p;
				clients[clientId]=p;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case ProductoFP:{
				string nombre, categoria;
				double precio;
				int stock;
				
				nombre.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)nombre.data(),(int)nombre.size());
				
				precio=unpack<double>(buffer);
				stock=unpack<int>(buffer);
				
				categoria.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)categoria.data(),(int)categoria.size());
				
				Producto p(nombre, precio, stock, categoria);
				clients[clientId]=p;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case ProductoFDe:{
				clients.erase(clientId);
				salir=true;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setNombreF:{
				string nombre;
				nombre.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)nombre.data(),(int)nombre.size());
				clients[clientId].setNombre(nombre);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setPrecioF:{
				double precio;
				precio=unpack<double>(buffer);
				clients[clientId].setPrecio(precio);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setStockF:{
				int stock;
				stock=unpack<int>(buffer);
				clients[clientId].setStock(stock);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setCategoriaF:{
				string categoria;
				categoria.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)categoria.data(),(int)categoria.size());
				clients[clientId].setCategoria(categoria);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case getNombreF:{
				string nombre=clients[clientId].getNombre();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)nombre.size());
				packv(buffer,(char*)nombre.data(),(int)nombre.size());
			}break;
			
			case getPrecioF:{
				double precio=clients[clientId].getPrecio();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,precio);
			}break;
			
			case getStockF:{
				int stock=clients[clientId].getStock();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,stock);
			}break;
			
			case getCategoriaF:{
				string categoria=clients[clientId].getCategoria();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)categoria.size());
				packv(buffer,(char*)categoria.data(),(int)categoria.size());
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
