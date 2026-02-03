#include "gestorClientes.h"
#include <sstream>      

void GestorClientes::atiendeCliente(int clientId){
	bool salir=false;
	vector<unsigned char> buffer;
	
	while(!salir)
	{
		recvMSG(clientId,buffer);
		auto tipo=unpack<cuentaBancariaMSGTypes>(buffer);
		
		switch(tipo){
			case CuentaBancariaFD:{
				CuentaBancaria c;
				clients[clientId]=c;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case CuentaBancariaFP:{
				string titular, numeroCuenta;
				double saldo;
				
				titular.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)titular.data(),(int)titular.size());
				
				saldo=unpack<double>(buffer);
				
				numeroCuenta.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)numeroCuenta.data(),(int)numeroCuenta.size());
				
				CuentaBancaria c(titular, saldo, numeroCuenta);
				clients[clientId]=c;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case CuentaBancariaFDe:{
				clients.erase(clientId);
				salir=true;
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setTitularF:{
				string titular;
				titular.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)titular.data(),(int)titular.size());
				clients[clientId].setTitular(titular);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setSaldoF:{
				double saldo;
				saldo=unpack<double>(buffer);
				clients[clientId].setSaldo(saldo);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case setNumeroCuentaF:{
				string numeroCuenta;
				numeroCuenta.resize(unpack<int>(buffer));
				unpackv<char>(buffer,(char*)numeroCuenta.data(),(int)numeroCuenta.size());
				clients[clientId].setNumeroCuenta(numeroCuenta);
				buffer.clear();
				pack(buffer,ackMSG);
			}break;
			
			case getTitularF:{
				string titular=clients[clientId].getTitular();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)titular.size());
				packv(buffer,(char*)titular.data(),(int)titular.size());
			}break;
			
			case getSaldoF:{
				double saldo=clients[clientId].getSaldo();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,saldo);
			}break;
			
			case getNumeroCuentaF:{
				string numeroCuenta=clients[clientId].getNumeroCuenta();
				buffer.clear();
				pack(buffer,ackMSG);
				pack(buffer,(int)numeroCuenta.size());
				packv(buffer,(char*)numeroCuenta.data(),(int)numeroCuenta.size());
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
