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

// globales
std::atomic<bool> isRunning(true);
int clientSocket = -1;
std::string myUsername;

/**
 * @brief Envía un mensaje al servidor empaquetando todos sus campos
 * @param msg Estructura Message con tipo, usuario, contenido y destinatario (si aplica)
 */
void sendMessage(const Message& msg) {
    std::vector<unsigned char> buffer;
    
    // Empaquetar tipo de mensaje
    int tipo = static_cast<int>(msg.type);
    pack(buffer, tipo);
    
    // Empaquetar username
    for (char c : msg.username) {
        pack(buffer, c);
    }
    pack(buffer, '\0'); // Null terminator
    
    // Empaquetar contenido
    for (char c : msg.content) {
        pack(buffer, c);
    }
    pack(buffer, '\0');
    
    // Si es privado, empaquetar destinatario
    if (msg.type == MSG_PRIVATE) {
        for (char c : msg.recipient) {
            pack(buffer, c);
        }
        pack(buffer, '\0');
    }
    
    sendMSG(clientSocket, buffer);
}

/**
 * @brief Hilo para recibir mensajes del servidor continuamente
 * @details Se ejecuta en paralelo al hilo principal. Recibe mensajes en bucle,
 *          los desempaqueta y los muestra según su tipo. Termina cuando isRunning=false
 *          o cuando el servidor cierra la conexión.
 */
void receiveMessages() {
    std::vector<unsigned char> buffer;
    
    while (isRunning) {
        buffer.clear();
        recvMSG(clientSocket, buffer);
        
        if (buffer.empty()) {
            if (isRunning) {
                std::cout << "\n[INFO] Conexión cerrada por el servidor" << std::endl;
                isRunning = false;
            }
            break;
        }
        
        try {
            // Desempaquetar tipo
            int msgType = unpack<int>(buffer);
            
            // Desempaquetar username
            std::string username;
            while (!buffer.empty()) {
                char c = unpack<char>(buffer);
                if (c == '\0') break;
                username += c;
            }
            
            // Desempaquetar contenido
            std::string content;
            while (!buffer.empty()) {
                char c = unpack<char>(buffer);
                if (c == '\0') break;
                content += c;
            }
            
            // Procesar según tipo 
            if (msgType == MSG_DISCONNECT) {
                // Mensaje de desconexión del servidor
                std::cout << "\n[INFO] " << content << std::endl;
                isRunning = false;
                break;
                
            } else if (msgType == MSG_PRIVATE) {
                // Mensaje privado recibido - desempaquetar destinatario
                std::string recipient;
                while (!buffer.empty()) {
                    char c = unpack<char>(buffer);
                    if (c == '\0') break;
                    recipient += c;
                }
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
 * @brief Muestra la ayuda de comandos disponibles en la consola
 * @details Lista todos los comandos que el usuario puede utilizar en el chat
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
 * @brief Procesa comandos especiales del usuario (/privado, /ayuda, etc.)
 * @param input Cadena ingresada por el usuario
 * @return true si se procesó un comando especial, false si es un mensaje normal
 * @details Si el comando es inválido, muestra mensaje de error y retorna true
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
 * @return 0 si la ejecución fue exitosa, 1 si hubo error
 * @details Solicita nombre de usuario, conecta al servidor en 127.0.0.1:3000,
 *          crea hilo para recibir mensajes, y gestiona el bucle de envío de mensajes.
 *          Maneja desconexión ordenada con exit() y limpia recursos al terminar.
 */
int main() {
    const char* SERVER_IP = "127.0.0.1";
    const int PORT = 3000;
    
    std::cout << "========================================" << std::endl;
    std::cout << "            CLIENTE AEC2                " << std::endl;
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
    connection_t conn = initClient(std::string(SERVER_IP), PORT);
    clientSocket = conn.serverId;  // Usar el ID del cliente, no el socket directo
    
    if (conn.socket < 0 || !conn.alive) {
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
