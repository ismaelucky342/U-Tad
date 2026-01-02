/**
* El proyecto consistirá en dos ejecutables llamados “cliente” y “servidor”,
* usando los archivos de código contenidos en “libUtils.zip(opens in a new tab)”.
* Este ejemplo creará un programa “cliente” que envíe el mensaje “Hola Mundo”
* al un programa servidor, éste lo mostrará por terminal y terminará su ejecución.
* Para ello, editaremos el archivo “client.cpp” y mandaremos mensajes al programa servidor
* usando la librería “utils.h”. De igual manera, habremos de editar el archivo “server.cpp
* para recibir esos mensajes y mostrarlos por pantalla.
*/

#include <iostream>
#include "utils.h"
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]){
    
    string serverAddress = argv[1];
    int serverPort = stoi(argv[2]);

    // Crear el socket del cliente
    int clientSocket = createClientSocket(serverAddress, serverPort);

    // Mensaje a enviar
    string message = "Hola Mundo";

    // Enviar el mensaje al servidor
    if (!sendMessage(clientSocket, message)) {
        cerr << "Error sending message to server" << endl;
        closeSocket(clientSocket);
        return 1;
    }

    cout << "Message sent to server: " << message << endl;

    // Cerrar el socket del cliente
    closeSocket(clientSocket);

    return 0;
}