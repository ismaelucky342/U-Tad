/**
 * @file client.cpp
 * @brief Cliente de Chat-Room con soporte para mensajes públicos y privados
 * 
 * Funcionalidades implementadas:
 * - Conexión al servidor en localhost:3000
 * - Hilo paralelo para recibir mensajes del servidor
 * - Envío de mensajes públicos (broadcast)
 * - Envío de mensajes privados con comando /privado (EXTENSIÓN)
 * - Cierre ordenado con comando exit()
 * - Manejo de desconexión sin error "lost connection" (EXTENSIÓN)
 */

#include <iostream>
#include <string>
#include <thread>
#include <atomic>
#include <sstream>
#include <cstring>
#include "../include/protocol.h"

// Declaraciones de funciones de libUtils
extern "C" {
    int initClient(const char* serverIP, int port);
    void sendMSG(int socketID, const std::string& buffer);
    void recvMSG(int socketID, std::string* buffer);
    void closeConnection(int socketID);
}

// Pack y unpack para serialización
std::string pack(const std::string& data);
std::string unpack(const std::string& data);

// Variables globales
std::atomic<bool> isRunning(true);
int clientSocket = -1;
std::string myUsername;

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
 * @brief Envía un mensaje al servidor
 */
void sendMessage(const Message& msg) {
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
    
    sendMSG(clientSocket, buffer);
}

/**
 * @brief Hilo para recibir mensajes del servidor continuamente
 */
void receiveMessages() {
    std::string buffer;
    
    while (isRunning) {
        buffer.clear();
        recvMSG(clientSocket, &buffer);
        
        if (buffer.empty()) {
            if (isRunning) {
                std::cout << "\n[INFO] Conexión cerrada por el servidor" << std::endl;
                isRunning = false;
            }
            break;
        }
        
        try {
            // Desempaquetar tipo de mensaje
            std::string typeStr = unpack(buffer);
            buffer = buffer.substr(sizeof(int) + typeStr.length());
            
            int msgType = std::stoi(typeStr);
            
            // Desempaquetar username
            std::string username = unpack(buffer);
            buffer = buffer.substr(sizeof(int) + username.length());
            
            // Desempaquetar contenido
            std::string content = unpack(buffer);
            buffer = buffer.substr(sizeof(int) + content.length());
            
            // Procesar según tipo de mensaje
            if (msgType == MSG_DISCONNECT) {
                // Mensaje de desconexión del servidor
                std::cout << "\n[INFO] " << content << std::endl;
                isRunning = false;
                break;
                
            } else if (msgType == MSG_PRIVATE) {
                // Mensaje privado recibido
                std::string recipient = unpack(buffer);
                std::cout << "\n[PRIVADO] " << username << " te dice: " << content << std::endl;
                std::cout << "> " << std::flush;
                
            } else if (msgType == MSG_PUBLIC) {
                // Mensaje público
                if (username == "SERVIDOR") {
                    std::cout << "\n[SERVIDOR] " << content << std::endl;
                } else {
                    std::cout << "\n[" << username << "]: " << content << std::endl;
                }
                std::cout << "> " << std::flush;
            }
            
        } catch (const std::exception& e) {
            std::cerr << "\n[ERROR] Error al procesar mensaje: " << e.what() << std::endl;
        }
    }
}

/**
 * @brief Muestra la ayuda de comandos disponibles
 */
void showHelp() {
    std::cout << "\n========== COMANDOS DISPONIBLES ==========" << std::endl;
    std::cout << "  exit()                     - Salir del chat" << std::endl;
    std::cout << "  /privado <usuario> <msg>   - Enviar mensaje privado" << std::endl;
    std::cout << "  /ayuda                     - Mostrar esta ayuda" << std::endl;
    std::cout << "  <mensaje>                  - Enviar mensaje público" << std::endl;
    std::cout << "===========================================" << std::endl;
}

/**
 * @brief Procesa comandos especiales del usuario
 * @return true si se procesó un comando especial, false en caso contrario
 */
bool processCommand(const std::string& input) {
    if (input == "/ayuda" || input == "/help") {
        showHelp();
        return true;
    }
    
    // Comando para mensaje privado: /privado <usuario> <mensaje>
    if (input.substr(0, 8) == "/privado" || input.substr(0, 9) == "/private") {
        std::istringstream iss(input);
        std::string command, recipient, message;
        
        iss >> command;  // Leer comando
        iss >> recipient; // Leer destinatario
        
        if (recipient.empty()) {
            std::cout << "[ERROR] Uso: /privado <usuario> <mensaje>" << std::endl;
            return true;
        }
        
        // Leer el resto como mensaje
        std::getline(iss, message);
        if (!message.empty() && message[0] == ' ') {
            message = message.substr(1); // Eliminar espacio inicial
        }
        
        if (message.empty()) {
            std::cout << "[ERROR] El mensaje no puede estar vacío" << std::endl;
            return true;
        }
        
        // Enviar mensaje privado
        Message privateMsg(MSG_PRIVATE, myUsername, message, recipient);
        sendMessage(privateMsg);
        
        std::cout << "[INFO] Mensaje privado enviado a " << recipient << std::endl;
        return true;
    }
    
    return false;
}

/**
 * @brief Función principal del cliente
 */
int main() {
    const char* SERVER_IP = "127.0.0.1";
    const int PORT = 3000;
    
    std::cout << "========================================" << std::endl;
    std::cout << "       CLIENTE CHAT-ROOM v2.0          " << std::endl;
    std::cout << "========================================" << std::endl;
    std::cout << std::endl;
    
    // Solicitar nombre de usuario
    std::cout << "Por favor, ingresa tu nombre de usuario: ";
    std::getline(std::cin, myUsername);
    
    if (myUsername.empty()) {
        myUsername = "Anonymous";
    }
    
    std::cout << "\n[INFO] Conectando al servidor " << SERVER_IP << ":" << PORT << "..." << std::endl;
    
    // Inicializar conexión con el servidor
    clientSocket = initClient(SERVER_IP, PORT);
    
    if (clientSocket < 0) {
        std::cerr << "[ERROR] No se pudo conectar al servidor" << std::endl;
        std::cerr << "[INFO] Asegúrate de que el servidor esté ejecutándose" << std::endl;
        return 1;
    }
    
    std::cout << "[OK] Conectado al servidor exitosamente" << std::endl;
    
    // Enviar nombre de usuario al servidor
    Message connectMsg(MSG_CONNECT, myUsername, "");
    sendMessage(connectMsg);
    
    std::cout << "\n[INFO] ¡Bienvenido al chat, " << myUsername << "!" << std::endl;
    std::cout << "[INFO] Escribe '/ayuda' para ver los comandos disponibles" << std::endl;
    std::cout << "[INFO] Escribe 'exit()' para salir del chat" << std::endl;
    std::cout << std::endl;
    
    // Iniciar hilo para recibir mensajes
    std::thread receiverThread(receiveMessages);
    
    // Bucle principal para enviar mensajes
    std::string input;
    while (isRunning) {
        std::cout << "> ";
        std::getline(std::cin, input);
        
        // Verificar si se perdió la conexión
        if (!isRunning) {
            break;
        }
        
        // Ignorar líneas vacías
        if (input.empty()) {
            continue;
        }
        
        // Comando para salir
        if (input == "exit()" || input == "exit" || input == "quit") {
            std::cout << "\n[INFO] Cerrando conexión..." << std::endl;
            
            // Enviar mensaje de desconexión al servidor
            Message disconnectMsg(MSG_DISCONNECT, myUsername, "Desconectando");
            sendMessage(disconnectMsg);
            
            isRunning = false;
            break;
        }
        
        // Procesar comandos especiales
        if (processCommand(input)) {
            continue;
        }
        
        // Enviar mensaje público
        Message publicMsg(MSG_PUBLIC, myUsername, input);
        sendMessage(publicMsg);
    }
    
    // Esperar a que el hilo receptor termine
    if (receiverThread.joinable()) {
        receiverThread.join();
    }
    
    // Cerrar conexión
    closeConnection(clientSocket);
    
    std::cout << "\n[INFO] Desconectado del servidor. ¡Hasta pronto!" << std::endl;
    
    return 0;
}
