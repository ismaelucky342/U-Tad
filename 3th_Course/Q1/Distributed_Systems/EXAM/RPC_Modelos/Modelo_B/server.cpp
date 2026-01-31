#include "protocolo.h"
#include "calculadora.h"
#include <sys/socket.h>
#include <unistd.h>
#include <vector>

class GestorCalculadora {
public:
    void atiendeCliente(int clientId);
};

void GestorCalculadora::atiendeCliente(int clientId) {
    bool salir = false;
    Calculadora calcReal; 

    while(!salir) {
        int msgType;
        int n = recv(clientId, &msgType, sizeof(int), 0);
        
        if (n <= 0) { salir = true; continue; }

        switch(msgType) {
            case OP_SUMA:
                // TODO: Recibir 2 enteros, calcular y devolver
                break;

            case OP_SUMA_VECTORIAL:
                // TODO: 
                // 1. Recibir tamaño del vector
                // 2. Reservar memoria o crear vector
                // 3. Recibir datos del vector
                // 4. Llamar a calcReal.sumaVectorial
                // 5. Devolver ACK + Resultado
                break;
                
            // case OP_RESTA: ...
                
            default:
                salir = true;
                break;
        }
    }
    close(clientId);
}
