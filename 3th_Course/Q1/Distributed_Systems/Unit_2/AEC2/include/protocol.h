/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Sistemas Distribuidos       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        27/11/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    29/11/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*      Ismael Hernandez Clemente          ismael.hernandez@live.u-tad.com             */
/*                                                                                     */
/***************************************************************************************/

#ifndef PROTOCOL_H
#define PROTOCOL_H

#include <string>

// Tipos de mensajes
enum MessageType {
    MSG_PUBLIC = 0,     // Mensaje público (broadcast)
    MSG_PRIVATE = 1,    // Mensaje privado a un usuario específico
    MSG_DISCONNECT = 2, // Mensaje de desconexión ordenada
    MSG_CONNECT = 3     // Mensaje de conexión (envío de nombre)
};

// Estructura para mensajes
struct Message {
    MessageType type;
    std::string username;
    std::string content;
    std::string recipient;  // Para mensajes privados
    
    Message() : type(MSG_PUBLIC), username(""), content(""), recipient("") {}
    Message(MessageType t, const std::string& user, const std::string& msg, const std::string& recip = "")
        : type(t), username(user), content(msg), recipient(recip) {}
};

#endif // PROTOCOL_H
