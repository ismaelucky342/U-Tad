#include "calculadora.h"
#include "protocolo.h"
#include <sys/socket.h>
#include <vector>
#include <iostream>
#include <cstring>

int CalculadoraRemota::suma(int a, int b) {
    // 1. Empaquetar ID, a, b
    int bufferSize = sizeof(int) * 3; // OP + A + B
    std::vector<char> buffer(bufferSize);
    int op = OP_SUMA;
    int offset = 0;

    memcpy(buffer.data() + offset, &op, sizeof(int)); offset += sizeof(int);
    memcpy(buffer.data() + offset, &a, sizeof(int)); offset += sizeof(int);
    memcpy(buffer.data() + offset, &b, sizeof(int));

    // 2. Enviar
    send(serverSocket, buffer.data(), bufferSize, 0);

    // 3. Recibir ACK y Resultado
    int response[2]; // ACK + RESULT
    recv(serverSocket, response, sizeof(int) * 2, 0);

    if (response[0] != OP_ACK) return -1;
    return response[1];
}

int CalculadoraRemota::resta(int a, int b) {
    // 1. Empaquetar ID, a, b
    int bufferSize = sizeof(int) * 3;
    std::vector<char> buffer(bufferSize);
    int op = OP_RESTA;
    int offset = 0;

    memcpy(buffer.data() + offset, &op, sizeof(int)); offset += sizeof(int);
    memcpy(buffer.data() + offset, &a, sizeof(int)); offset += sizeof(int);
    memcpy(buffer.data() + offset, &b, sizeof(int));

    // 2. Enviar
    send(serverSocket, buffer.data(), bufferSize, 0);

    // 3. Recibir ACK y Resultado
    int response[2];
    recv(serverSocket, response, sizeof(int) * 2, 0);

    return (response[0] == OP_ACK) ? response[1] : 0;
}

int CalculadoraRemota::sumaVectorial(std::vector<int> numeros) {
    // 1. Preparar paquete (ID + Size + Datos...)
    // OJO: Hay que enviar el TAMAÑO del vector primero, luego los datos
    int numElems = numeros.size();
    int dataSize = numElems * sizeof(int);
    int bufferSize = sizeof(int) * 2 + dataSize;
    
    std::vector<char> buffer(bufferSize);
    int op = OP_SUMA_VECTORIAL;
    int offset = 0;

    // Cabecera
    memcpy(buffer.data() + offset, &op, sizeof(int)); offset += sizeof(int);
    memcpy(buffer.data() + offset, &numElems, sizeof(int)); offset += sizeof(int);
    
    // Datos (copia directa del vector al buffer)
    memcpy(buffer.data() + offset, numeros.data(), dataSize);

    // 2. Enviar (ID + Size + Datos...)
    send(serverSocket, buffer.data(), bufferSize, 0);

    // 3. Recibir resultado
    int response[2];
    recv(serverSocket, response, sizeof(int) * 2, 0);

    return (response[0] == OP_ACK) ? response[1] : 0;
}
