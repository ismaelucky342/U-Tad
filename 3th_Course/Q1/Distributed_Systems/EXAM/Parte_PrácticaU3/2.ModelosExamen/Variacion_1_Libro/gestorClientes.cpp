#include "gestorClientes.h"
#include <sstream>      

void GestorClientes::atiendeCliente(int clientId){
	bool salir=false;
	vector<unsigned char> buffer;
	
	while(!salir)
	{
		recvMSG(clientId,buffer);
		auto tipo=unpack<libroMSGTypes>(buffer);
		
		switch(tipo){
			case LibroFD:{
				Libro l;
				clients[clientId]=l;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case LibroFP:{
				string titulo, autor;
				int numPaginas;
				
				titulo.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)titulo.data(),(int)titulo.size());
				
				autor.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)autor.data(),(int)autor.size());
				
				numPaginas=unpack<int>(buffer);
				
				Libro l(titulo, autor, numPaginas);
				clients[clientId]=l;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case LibroFDe:{
				clients.erase(clientId);
				salir=true;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setTituloF:{
				string titulo;
				titulo.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)titulo.data(),(int)titulo.size());
				clients[clientId].setTitulo(titulo);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setAutorF:{
				string autor;
				autor.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)autor.data(),(int)autor.size());
				clients[clientId].setAutor(autor);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setNumPaginasF:{
				int numPaginas;
				numPaginas=unpack<int>(buffer);
				clients[clientId].setNumPaginas(numPaginas);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case getTituloF:{
				string titulo=clients[clientId].getTitulo();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)titulo.size());
				packv(buffer,(char*)titulo.data(),(int)titulo.size());
			}break;
			
			case getAutorF:{
				string autor=clients[clientId].getAutor();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)autor.size());
				packv(buffer,(char*)autor.data(),(int)autor.size());
			}break;
			
			case getNumPaginasF:{
				int numPaginas=clients[clientId].getNumPaginas();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,numPaginas);
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
