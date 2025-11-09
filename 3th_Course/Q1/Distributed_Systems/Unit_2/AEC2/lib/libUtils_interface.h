/**
 * @file libUtils_interface.h
 * @brief Interfaz esperada de la librería libUtils
 * 
 * Este archivo documenta las funciones que se esperan de libUtils.
 * Si tu versión de libUtils tiene una interfaz diferente, 
 * deberás adaptar las llamadas en server.cpp y client.cpp.
 * 
 * NOTA: Este archivo es solo documentación, NO compilar.
 */

#ifndef LIBUTILS_INTERFACE_H
#define LIBUTILS_INTERFACE_H

#include <string>

extern "C" {

/**
 * @brief Inicializa el servidor en el puerto especificado
 * @param port Puerto en el que escuchará el servidor (ej: 3000)
 * @return Socket del servidor, o -1 en caso de error
 */
int initServer(int port);

/**
 * @brief Inicializa un cliente y lo conecta al servidor
 * @param serverIP Dirección IP del servidor (ej: "127.0.0.1")
 * @param port Puerto del servidor (ej: 3000)
 * @return Socket del cliente, o -1 en caso de error
 */
int initClient(const char* serverIP, int port);

/**
 * @brief Comprueba si hay nuevos clientes esperando conectarse
 * @return Número de clientes nuevos, o -1 en caso de error
 */
int checkClient();

/**
 * @brief Obtiene el ID del último cliente que se conectó
 * @return ID del cliente
 */
int getLastClientID();

/**
 * @brief Envía un mensaje a través del socket especificado
 * @param socketID ID del socket (cliente o servidor)
 * @param buffer Buffer con los datos a enviar (std::string)
 * 
 * NOTA: Algunas implementaciones pueden usar const std::string&
 */
void sendMSG(int socketID, const std::string& buffer);

/**
 * @brief Recibe un mensaje del socket especificado
 * @param socketID ID del socket (cliente o servidor)
 * @param buffer Puntero a std::string donde se almacenará el mensaje
 * 
 * IMPORTANTE: 
 * - Si la conexión se cierra, buffer quedará vacío
 * - Esta función es bloqueante
 */
void recvMSG(int socketID, std::string* buffer);

/**
 * @brief Cierra la conexión del socket especificado
 * @param socketID ID del socket a cerrar
 */
void closeConnection(int socketID);

/**
 * @brief Cierra completamente el socket (alternativa a closeConnection)
 * @param socketID ID del socket a cerrar
 * 
 * NOTA: Algunas versiones de libUtils pueden usar esta función en lugar de closeConnection
 */
void close(int socketID);

} // extern "C"

// ========================================
// FUNCIONES DE SERIALIZACIÓN
// ========================================

/**
 * @brief Empaqueta datos con el formato [longitud][contenido]
 * @param data Datos a empaquetar
 * @return String empaquetado
 * 
 * Formato:
 * - Primeros 4 bytes: longitud del contenido (int)
 * - Siguientes N bytes: contenido
 */
std::string pack(const std::string& data);

/**
 * @brief Desempaqueta datos del formato [longitud][contenido]
 * @param data Datos empaquetados
 * @return Contenido desempaquetado
 */
std::string unpack(const std::string& data);

#endif // LIBUTILS_INTERFACE_H

/*
 * POSIBLES VARIACIONES DE LA INTERFAZ:
 * 
 * 1. Si sendMSG usa char* en lugar de std::string:
 *    void sendMSG(int socketID, const char* buffer, int length);
 *    
 *    Adaptación necesaria:
 *    sendMSG(id, buffer.c_str(), buffer.length());
 * 
 * 2. Si recvMSG usa char* en lugar de std::string*:
 *    int recvMSG(int socketID, char* buffer, int maxLength);
 *    
 *    Adaptación necesaria:
 *    char tempBuffer[4096];
 *    int received = recvMSG(id, tempBuffer, sizeof(tempBuffer));
 *    buffer->assign(tempBuffer, received);
 * 
 * 3. Si pack/unpack están en libUtils:
 *    extern "C" {
 *        std::string pack(const std::string& data);
 *        std::string unpack(const std::string& data);
 *    }
 *    
 *    En este caso, eliminar las implementaciones de pack/unpack
 *    de server.cpp y client.cpp
 * 
 * 4. Si la función de cierre se llama diferente:
 *    - closeSocket(int id)
 *    - disconnectClient(int id)
 *    - shutdown(int id)
 *    
 *    Buscar y reemplazar closeConnection por el nombre correcto
 */
