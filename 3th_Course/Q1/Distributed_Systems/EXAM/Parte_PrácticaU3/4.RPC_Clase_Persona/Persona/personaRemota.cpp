#include "persona.h"
#include "gestorClientes.h"
		
		

Persona::Persona(){
	//iniciar conexion
	auto conn=initClient("127.0.0.1",5000);

	//invocar constructor en server:
		//crear buffer
	vector<unsigned char> buffer;
		//empaquetar tipo de llamada constructor por defecto de persona
	pack(buffer,PersonaFD);
		//mandar mensaje
	sendMSG(conn.serverId, buffer);
		//esperar confirmación de ejecución
	buffer.clear(); //limpiar buffer antes de reutilizarlo
	recvMSG(conn.serverId,buffer); //recibir respuesta de servidor
	
	if(buffer.size()==0) //Error estándar, no hay datos recibidos
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl; //Mensaje estándar error
	}
	else{//Debería haber un mensaje, debe ser un ACK	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		//si no recibo confirmación
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;	
		//error
		else{ 
			//Todo correcto, se almancena esta conexión y devuelve el control
			//a programa main
			GestorClientes::connections[this]=conn;
		}
	}		
}
Persona::Persona(string nombre,int edad){
		//iniciar conexion
	auto conn=initClient("127.0.0.1",5000);

	//invocar constructor en server:
		//buffer
	vector<unsigned char> buffer;
		//empaquetar tipo de llamada constructor con parametros
	pack(buffer,PersonaFP);
	pack(buffer,(int)nombre.size());//Empaquetar tamaño de nombre
	packv(buffer,(char*)nombre.data(),(int)nombre.size()); //Empaquetar letras del nombre (data())
	pack(buffer,(int)edad);//Empaquetar Edad
	
		//mandar mensaje
	sendMSG(conn.serverId, buffer);
		//esperar confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<	"Tipo de mensaje inválido"<<endl;	
		else{
			GestorClientes::connections[this]=conn;
		}
	}	
	
	
}

Persona::~Persona(){
	//Buscar datos de conexión
	auto conn=GestorClientes::connections[this];
	
	vector<unsigned char> buffer;
	//Empaquetar invocación de destructor
	pack(buffer,PersonaFDe);
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
		else{
			//si todo es correcto, cerrar conexión
			closeConnection(conn.serverId);
			//eliminar datos de conexión
			GestorClientes::connections.erase(this);
		}
	}	
}

void Persona::setEdad(int edad){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	//Empaquetar invocación de setEdad
	pack(buffer,setEdadF);
	pack(buffer,(int)edad);
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
	}	
}

void Persona::setNombre(string nombre){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	//Empaquetar invocación de setNombre
	pack(buffer,setNombreF);
	pack(buffer,(int)nombre.size());
	packv(buffer,(char*)nombre.data(),(int)nombre.size());
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
	}	
}

int  Persona::getEdad(){
	int resultado=0;
//Buscar datos de conexión
	auto conn=GestorClientes::connections[this];
	
	vector<unsigned char> buffer;
	//Empaquetar invocación de getEdad
	pack(buffer,getEdadF);
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
		else{
			//si todo es correcto, desempaquetar datos
			resultado=unpack<int>(buffer);
		}
	}	
	//siempre devuelve un resultado
	return resultado;	
}

string Persona::getNombre(){
	string resultado="";
//Buscar datos de conexión
	auto conn=GestorClientes::connections[this];
	
	vector<unsigned char> buffer;
	//Empaquetar invocación de getNombre
	pack(buffer,getNombreF);
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
		else{
			//si todo es correcto, desempaquetar datos
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
		}
	}	
	//siempre devuelve un resultado
	return resultado;
}


void Persona::escribirAFichero(string nombreFichero){
	
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	//Empaquetar invocación de setNombre
	pack(buffer,escribirAFicheroF);
	pack(buffer,(int)nombreFichero.size());
	packv(buffer,(char*)nombreFichero.data(),(int)nombreFichero.size());
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
	}
}


void Persona::leerDeFichero(string nombreFichero){
	auto conn=GestorClientes::connections[this];
	vector<unsigned char> buffer;
	//Empaquetar invocación de setNombre
	pack(buffer,leerDeFicheroF);
	pack(buffer,(int)nombreFichero.size());
	packv(buffer,(char*)nombreFichero.data(),(int)nombreFichero.size());
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
	}
}

ostream& operator<<(ostream& os,const Persona &p)
{
	string resultado="";
//Buscar datos de conexión
	auto conn=GestorClientes::connections[(Persona*)&p];
	
	vector<unsigned char> buffer;
	//Empaquetar invocación de ostreamOpF
	pack(buffer,ostreamOpF);
	//Enviar
	sendMSG(conn.serverId, buffer);
	//recibir confirmación de ejecución
	buffer.clear();
	recvMSG(conn.serverId,buffer);
	
	if(buffer.size()==0)
	{
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tamaño de mensaje inválido"<<endl;							//error
	}
	else{	
		personaMSGTypes ack=unpack<personaMSGTypes>(buffer);
		if(ack!=ackMSG)
			cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
		else{
			//si todo es correcto, desempaquetar datos
			resultado.resize(unpack<int>(buffer));
			unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
			//redirigir resultado a la salida por terminal
			os<<resultado;
		}
	}	
	//siempre devuelve un resultado
    return os;
}




