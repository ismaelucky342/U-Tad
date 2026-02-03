#include "cuentaBancaria.h"
#include "gestorClientes.h"

CuentaBancaria::CuentaBancaria(){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,CuentaBancariaFD);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}		
}

CuentaBancaria::CuentaBancaria(string titular, double saldo, string numeroCuenta){
	auto conn=initClient("127.0.0.1",5000);
	vector<unsigned char> buffer;
	pack(buffer,CuentaBancariaFP);
	pack(buffer,(int)titular.size());
	packv(buffer,(char*)titular.data(),(int)titular.size());
	pack(buffer,saldo);
	pack(buffer,(int)numeroCuenta.size());
	packv(buffer,(char*)numeroCuenta.data(),(int)numeroCuenta.size());
	
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}	
}

CuentaBancaria::~CuentaBancaria(){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,CuentaBancariaFDe);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			closeConnection(conn.serverId);
			GestorClientes::connections.erase(this);
		}
	}	
}

void CuentaBancaria::setTitular(string titular){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setTitularF);
	pack(buffer,(int)titular.size());
	packv(buffer,(char*)titular.data(),(int)titular.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void CuentaBancaria::setSaldo(double saldo){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setSaldoF);
	pack(buffer,saldo);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

void CuentaBancaria::setNumeroCuenta(string numeroCuenta){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,setNumeroCuentaF);
	pack(buffer,(int)numeroCuenta.size());
	packv(buffer,(char*)numeroCuenta.data(),(int)numeroCuenta.size());
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}	
}

string CuentaBancaria::getTitular(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getTitularF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

double CuentaBancaria::getSaldo(){
	double resultado=0.0;
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getSaldoF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado=unpack<double>(buffer);
		}
	}	
	return resultado;	
}

string CuentaBancaria::getNumeroCuenta(){
	string resultado="";
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	pack(buffer,getNumeroCuentaF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
		else{
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	return resultado;
}

void CuentaBancaria::escribirAFichero(string nombreFichero){
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
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

void CuentaBancaria::leerDeFichero(string nombreFichero){
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
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
	}
}

ostream& operator<<(ostream& os, const CuentaBancaria &c)
{
	string resultado="";
	auto conn=GestorClientes::connections[(CuentaBancaria*)&c];
	vector<unsigned char> buffer;
	pack(buffer,ostreamOpF);
	sendMSG(conn.serverId, buffer);
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0){
		cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
	}
	else{	
		cuentaBancariaMSGTypes ack=unpack<cuentaBancariaMSGTypes>(buffer);
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
