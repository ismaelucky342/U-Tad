#include "protocolo.h"
#include "persona.h"
#include <sys/socket.h>
#include <unistd.h>
#include <iostream>
#include <vector>
#include <string>

class GestorClientes {
public:
    void atiendeCliente(int clientId);
};

void GestorClientes::atiendeCliente(int clientId) {
    bool salir = false;
    char buffer[1024];
    Persona personaReal; // Instancia real en servidor

    while(!salir) {
        // 1. Recibir cabecera/ID operación
        int msgType;
        int n = recv(clientId, &msgType, sizeof(int), 0);
        
        if (n <= 0) { salir = true; continue; }

        switch(msgType) {
            case OP_SET_EDAD:
                // TODO:
                // 1. Recibir/Desempaquetar argumentos
                // 2. Ejecutar método en personaReal
                // 3. Empaquetar ACK
                // 4. Enviar ACK
                break;

            // TODO: AÑADIR RESTO DE CASES (OP_GET_EDAD, ETC)
            
            // case OP_GET_EDAD: ...
            
            // case OP_SET_NOMBRE: ...

            // case OP_GET_NOMBRE: ...
                
            default:
                salir = true;
                break;
        }
    }
    close(clientId);
}
