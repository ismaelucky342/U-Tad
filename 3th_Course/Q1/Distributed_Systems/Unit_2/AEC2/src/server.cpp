/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Sistemas Distribuidos                      ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        29/10/2025  -  03:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    15/11/2025  -  02:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

#include "../include/protocol.h"

/** Estructura para almacenar información de cada cliente conectado */
struct ClientInfo {
    int clientId;
    std::string username;

    ClientInfo(int id, const std::string& name) : clientId(id), username(name) {}
};

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

    /** Empaqueta el tipo de mensaje en el buffer */
    int tipo = static_cast<int>(msg.type);
    pack(buffer, tipo);

    /** Empaqueta el nombre de usuario en el buffer */
    for (char c : msg.username) {
        pack(buffer, c);
    }
    pack(buffer, '\0');

    /** Empaqueta el contenido del mensaje en el buffer */
    for (char c : msg.content) {
        pack(buffer, c);
    }
    pack(buffer, '\0');

    /** Empaqueta el destinatario si el mensaje es privado */
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
/** Busca el ID de un cliente por su nombre de usuario de forma segura con mutex */
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
/** Obtiene el nombre de usuario de un cliente por su ID de forma segura con mutex */
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
 * @brief Envía un mensaje a todos los clientes
 * @param senderId ID del cliente que envió el mensaje original (para logging)
 * @param msg Estructura Message a reenviar
 * @details Thread-safe: adquiere lock del mutex antes de iterar la lista
 */
/** Envía un mensaje a todos los clientes conectados de forma segura con mutex */
void broadcastMessage(int senderId, const Message& msg) {
    std::lock_guard<std::mutex> lock(clientsMutex);

    for (const auto& client : connectedClients) {
        sendToClient(client.clientId, msg);
    }
}

/**
 * @brief Maneja la comunicación con un cliente individual en un hilo separado
 * @param clientId ID del socket del cliente a gestionar
 * @details Recibe nombre de usuario, registra cliente, procesa mensajes en bucle,
 *          maneja tipos de mensaje (público, privado, desconexión), y limpia
 *          recursos al terminar. Se ejecuta en un hilo detached.
 */
/** Maneja la comunicación con un cliente específico en un hilo separado */
void handleClient(int clientId) {
    std::vector<unsigned char> buffer;
    std::string username = "User_" + std::to_string(clientId);
    bool isConnected = true;

    std::cout << "[INFO] Cliente " << clientId << " conectado. Esperando nombre de usuario..." << std::endl;

        try {
            /** Espera el mensaje de conexión usando operaciones directas del socket */
            int bufferSize = 0;
            int readData = read(clientList[clientId].socket, &bufferSize, sizeof(int));
            if (readData <= 0) {
                std::cout << "[ERROR] No se pudo leer el tamaño del mensaje de conexión del cliente " << clientId << std::endl;
                closeConnection(clientId);
                return;
            }

            buffer.resize(bufferSize);
            int remaining = bufferSize;
            while (remaining > 0) {
                int bytesRead = read(clientList[clientId].socket, &buffer[bufferSize - remaining], remaining);
                if (bytesRead <= 0) {
                    std::cout << "[ERROR] Error al leer datos de conexión del cliente " << clientId << std::endl;
                    closeConnection(clientId);
                    return;
                }
                remaining -= bytesRead;
            }

        /** Desempaqueta el tipo de mensaje */
        int msgType = unpack<int>(buffer);
        if (msgType != MSG_CONNECT) {
            std::cout << "[ERROR] Se esperaba MSG_CONNECT, recibido tipo " << msgType << " del cliente " << clientId << std::endl;
            closeConnection(clientId);
            return;
        }

        /** Desempaqueta el nombre de usuario */
        username.clear();
        while (!buffer.empty()) {
            char c = unpack<char>(buffer);
            if (c == '\0') break;
            username += c;
        }

        /** Desempaqueta el contenido (debería estar vacío para MSG_CONNECT) */
        std::string content;
        while (!buffer.empty()) {
            char c = unpack<char>(buffer);
            if (c == '\0') break;
            content += c;
        }

        /** Registra el cliente en la lista compartida */
        {
            std::lock_guard<std::mutex> lock(clientsMutex);
            connectedClients.emplace_back(clientId, username);
        }

        std::cout << "[CONEXIÓN] Usuario '" << username << "' (ID: " << clientId << ") se ha unido al chat" << std::endl;

        /** Notifica a todos los demás usuarios sobre la nueva conexión */
        Message joinMsg(MSG_PUBLIC, "SERVIDOR", username + " se ha unido al chat");
        broadcastMessage(clientId, joinMsg);

        /** Bucle para recibir y procesar mensajes del cliente */
        while (isConnected) {
            buffer.clear();

            /** Lee el tamaño del mensaje entrante */
            int bufferSize = 0;
            int readData = read(clientList[clientId].socket, &bufferSize, sizeof(int));
            if (readData <= 0) {
                std::cout << "[DESCONEXIÓN] Cliente " << clientId << " (" << username << ") desconectado" << std::endl;
                isConnected = false;
                break;
            }

            buffer.resize(bufferSize);
            int remaining = bufferSize;
            while (remaining > 0) {
                int bytesRead = read(clientList[clientId].socket, &buffer[bufferSize - remaining], remaining);
                if (bytesRead <= 0) {
                    std::cout << "[DESCONEXIÓN] Cliente " << clientId << " (" << username << ") desconectado" << std::endl;
                    isConnected = false;
                    break;
                }
                remaining -= bytesRead;
            }

            if (!isConnected) break;

            /** Desempaqueta el mensaje recibido */
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

            /** Procesa el mensaje según su tipo */
            if (msgType == MSG_DISCONNECT) {
                std::cout << "[DESCONEXIÓN] Usuario '" << username << "' ha salido del chat" << std::endl;

                /** Notifica a todos los demás sobre la desconexión */
                Message leaveMsg(MSG_PUBLIC, "SERVIDOR", username + " ha salido del chat");
                broadcastMessage(clientId, leaveMsg);

                /** BONUS 1: Envía confirmación de desconexión antes de cerrar */
                Message disconnectConfirm(MSG_DISCONNECT, "SERVIDOR", "Desconexión confirmada");
                sendToClient(clientId, disconnectConfirm);

                isConnected = false;
                break;

            } else if (msgType == MSG_PRIVATE) {
                /** BONUS 2: Maneja mensaje privado */
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

                    /** Confirma al remitente que el mensaje fue enviado */
                    Message confirmMsg(MSG_PUBLIC, "SERVIDOR",
                        "Mensaje privado enviado a " + recipient);
                    sendToClient(clientId, confirmMsg);
                } else {
                    /** Usuario destinatario no encontrado */
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

    /** Limpia el cliente de la lista compartida */
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
/** Función principal del servidor que inicia el servicio y acepta conexiones */
int main() {
    const int PORT = 3000;

    std::cout << "========================================" << std::endl;
    std::cout << "              SERVIDOR AEC2             " << std::endl;
    std::cout << "========================================" << std::endl;
    std::cout << std::endl;

    /** Inicializa el servidor en el puerto especificado */
    int serverSocket = initServer(PORT);
    if (serverSocket < 0) {
        std::cerr << "[ERROR] No se pudo inicializar el servidor en el puerto " << PORT << std::endl;
        return 1;
    }

    std::cout << "[OK] Servidor iniciado en localhost:" << PORT << std::endl;
    std::cout << "[INFO] Esperando conexiones de clientes..." << std::endl;
    std::cout << std::endl;

    std::list<std::thread> clientThreads;

    /** Bucle principal para aceptar nuevos clientes */
    while (true) {
        /** Comprueba si hay nuevos clientes intentando conectar */
        bool result = checkClient();

        if (result) {
            /** Nuevo cliente conectado */
            int clientId = getLastClientID();

            /** Crea un hilo detached para manejar la comunicación con este cliente */
            clientThreads.emplace_back(handleClient, clientId);
            clientThreads.back().detach(); /** Detach para ejecutar de forma independiente */
        }

        /** Pausa breve para evitar sobrecargar el CPU */
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
