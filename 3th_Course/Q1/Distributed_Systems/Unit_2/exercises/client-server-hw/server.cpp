/*

El programa servidor debe abrir una conexión a través del puerto 3000. Para ello usa la función “initServer” de la línea 15, pasándole por parámetros el número del puerto usado. Una vez iniciado, debe esperar a que un cliente se conecte, para lo que usa las funciones checkClient() y getLastClientID():

    CheckClient(): Función que devuelve “true” en caso de haber al menos un cliente iniciando conexión  (puede haber varios esperando).

    getLastClientID(): Función para conseguir el identificador de uno de los clientes que estén iniciando conexión. Ese identificador se usará en el resto de funciones para comunicaciones de datos.
*/

#include <iostream>
#include "utils.h"
#include <string>
#include <vector>

using namespace std;

int main() {
    int serverPort = 3000;

    // Iniciar el servidor
    int serverSocket = initServer(serverPort);
    if (serverSocket < 0) {
        cerr << "Error initializing server on port " << serverPort << endl;
        return 1;
    }
    cout << "Server initialized on port " << serverPort << endl;

    // Esperar a que un cliente se conecte
    cout << "Waiting for client connection..." << endl;
    while (!checkClient()) {
        // Esperar
    }

    // Obtener el ID del cliente conectado
    int clientID = getLastClientID();
    cout << "Client connected with ID: " << clientID << endl;

    // Recibir el mensaje del cliente
    string message;
    if (!receiveMessage(clientID, message)) {
        cerr << "Error receiving message from client ID: " << clientID << endl;
        closeSocket(serverSocket);
        return 1;
    }

    // Mostrar el mensaje recibido
    cout << "Message received from client: " << message << endl;

    // Cerrar el socket del servidor
    closeSocket(serverSocket);

    return 0;
}