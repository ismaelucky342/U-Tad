#include "protocolo.h"
#include "persona.h"
#include <sys/socket.h>
#include <unistd.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>

class GestorClientes {
public:
    void atiendeCliente(int clientId);
};

void GestorClientes::atiendeCliente(int clientId) {
    bool salir = false;
    Persona personaReal; // Instancia real en servidor

    while(!salir) {
        int msgType;
        // Leemos solo el ID de operación para empezar
        int n = recv(clientId, &msgType, sizeof(int), 0);
        
        if (n <= 0) {
            salir = true;
            continue;
        }

        switch(msgType) {
            case OP_SET_EDAD: {
                // 1. Recibir/Desempaquetar argumentos
                int edad;
                recv(clientId, &edad, sizeof(int), 0);
                
                // 2. Ejecutar método en personaReal
                personaReal.setEdad(edad);
                
                // 3. Empaquetar ACK
                int ack = OP_ACK;

                // 4. Enviar ACK
                send(clientId, &ack, sizeof(int), 0);
                break;
            }

            case OP_GET_EDAD: {
                // 1. Ejecutar método -> obtener dato
                int edad = personaReal.getEdad();

                // 2. Empaquetar ACK + Dato
                int buffer[2];
                buffer[0] = OP_ACK;
                buffer[1] = edad;

                // 3. Enviar
                send(clientId, buffer, sizeof(int) * 2, 0);
                break;
            }

            case OP_SET_NOMBRE: {
                // 1. Recibir/Desempaquetar argumentos (Tamaño + Buffer)
                int strLen;
                recv(clientId, &strLen, sizeof(int), 0);
                
                std::vector<char> strBuffer(strLen + 1);
                recv(clientId, strBuffer.data(), strLen, 0);
                strBuffer[strLen] = '\0';
                
                // 2. Ejecutar método en personaReal
                personaReal.setNombre(std::string(strBuffer.data()));
                
                // 3. Empaquetar ACK
                int ack = OP_ACK;

                // 4. Enviar ACK
                send(clientId, &ack, sizeof(int), 0);
                break;
            }

            case OP_GET_NOMBRE: {
                // 1. Ejecutar método -> obtener dato
                std::string nombre = personaReal.getNombre();
                int strLen = nombre.length();

                // 2. Empaquetar ACK + Tamaño + Datos
                // Enviamos cabecera primero o todo junto (aquí todo junto es mejor si no es muy grande)
                int headerSize = sizeof(int) * 2;
                int totalSize = headerSize + strLen;
                std::vector<char> buffer(totalSize);
                
                int ack = OP_ACK;
                int offset = 0;

                memcpy(&buffer[0] + offset, &ack, sizeof(int));
                offset += sizeof(int);
                memcpy(&buffer[0] + offset, &strLen, sizeof(int));
                offset += sizeof(int);
                memcpy(&buffer[0] + offset, nombre.c_str(), strLen);

                // 3. Enviar
                send(clientId, buffer.data(), totalSize, 0);
                break;
            }
                
            default:
                salir = true;
                break;
        }
    }
    close(clientId);
}
