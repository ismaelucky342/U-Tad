#include "gestorClientes.h"
#include <sstream>      

void GestorClientes::atiendeCliente(int clientId){
	bool salir=false;
	vector<unsigned char> buffer;//Buffer de datos recibidos desde le cliente
	//Mantener la conexión hasta que el cliente invoque el destructor
	while(!salir)
	{
		//recibir mensaje
		recvMSG(clientId,buffer);
		//tratar mensaje
		//desempaquetar tipo de invocación
		auto tipo=unpack<personaMSGTypes>(buffer);
		//swith tipo
		switch(tipo){ //crear un caso para cada tipo de mensaje
			case PersonaFD:{
				//crear una persona llamando al constructor por defecto
				Persona p;
				//almacenar la persona usando el identificador de cliente
				//para poder referenciarlo en el resto de llamadas
				clients[clientId]=p;
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case
			}break;
			case PersonaFP:{
				string nombre; //Variables para almacenar nombre/edad
				int edad;
				//Reconstruimos el nombre desempaquetando sus datos
				//- Desempaquetamos y redimensionamos el tamaño del nombre
				nombre.resize(unpack<int>(buffer));
				//- Desempaquetamos datos/caracteres del nombre
				unpackv<char>(buffer,(char*)nombre.data(),(int)nombre.size());
				//desempaquetamos la edad, que es un dato integer
				edad=unpack<int>(buffer);
				//crear una persona llamando al constructor con parámetros
				Persona p(nombre,edad);
				//almacenar la persona usando el identificador de cliente
				//para poder referenciarlo en el resto de llamadas
				clients[clientId]=p;
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case
				
			}break;
			case PersonaFDe:{
				//Invocamos el destructor eliminando la instancia de persona
				//de la lista de clientes
				clients.erase(clientId);
				//acabamos el bucle "while" que mantiene la conexión con el cliente
				salir=true;
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case
			}break;
			case setEdadF:{
				int edad;
				//desempaquetamos la edad, que es un dato integer
				edad=unpack<int>(buffer);
				//invocamos el método "setEdad" de la persona del cliente
				clients[clientId].setEdad(edad);
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case				
			}break;
			case setNombreF:{
				string nombre; //Variables para almacenar nombre/edad
				//Reconstruimos el nombre desempaquetando sus datos
				//- Desempaquetamos y redimensionamos el tamaño del nombre
				nombre.resize(unpack<int>(buffer));
				//- Desempaquetamos datos/caracteres del nombre
				unpackv<char>(buffer,(char*)nombre.data(),(int)nombre.size());
				//invocamos el método "setNombre" de la persona del cliente
				clients[clientId].setNombre(nombre);
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case	
			}break;
			case getEdadF:{
				//invocar y empaquetar resultado
				pack(buffer,(int)clients[clientId].getEdad());
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case	
			}break;
			case getNombreF:{
				//Los string son tipos complejos
				//Usamos una variable intermedia
				string nombre=clients[clientId].getNombre();
				//retornar un mensaje ACK y datos resultado
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje ack
				//empaquetar resultado
				pack(buffer,(int)nombre.size());
				packv(buffer,(char*)nombre.data(),(int)nombre.size());
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case
			}break;
			case ostreamOpF:{
				//invocar el operador y guardar resultado
				std::ostringstream ss;
				ss << clients[clientId];
				string result =  ss.str();
				//empaquetar el resultado y enviarlo
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje ack
				//empaquetar resultado
				pack(buffer,(int)result.size());
				packv(buffer,(char*)result.data(),(int)result.size());
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case
			}break;
			case escribirAFicheroF:{
				string fichero; //Variables para almacenar nombre/edad
				//Reconstruimos el nombre desempaquetando sus datos
				//- Desempaquetamos y redimensionamos el tamaño del nombre
				fichero.resize(unpack<int>(buffer));
				//- Desempaquetamos datos/caracteres del nombre
				unpackv<char>(buffer,(char*)fichero.data(),(int)fichero.size());
				//invocamos el método "setNombre" de la persona del cliente
				clients[clientId].escribirAFichero(fichero);
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case	
				
			}break;
			case leerDeFicheroF:{
				string fichero; //Variables para almacenar nombre/edad
				//Reconstruimos el nombre desempaquetando sus datos
				//- Desempaquetamos y redimensionamos el tamaño del nombre
				fichero.resize(unpack<int>(buffer));
				//- Desempaquetamos datos/caracteres del nombre
				unpackv<char>(buffer,(char*)fichero.data(),(int)fichero.size());
				//invocamos el método "setNombre" de la persona del cliente
				clients[clientId].leerDeFichero(fichero);
				//retornar un mensaje ACK
				buffer.clear();//limpiar el buffer antes de reutilizarlo
				pack(buffer,ackMSG);//almacenar mensaje
				//en este punto termina la invocación, el mensaje se envía
				//al final del cuerpo switch-case	
			}break;
			case ackMSG: //No debemos recibir mensajes de ACK, ERROR
			default:
			{
			//default: mensaje error
				cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<
						"Tipo de mensaje inválido"<<endl;
			}break;
		};
		//En cada caso, se debe rellenar el buffer de respuesta
		//Una vez relleno, se envía al cliente:
		sendMSG(clientId,buffer);
	}
	//Al acabar, cerrar conexion
	closeConnection(clientId);
}





