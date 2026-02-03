#include "producto.h"
#include "gestorClientes.h"

Producto::Producto(){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,ProductoFD);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}		
}

Producto::Producto(string nombre, double precio, int stock, string categoria){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,ProductoFP);
	pack(buffer,(int)nombre.size());
	packv(buffer,(char*)nombre.data(),(int)nombre.size());
	pack(buffer,precio);
	pack(buffer,stock);
	pack(buffer,(int)categoria.size());
	packv(buffer,(char*)categoria.data(),(int)categoria.size());
	
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}	
}

Producto::~Producto(){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,ProductoFDe);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			closeConnection(conn.serverId);
			GestorClientes::connections.erase(this);
		}
	}	
}

void Producto::setNombre(string nombre){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setNombreF);
	pack(buffer,(int)nombre.size());
	packv(buffer,(char*)nombre.data(),(int)nombre.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Producto::setPrecio(double precio){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setPrecioF);
	pack(buffer,precio);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Producto::setStock(int stock){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setStockF);
	pack(buffer,stock);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void Producto::setCategoria(string categoria){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setCategoriaF);
	pack(buffer,(int)categoria.size());
	packv(buffer,(char*)categoria.data(),(int)categoria.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

string Producto::getNombre(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getNombreF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

double Producto::getPrecio(){
	double resultado=0.0;
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getPrecioF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado=unpack<double>(buffer);
		}
	}	
	return resultado;	
}

int Producto::getStock(){
	int resultado=0;
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getStockF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado=unpack<int>(buffer);
		}
	}	
	return resultado;	
}

string Producto::getCategoria(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getCategoriaF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

void Producto::escribirAFichero(string nombreFichero){
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
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

void Producto::leerDeFichero(string nombreFichero){
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
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

ostream& operator<<(ostream& os, const Producto &p)
{
	string resultado="";
	auto conn=GestorClientes::connections[(Producto*)&p];
	vector<unsigned char> buffer;
	pack(buffer,ostreamOpF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		productoMSGTypes ack=unpack<productoMSGTypes>(buffer);
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
