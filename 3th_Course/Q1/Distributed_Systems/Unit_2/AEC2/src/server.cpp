/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Sistemas Distribuidos                      ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        29/10/2025  -  03:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    09/11/2025  -  22:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

#include "../include/protocol.h"

std::list<ClientInfo> connectedClients;
std::mutex clientsMutex;

/**
 * @brief Envía un mensaje a un cliente específico
 * @param clientId ID del socket del cliente destinatario
 * @param msg Estructura Message con todos los campos del mensaje
 * @details Empaqueta el tipo, username, contenido y (si es privado) destinatario
 */
void sendToClient(int clientId, const Message& msg) {
    std::vector<unsigned char> buffer;
    
    // Empaquetar tipo de mensaje
    int tipo = static_cast<int>(msg.type);
    pack(buffer, tipo);
    
    // Empaquetar username
    for (char c : msg.username) {
        pack(buffer, c);
    }
    pack(buffer, '\0');
    
    // Empaquetar contenido
    for (char c : msg.content) {
        pack(buffer, c);
    }
    pack(buffer, '\0');
    
    // empaquetar destinatario si esq es privado
    if (msg.type == MSG_PRIVATE) {
        for (char c : msg.recipient) {
            pack(buffer, c);
        }
        pack(buffer, '\0');
    }
    
    sendMSG(clientId, buffer);
}

/**
 * @brief Busca un cliente por nombre de usuario en la lista compartida
 * @param username Nombre de usuario a buscar
 * @return ID del cliente si se encuentra, -1 si no existe
 * @details Thread-safe: adquiere lock del mutex antes de buscar
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
 * @brief Obtiene el nombre de usuario asociado a un cliente
 * @param clientId ID del socket del cliente
 * @return Nombre de usuario si se encuentra, "Unknown" si no existe
 * @details Thread-safe: adquiere lock del mutex antes de buscar
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
 * @param senderId ID del cliente que envió el mensaje original
 * @param msg Estructura Message a reenviar
 * @details Thread-safe: adquiere lock del mutex antes de iterar la lista
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
 * @brief Maneja la comunicación con un cliente individual en un hilo separado
 * @param clientId ID del socket del cliente a gestionar
 * @details Recibe nombre de usuario, registra cliente, procesa mensajes en bucle,
 *          maneja tipos de mensaje (público, privado, desconexión), y limpia
 *          recursos al terminar. Se ejecuta en un hilo detached.
 */
void handleClient(int clientId) {
    std::vector<unsigned char> buffer;
    std::string username = "User_" + std::to_string(clientId);
    bool isConnected = true;
    
    std::cout << "[INFO] Cliente " << clientId << " conectado. Esperando nombre de usuario..." << std::endl;
    
    try {
        // Esperar el nombre de usuario 
        recvMSG(clientId, buffer);
        
        if (buffer.empty()) {
            std::cout << "[ERROR] No se recibió nombre de usuario del cliente " << clientId << std::endl;
            closeConnection(clientId);
            return;
        }
        
        // Desempaquetar el usuario
        int msgType = unpack<int>(buffer);
        username.clear();
        while (!buffer.empty()) {
            char c = unpack<char>(buffer);
            if (c == '\0') break;
            username += c;
        }
        
        // Registrar cliente
        {
            std::lock_guard<std::mutex> lock(clientsMutex);
            connectedClients.emplace_back(clientId, username);
        }
        
        std::cout << "[CONEXIÓN] Usuario '" << username << "' (ID: " << clientId << ") se ha unido al chat" << std::endl;
        
        // Notificar a todos los demás usuarios
        Message joinMsg(MSG_PUBLIC, "SERVIDOR", username + " se ha unido al chat");
        broadcastMessage(clientId, joinMsg);
        
        // recepción de mensajes
        while (isConnected) {
            buffer.clear();
            recvMSG(clientId, buffer);
            
            if (buffer.empty()) {
                // Conexión perdida o cerrada
                std::cout << "[DESCONEXIÓN] Cliente " << clientId << " (" << username << ") desconectado" << std::endl;
                isConnected = false;
                break;
            }
            
            // Desempaquetar
            msgType = unpack<int>(buffer);
            
            std::string msgUsername;
            while (!buffer.empty()) {
                char c = unpack<char>(buffer);
                if (c == '\0') break;
                msgUsername += c;
            }
            
            std::string content;
            while (!buffer.empty()) {
                char c = unpack<char>(buffer);
                if (c == '\0') break;
                content += c;
            }
            
            // Procesar según tipo 
            if (msgType == MSG_DISCONNECT) {
                std::cout << "[DESCONEXIÓN] Usuario '" << username << "' ha salido del chat" << std::endl;
                
                // Notificar a todos los demás
                Message leaveMsg(MSG_PUBLIC, "SERVIDOR", username + " ha salido del chat");
                broadcastMessage(clientId, leaveMsg);
                
                // BONUS 1: Enviar confirmación de desconexión antes de cerrar
                Message disconnectConfirm(MSG_DISCONNECT, "SERVIDOR", "Desconexión confirmada");
                sendToClient(clientId, disconnectConfirm);
                
                isConnected = false;
                break;
                
            } else if (msgType == MSG_PRIVATE) {
                // BONUS 2: Mensaje privado
                std::string recipient;
                while (!buffer.empty()) {
                    char c = unpack<char>(buffer);
                    if (c == '\0') break;
                    recipient += c;
                }
                
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
 * @return 0 si la ejecución fue exitosa, 1 si hubo error al inicializar
 * @details Inicializa servidor en puerto 3000, entra en bucle infinito
 *          aceptando clientes, crea un hilo detached para cada cliente nuevo.
 */
int main() {
    const int PORT = 3000;
    
    std::cout << "========================================" << std::endl;
    std::cout << "              SERVIDOR AEC2             " << std::endl;
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
    
    // Bucle principal de clientes
    while (true) {
        // Comprobar si hay nuevos cli
        bool result = checkClient();
        
        if (result) {
            // Nuevo cliente 
            int clientId = getLastClientID();
            
            // Crear un hilo para manejar este cliente
            clientThreads.emplace_back(handleClient, clientId);
            clientThreads.back().detach(); // Detach para ejecutar de forma independiente
        }
        
        // pausita o peta
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    
    return 0;
}
