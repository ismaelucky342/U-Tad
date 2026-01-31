#include "persona.h"
#include "protocolo.h"
#include <sys/socket.h>
#include <vector>
#include <string.h>
#include <iostream>

void PersonaRemota::setEdad(int edad) {
    // 1. Definir buffer y variables
    // Calculamos tamaño total: 4 bytes para op code + 4 bytes para el entero 'edad'
    int bufferSize = sizeof(int) * 2; // Op + Dato
    
    // Vector de char actúa como nuestro buffer de bytes crudos
    std::vector<char> buffer(bufferSize);
    
    // Seleccionamos la operación (definida en el enum del protocolo)
    int op = OP_SET_EDAD;
    int offset = 0; // Controla dónde escribimos en el buffer

    // 2. Empaquetar: ID operación + Argumentos
    // Escribimos el código de operación en el inicio del buffer
    memcpy(&buffer[0] + offset, &op, sizeof(int));
    offset += sizeof(int); // Avanzamos el puntero 4 bytes
    
    // Escribimos el argumento 'edad' a continuación
    memcpy(&buffer[0] + offset, &edad, sizeof(int));
    
    // 3. Enviar mensaje
    // Enviamos el contenido crudo del vector por el socket
    send(serverSocket, buffer.data(), bufferSize, 0);

    // 4. Recibir ACK (Bloqueante)
    // Es obligatorio esperar respuesta para confirmar que el servidor procesó
    int ack;
    recv(serverSocket, &ack, sizeof(int), 0);
    
    // 5. Comprobar confirmación
    if(ack != OP_ACK) {
        std::cerr << "Error RPC setEdad: Servidor no devolvió ACK" << std::endl;
    }
}

int PersonaRemota::getEdad() {
    // 1. Definir buffer y variables
    int op = OP_GET_EDAD;
    
    // 2. Empaquetar: ID operación
    // Al ser solo un entero (la OpCode), no hace falta un buffer vector complejo
    // Podemos enviar la dirección de la variable 'op' directamente
    
    // 3. Enviar mensaje
    send(serverSocket, &op, sizeof(int), 0);

    // 4. Recibir respuesta
    // El protocolo dice que el servidor devuelve: [ACK] [DATO_INT]
    // Necesitamos espacio para 2 enteros (2 * 4 bytes)
    int datos[2]; // 0: ACK, 1: Edad
    
    // recv bloqueará hasta recibir los datos
    recv(serverSocket, datos, sizeof(int) * 2, 0);

    // 5. Desempaquetar: ACK + Datos
    // Validamos que el primer entero sea el ACK esperado
    if(datos[0] != OP_ACK) {
        std::cerr << "Error RPC getEdad" << std::endl;
        return -1; // Valor de error
    }
    
    // 6. Retornar valor real
    // El segundo entero en el array es el dato que pedimos
    return datos[1];
}

void PersonaRemota::setNombre(std::string nombre) {
    // 1. Definir buffer
    // Necesitamos serializar una cadena de longitud variable.
    // Estructura del paquete: [OP_CODE (4b)] [LENGTH (4b)] [CHAR_DATA (Nb)]
    
    int strLen = nombre.length(); 
    // Calculamos tamaño total sumando cabeceras y datos
    int bufferSize = sizeof(int) + sizeof(int) + strLen;
    std::vector<char> buffer(bufferSize);
    
    int offset = 0;
    int op = OP_SET_NOMBRE;

    // 2. Empaquetar: ID + Tamaño String + Datos String
    
    // A) Copiar OpCode
    memcpy(&buffer[0] + offset, &op, sizeof(int)); 
    offset += sizeof(int);
    
    // B) Copiar Longitud del string (para que el servidor sepa cuánto leer después)
    memcpy(&buffer[0] + offset, &strLen, sizeof(int)); 
    offset += sizeof(int);
    
    // C) Copiar los bytes del string usando .c_str()
    memcpy(&buffer[0] + offset, nombre.c_str(), strLen);

    // 3. Enviar
    // Enviamos todo el paquete de una vez
    send(serverSocket, buffer.data(), bufferSize, 0);

    // 4. Recibir ACK
    // Esperamos confirmación de que se actualizó el nombre
    int ack;
    recv(serverSocket, &ack, sizeof(int), 0);
}

std::string PersonaRemota::getNombre() {
    // 1. Empaquetar ID
    // Solicitud simple, solo enviamos qué queremos hacer
    int op = OP_GET_NOMBRE;
    
    // 2. Enviar
    send(serverSocket, &op, sizeof(int), 0);

    // 3. Recibir Buffer
    // Como no sabemos cuánto mide el nombre que nos devolverán, leemos en 2 pasos
    
    // PASO A: Leer Cabecera (ACK + Tamaño del string que viene)
    int header[2]; // 0: ACK, 1: Size
    recv(serverSocket, header, sizeof(int) * 2, 0);

    // Validar ACK
    if(header[0] != OP_ACK) return ""; // Retorno vacío si hay error

    // Obtener tamaño del string
    int strLen = header[1];
    
    // PASO B: Preparar buffer para los datos
    // +1 para el caracter nulo '\0' final de C++
    std::vector<char> strBuffer(strLen + 1); 
    
    // PASO C: Leer el cuerpo del mensaje (los caracteres del nombre)
    recv(serverSocket, strBuffer.data(), strLen, 0);
    
    // Añadir terminador nulo manual para convertir a std::string con seguridad
    strBuffer[strLen] = '\0';

    // 5. Retornar string reconstruida
    return std::string(strBuffer.data());
}
