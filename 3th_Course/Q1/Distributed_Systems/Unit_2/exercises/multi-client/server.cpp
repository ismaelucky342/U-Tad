/*
Programa servidor (varios clientes)

El programa anterior recibe una única conexión de un programa cliente, muestra el mensaje y cierra la conexión. Un servidor real debería soportar múltiples conexiones, por lo que pasaremos a modificarlo para que gestione múltiples clientes. Para ello se usará la librería “thread” de C++, la cual nos permite crear un hilo de ejecución para atender a cada cliente por separado. Las acciones que realizará el servidor serán las siguientes:

    Crear un bucle “infinito” en el que se atiendan varias conexiones de clientes:

        Esperar una conexión

        Al recibir una conexión, crear un hilo de ejecución aparte para atender los mensajes y volver a esperar una nueva conexión

    Cada hilo creado se gestionará automáticamente:

        Recibe mensaje de usuario

        Muestra mensaje

        Cierra conexión

        Termina hilo de ejecución

*/

#include <iostream>
#include "utils.h"
#include <string>
#include <thread>
#include <vector>

using namespace std;

void handleClient(int clientID) {
    // Recibir el mensaje del cliente
    string message;
    if (!receiveMessage(clientID, message)) {
        cerr << "Error receiving message from client ID: " << clientID << endl;
        closeSocket(clientID);
        return;
    }

    // Mostrar el mensaje recibido
    cout << "Message received from client ID " << clientID << ": " << message << endl;

    // Cerrar el socket del cliente
    closeSocket(clientID);
}

int main() {
    int serverPort = 3000;

    // Iniciar el servidor
    int serverSocket = initServer(serverPort);
    if (serverSocket < 0) {
        cerr << "Error initializing server on port " << serverPort << endl;
        return 1;
    }
    cout << "Server initialized on port " << serverPort << endl;

    // Vector para almacenar los hilos de los clientes
    vector<thread> clientThreads;

    // Bucle infinito para atender múltiples conexiones de clientes
    while (true) {
        // Esperar a que un cliente se conecte
        cout << "Waiting for client connection..." << endl;
        while (!checkClient()) {
            // Esperar
        }

        // Obtener el ID del cliente conectado
        int clientID = getLastClientID();
        cout << "Client connected with ID: " << clientID << endl;

        // Crear un hilo para manejar al cliente
        clientThreads.emplace_back(handleClient, clientID);
    }

    // Cerrar el socket del servidor (nunca se alcanza en este ejemplo)
    closeSocket(serverSocket);

    // Unir todos los hilos antes de salir (nunca se alcanza en este ejemplo)
    for (auto& t : clientThreads) {
        if (t.joinable()) {
            t.join();
        }
    }

    return 0;
}