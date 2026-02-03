#include "libro.h"
#include "gestorClientes.h"

Libro::Libro(){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,LibroFD);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}		
}

Libro::Libro(string titulo, string autor, int numPaginas){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,LibroFP);
	pack(buffer,(int)titulo.size());
	packv(buffer,(char*)titulo.data(),(int)titulo.size());
	pack(buffer,(int)autor.size());
	packv(buffer,(char*)autor.data(),(int)autor.size());
	pack(buffer,(int)numPaginas);
	
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}	
}

Libro::~Libro(){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,LibroFDe);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			closeConnection(conn.serverId);
			GestorClientes::connections.erase(this);
		}
	}	
}

void Libro::setTitulo(string titulo){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setTituloF);
	pack(buffer,(int)titulo.size());
	packv(buffer,(char*)titulo.data(),(int)titulo.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Libro::setAutor(string autor){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setAutorF);
	pack(buffer,(int)autor.size());
	packv(buffer,(char*)autor.data(),(int)autor.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Libro::setNumPaginas(int numPaginas){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setNumPaginasF);
	pack(buffer,(int)numPaginas);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

string Libro::getTitulo(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getTituloF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

string Libro::getAutor(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getAutorF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

int Libro::getNumPaginas(){
	int resultado=0;
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getNumPaginasF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado=unpack<int>(buffer);
		}
	}	
	return resultado;	
}

void Libro::escribirAFichero(string nombreFichero){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,escribirAFicheroF);
	pack(buffer,(int)nombreFichero.size());
	packv(buffer,(char*)nombreFichero.data(),(int)nombreFichero.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

void Libro::leerDeFichero(string nombreFichero){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,leerDeFicheroF);
	pack(buffer,(int)nombreFichero.size());
	packv(buffer,(char*)nombreFichero.data(),(int)nombreFichero.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

ostream& operator<<(ostream& os, const Libro &l)
{
	string resultado="";
	auto conn=GestorClientes::connections[(Libro*)&l];
	vector<unsigned char> buffer;
	pack(buffer,ostreamOpF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
			os<<resultado;
		}
	}	
    return os;
}
