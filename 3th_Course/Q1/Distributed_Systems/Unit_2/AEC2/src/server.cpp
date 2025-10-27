/**
 * @file server.cpp
 * @brief Servidor de Chat-Room que gestiona múltiples clientes concurrentemente
 * 
 * Funcionalidades implementadas:
 * - Escucha en puerto 3000
 * - Gestión de múltiples clientes usando hilos
 * - Broadcast de mensajes públicos a todos los clientes
 * - Mensajes privados entre usuarios específicos (EXTENSIÓN)
 * - Cierre ordenado de conexiones para evitar "lost connection" (EXTENSIÓN)
 * - Lista de usuarios con pares {nombre, clientId}
 */

#include <iostream>
#include <string>
#include <list>
#include <thread>
#include <mutex>
#include <algorithm>
#include <cstring>
#include "../include/protocol.h"

// Declaraciones de funciones de libUtils
extern "C" {
    int initServer(int port);
    int checkClient();
    int getLastClientID();
    void recvMSG(int clientID, std::string* buffer);
    void sendMSG(int clientID, const std::string& buffer);
    void closeConnection(int clientID);
}

// Pack y unpack para serialización
std::string pack(const std::string& data);
std::string unpack(const std::string& data);

// Estructura para almacenar información del cliente
struct ClientInfo {
    int clientId;
    std::string username;
    
    ClientInfo(int id, const std::string& name) : clientId(id), username(name) {}
};

// Lista compartida de clientes conectados
std::list<ClientInfo> connectedClients;
std::mutex clientsMutex;

/**
 * @brief Serializa datos con formato: [longitud][contenido]
 */
std::string pack(const std::string& data) {
    int length = data.length();
    std::string packed;
    packed.append(reinterpret_cast<char*>(&length), sizeof(int));
    packed.append(data);
    return packed;
}

/**
 * @brief Deserializa datos del formato [longitud][contenido]
 */
std::string unpack(const std::string& data) {
    if (data.length() < sizeof(int)) {
        return "";
    }
    int length;
    std::memcpy(&length, data.c_str(), sizeof(int));
    
    if (data.length() < sizeof(int) + length) {
        return "";
    }
    
    return data.substr(sizeof(int), length);
}

/**
 * @brief Envía un mensaje a un cliente específico
 */
void sendToClient(int clientId, const Message& msg) {
    std::string buffer;
    
    // Empaquetar tipo de mensaje
    buffer += pack(std::to_string(static_cast<int>(msg.type)));
    
    // Empaquetar username
    buffer += pack(msg.username);
    
    // Empaquetar contenido
    buffer += pack(msg.content);
    
    // Si es mensaje privado, empaquetar destinatario
    if (msg.type == MSG_PRIVATE) {
        buffer += pack(msg.recipient);
    }
    
    sendMSG(clientId, buffer);
}

/**
 * @brief Busca un cliente por nombre de usuario
 */
int findClientByUsername(const std::string& username) {
    std::lock_guard<std::mutex> lock(clientsMutex);
    
    auto it = std::find_if(connectedClients.begin(), connectedClients.end(),
        [&username](const ClientInfo& client) {
            return client.username == username;
        });
    
    if (it != connectedClients.end()) {
        return it->clientId;
    }
    return -1;
}

/**
 * @brief Obtiene el nombre de usuario de un cliente
 */
std::string getUsername(int clientId) {
    std::lock_guard<std::mutex> lock(clientsMutex);
    
    auto it = std::find_if(connectedClients.begin(), connectedClients.end(),
        [clientId](const ClientInfo& client) {
            return client.clientId == clientId;
        });
    
    if (it != connectedClients.end()) {
        return it->username;
    }
    return "Unknown";
}

/**
 * @brief Envía un mensaje a todos los clientes excepto al remitente
 */
void broadcastMessage(int senderId, const Message& msg) {
    std::lock_guard<std::mutex> lock(clientsMutex);
    
    for (const auto& client : connectedClients) {
        if (client.clientId != senderId) {
            sendToClient(client.clientId, msg);
        }
    }
}

/**
 * @brief Maneja la comunicación con un cliente individual
 */
void handleClient(int clientId) {
    std::string buffer;
    std::string username = "User_" + std::to_string(clientId);
    bool isConnected = true;
    
    std::cout << "[INFO] Cliente " << clientId << " conectado. Esperando nombre de usuario..." << std::endl;
    
    try {
        // Esperar el nombre de usuario (primer mensaje)
        recvMSG(clientId, &buffer);
        
        if (buffer.empty()) {
            std::cout << "[ERROR] No se recibió nombre de usuario del cliente " << clientId << std::endl;
            closeConnection(clientId);
            return;
        }
        
        // Desempaquetar el nombre de usuario
        std::string typeStr = unpack(buffer);
        buffer = buffer.substr(sizeof(int) + typeStr.length());
        username = unpack(buffer);
        
        // Registrar cliente en la lista
        {
            std::lock_guard<std::mutex> lock(clientsMutex);
            connectedClients.emplace_back(clientId, username);
        }
        
        std::cout << "[CONEXIÓN] Usuario '" << username << "' (ID: " << clientId << ") se ha unido al chat" << std::endl;
        
        // Notificar a todos los demás usuarios
        Message joinMsg(MSG_PUBLIC, "SERVIDOR", username + " se ha unido al chat");
        broadcastMessage(clientId, joinMsg);
        
        // Bucle principal de recepción de mensajes
        while (isConnected) {
            buffer.clear();
            recvMSG(clientId, &buffer);
            
            if (buffer.empty()) {
                // Conexión perdida o cerrada
                std::cout << "[DESCONEXIÓN] Cliente " << clientId << " (" << username << ") desconectado" << std::endl;
                isConnected = false;
                break;
            }
            
            // Desempaquetar mensaje
            std::string typeStr = unpack(buffer);
            buffer = buffer.substr(sizeof(int) + typeStr.length());
            
            int msgType = std::stoi(typeStr);
            
            std::string msgUsername = unpack(buffer);
            buffer = buffer.substr(sizeof(int) + msgUsername.length());
            
            std::string content = unpack(buffer);
            buffer = buffer.substr(sizeof(int) + content.length());
            
            // Procesar según tipo de mensaje
            if (msgType == MSG_DISCONNECT) {
                std::cout << "[DESCONEXIÓN] Usuario '" << username << "' ha salido del chat" << std::endl;
                
                // Notificar a todos los demás
                Message leaveMsg(MSG_PUBLIC, "SERVIDOR", username + " ha salido del chat");
                broadcastMessage(clientId, leaveMsg);
                
                // EXTENSIÓN 1: Enviar confirmación de desconexión antes de cerrar
                Message disconnectConfirm(MSG_DISCONNECT, "SERVIDOR", "Desconexión confirmada");
                sendToClient(clientId, disconnectConfirm);
                
                isConnected = false;
                break;
                
            } else if (msgType == MSG_PRIVATE) {
                // EXTENSIÓN 2: Mensaje privado
                std::string recipient = unpack(buffer);
                
                std::cout << "[PRIVADO] De: " << username << " Para: " << recipient 
                          << " | Mensaje: " << content << std::endl;
                
                int recipientId = findClientByUsername(recipient);
                
                if (recipientId != -1) {
                    Message privateMsg(MSG_PRIVATE, username, content, recipient);
                    sendToClient(recipientId, privateMsg);
                    
                    // Confirmar al remitente
                    Message confirmMsg(MSG_PUBLIC, "SERVIDOR", 
                        "Mensaje privado enviado a " + recipient);
                    sendToClient(clientId, confirmMsg);
                } else {
                    // Usuario no encontrado
                    Message errorMsg(MSG_PUBLIC, "SERVIDOR", 
                        "Error: Usuario '" + recipient + "' no encontrado");
                    sendToClient(clientId, errorMsg);
                }
                
            } else if (msgType == MSG_PUBLIC) {
                // Mensaje público (broadcast)
                std::cout << "[PÚBLICO] " << username << " dice: " << content << std::endl;
                
                Message publicMsg(MSG_PUBLIC, username, content);
                broadcastMessage(clientId, publicMsg);
            }
        }
        
    } catch (const std::exception& e) {
        std::cout << "[ERROR] Excepción al manejar cliente " << clientId << ": " << e.what() << std::endl;
    }
    
    // Limpiar cliente de la lista
    {
        std::lock_guard<std::mutex> lock(clientsMutex);
        connectedClients.remove_if([clientId](const ClientInfo& client) {
            return client.clientId == clientId;
        });
    }
    
    closeConnection(clientId);
}

/**
 * @brief Función principal del servidor
 */
int main() {
    const int PORT = 3000;
    
    std::cout << "========================================" << std::endl;
    std::cout << "    SERVIDOR CHAT-ROOM - PUERTO 3000   " << std::endl;
    std::cout << "========================================" << std::endl;
    std::cout << std::endl;
    
    // Inicializar servidor
    int serverSocket = initServer(PORT);
    if (serverSocket < 0) {
        std::cerr << "[ERROR] No se pudo inicializar el servidor en el puerto " << PORT << std::endl;
        return 1;
    }
    
    std::cout << "[OK] Servidor iniciado en localhost:" << PORT << std::endl;
    std::cout << "[INFO] Esperando conexiones de clientes..." << std::endl;
    std::cout << std::endl;
    
    std::list<std::thread> clientThreads;
    
    // Bucle principal de aceptación de clientes
    while (true) {
        // Comprobar si hay nuevos clientes
        int result = checkClient();
        
        if (result > 0) {
            // Nuevo cliente conectado
            int clientId = getLastClientID();
            
            // Crear un hilo para manejar este cliente
            clientThreads.emplace_back(handleClient, clientId);
            clientThreads.back().detach(); // Detach para ejecutar de forma independiente
        }
        
        // Pequeña pausa para no saturar la CPU
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    
    return 0;
}
