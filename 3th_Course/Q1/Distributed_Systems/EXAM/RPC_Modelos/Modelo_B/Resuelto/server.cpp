#include "protocolo.h"
#include "calculadora.h"
#include <sys/socket.h>
#include <unistd.h>
#include <vector>
#include <cstring> 

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
            case OP_SUMA: {
                // 1. Recibir 2 enteros
                int args[2];
                recv(clientId, args, sizeof(int) * 2, 0);
                
                // 2. Calcular
                int res = calcReal.suma(args[0], args[1]);
                
                // 3. Devolver ACK + Resultado
                int response[2] = {OP_ACK, res};
                send(clientId, response, sizeof(int) * 2, 0);
                break;
            }
            case OP_RESTA: {
                // 1. Recibir 2 enteros
                int args[2];
                recv(clientId, args, sizeof(int) * 2, 0);
                
                // 2. Calcular
                int res = calcReal.resta(args[0], args[1]);
                
                // 3. Devolver ACK + Resultado
                int response[2] = {OP_ACK, res};
                send(clientId, response, sizeof(int) * 2, 0);
                break;
            }
            case OP_SUMA_VECTORIAL: {
                // 1. Recibir tamaño del vector
                int numElems;
                recv(clientId, &numElems, sizeof(int), 0);
                
                // 2. Reservar memoria o crear vector y Recibir datos del vector
                std::vector<int> vec(numElems);
                // Leemos directamente al array interno del vector
                recv(clientId, vec.data(), numElems * sizeof(int), 0);
                
                // 3. Llamar a calcReal.sumaVectorial
                int res = calcReal.sumaVectorial(vec);
                
                // 4. Devolver ACK + Resultado
                int response[2] = {OP_ACK, res};
                send(clientId, response, sizeof(int) * 2, 0);
                break;
            }
            default:
                salir = true;
                break;
        }
    }
    close(clientId);
}
