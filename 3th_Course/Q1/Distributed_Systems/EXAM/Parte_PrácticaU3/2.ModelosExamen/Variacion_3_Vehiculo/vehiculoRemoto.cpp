#include "vehiculo.h"
#include "gestorClientes.h"

Vehiculo::Vehiculo(){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,VehiculoFD);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}		
}

Vehiculo::Vehiculo(string marca, string modelo, int anio, int kilometraje){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,VehiculoFP);
	pack(buffer,(int)marca.size());
	packv(buffer,(char*)marca.data(),(int)marca.size());
	pack(buffer,(int)modelo.size());
	packv(buffer,(char*)modelo.data(),(int)modelo.size());
	pack(buffer,anio);
	pack(buffer,kilometraje);
	
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}	
}

Vehiculo::~Vehiculo(){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,VehiculoFDe);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			closeConnection(conn.serverId);
			GestorClientes::connections.erase(this);
		}
	}	
}

void Vehiculo::setMarca(string marca){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setMarcaF);
	pack(buffer,(int)marca.size());
	packv(buffer,(char*)marca.data(),(int)marca.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Vehiculo::setModelo(string modelo){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setModeloF);
	pack(buffer,(int)modelo.size());
	packv(buffer,(char*)modelo.data(),(int)modelo.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Vehiculo::setAnio(int anio){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setAnioF);
	pack(buffer,anio);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Vehiculo::setKilometraje(int kilometraje){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setKilometrajeF);
	pack(buffer,kilometraje);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

string Vehiculo::getMarca(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getMarcaF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

string Vehiculo::getModelo(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getModeloF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

int Vehiculo::getAnio(){
	int resultado=0;
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getAnioF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado=unpack<int>(buffer);
		}
	}	
	return resultado;	
}

int Vehiculo::getKilometraje(){
	int resultado=0;
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getKilometrajeF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado=unpack<int>(buffer);
		}
	}	
	return resultado;	
}

void Vehiculo::escribirAFichero(string nombreFichero){
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
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

void Vehiculo::leerDeFichero(string nombreFichero){
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
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

ostream& operator<<(ostream& os, const Vehiculo &v)
{
	string resultado="";
	auto conn=GestorClientes::connections[(Vehiculo*)&v];
	vector<unsigned char> buffer;
	pack(buffer,ostreamOpF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		vehiculoMSGTypes ack=unpack<vehiculoMSGTypes>(buffer);
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
