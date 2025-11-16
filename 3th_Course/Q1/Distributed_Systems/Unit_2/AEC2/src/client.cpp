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

/** Variables globales para el estado del cliente */
std::atomic<bool> isRunning(true);
int clientSocket = -1;
std::string myUsername;

/**
 * @brief Envía un mensaje al servidor empaquetando todos sus campos
 * @param msg Estructura Message con tipo, usuario, contenido y destinatario (si aplica)
 */
void sendMessage(const Message& msg) {
    std::vector<unsigned char> buffer;

    /** Empaqueta el tipo de mensaje en el buffer para enviarlo al servidor */
    int tipo = static_cast<int>(msg.type);
    pack(buffer, tipo);

    /** Empaqueta el nombre de usuario en el buffer */
    for (char c : msg.username) {
        pack(buffer, c);
    }
    pack(buffer, '\0'); /** Agrega el terminador nulo para el username */

    /** Empaqueta el contenido del mensaje en el buffer */
    for (char c : msg.content) {
        pack(buffer, c);
    }
    pack(buffer, '\0');

    /** Si el mensaje es privado, empaqueta el destinatario */
    if (msg.type == MSG_PRIVATE) {
        for (char c : msg.recipient) {
            pack(buffer, c);
        }
        pack(buffer, '\0');
    }

    /** Envía el buffer completo al servidor a través del socket del cliente */
    int dataLen = buffer.size();
    write(clientSocket, &dataLen, sizeof(int));
    write(clientSocket, buffer.data(), dataLen);
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

        /** Recibe el tamaño del mensaje desde el socket del cliente */
        int bufferSize = 0;
        int readData = read(clientSocket, &bufferSize, sizeof(int));
        if (readData <= 0) {
            if (isRunning) {
                std::cout << "\n[INFO] Conexión cerrada por el servidor" << std::endl;
                isRunning = false;
            }
            break;
        }

        buffer.resize(bufferSize);
        int remaining = bufferSize;
        while (remaining > 0) {
            int bytesRead = read(clientSocket, &buffer[bufferSize - remaining], remaining);
            if (bytesRead <= 0) {
                std::cout << "\n[ERROR] Error al leer datos del servidor" << std::endl;
                isRunning = false;
                break;
            }
            remaining -= bytesRead;
        }

        if (!isRunning) break;

        try {
            /** Desempaqueta el tipo de mensaje del buffer */
            int msgType = unpack<int>(buffer);

            /** Desempaqueta el nombre de usuario del buffer */
            std::string username;
            while (!buffer.empty()) {
                char c = unpack<char>(buffer);
                if (c == '\0') break;
                username += c;
            }

            /** Desempaqueta el contenido del mensaje del buffer */
            std::string content;
            while (!buffer.empty()) {
                char c = unpack<char>(buffer);
                if (c == '\0') break;
                content += c;
            }

            /** Procesa el mensaje según su tipo */
            if (msgType == MSG_DISCONNECT) {
                /** Mensaje de desconexión enviado por el servidor */
                std::cout << "\n[INFO] " << content << std::endl;
                isRunning = false;
                break;

            } else if (msgType == MSG_PRIVATE) {
                /** Mensaje privado recibido, desempaqueta el destinatario */
                std::string recipient;
                while (!buffer.empty()) {
                    char c = unpack<char>(buffer);
                    if (c == '\0') break;
                    recipient += c;
                }
                std::cout << "\n[PRIVADO] " << username << " te dice: " << content << std::endl;
                std::cout << "> " << std::flush;

            } else if (msgType == MSG_PUBLIC) {
                /** Mensaje público recibido */
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
/** Muestra en la consola la lista de comandos disponibles para el usuario */
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
/** Procesa comandos especiales del usuario como /privado o /ayuda, retorna true si se procesó un comando */
bool processCommand(const std::string& input) {
    if (input == "/ayuda" || input == "/help") {
        showHelp();
        return true;
    }

    /** Comando para enviar mensaje privado: /privado <usuario> <mensaje> */
    if (input.substr(0, 8) == "/privado" || input.substr(0, 9) == "/private") {
        std::istringstream iss(input);
        std::string command, recipient, message;

        iss >> command;  /** Lee el comando */
        iss >> recipient; /** Lee el destinatario */

        if (recipient.empty()) {
            std::cout << "[ERROR] Uso: /privado <usuario> <mensaje>" << std::endl;
            return true;
        }

        /** Lee el resto de la línea como mensaje */
        std::getline(iss, message);
        if (!message.empty() && message[0] == ' ') {
            message = message.substr(1); /** Elimina el espacio inicial */
        }

        if (message.empty()) {
            std::cout << "[ERROR] El mensaje no puede estar vacío" << std::endl;
            return true;
        }

        /** Envía el mensaje privado al servidor */
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
/** Función principal del cliente que maneja la conexión y el bucle de mensajes */
int main() {
    const char* SERVER_IP = "127.0.0.1";
    const int PORT = 3000;

    std::cout << "========================================" << std::endl;
    std::cout << "            CLIENTE AEC2                " << std::endl;
    std::cout << "========================================" << std::endl;
    std::cout << std::endl;

    /** Solicita el nombre de usuario al iniciar */
    std::cout << "Por favor, ingresa tu nombre de usuario: ";
    std::getline(std::cin, myUsername);

    if (myUsername.empty()) {
        myUsername = "Anonymous";
    }

    std::cout << "\n[INFO] Conectando al servidor " << SERVER_IP << ":" << PORT << "..." << std::endl;

    /** Inicializa la conexión con el servidor */
    connection_t conn = initClient(std::string(SERVER_IP), PORT);
    clientSocket = conn.socket;  /** Usa el socket fd para enviar mensajes */
    int clientId = conn.serverId;  /** Guarda el ID del cliente para cerrar conexión */

    if (conn.socket < 0 || !conn.alive) {
        std::cerr << "[ERROR] No se pudo conectar al servidor" << std::endl;
        std::cerr << "[INFO] Asegúrate de que el servidor esté ejecutándose" << std::endl;
        return 1;
    }

    std::cout << "[OK] Conectado al servidor exitosamente" << std::endl;

    /** Envía el nombre de usuario al servidor para registrarse */
    Message connectMsg(MSG_CONNECT, myUsername, "");
    sendMessage(connectMsg);

    std::cout << "\n[INFO] ¡Bienvenido al chat, " << myUsername << "!" << std::endl;
    std::cout << "[INFO] Escribe '/ayuda' para ver los comandos disponibles" << std::endl;
    std::cout << "[INFO] Escribe 'exit()' para salir del chat" << std::endl;
    std::cout << std::endl;

    /** Inicia un hilo para recibir mensajes del servidor */
    std::thread receiverThread(receiveMessages);

    /** Bucle principal para leer y enviar mensajes del usuario */
    std::string input;
    while (isRunning) {
        std::cout << "> ";
        std::getline(std::cin, input);

        /** Verifica si se perdió la conexión */
        if (!isRunning) {
            break;
        }

        /** Ignora líneas vacías */
        if (input.empty()) {
            continue;
        }

        /** Comando para salir del chat */
        if (input == "exit()" || input == "exit" || input == "quit") {
            std::cout << "\n[INFO] Cerrando conexión..." << std::endl;

            /** Envía mensaje de desconexión al servidor */
            Message disconnectMsg(MSG_DISCONNECT, myUsername, "Desconectando");
            sendMessage(disconnectMsg);

            isRunning = false;
            break;
        }

        /** Procesa comandos especiales como /privado */
        if (processCommand(input)) {
            continue;
        }

        /** Envía el mensaje como público al servidor */
        Message publicMsg(MSG_PUBLIC, myUsername, input);
        sendMessage(publicMsg);
    }

    /** Espera a que el hilo receptor termine */
    if (receiverThread.joinable()) {
        receiverThread.join();
    }

    /** Cierra la conexión con el servidor */
    closeConnection(clientId);

    std::cout << "\n[INFO] Desconectado del servidor. ¡Hasta pronto!" << std::endl;

    return 0;
}
