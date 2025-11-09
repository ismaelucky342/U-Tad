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

#ifndef PROTOCOL_H
#define PROTOCOL_H

#include <iostream>
#include <thread>
#include <atomic>
#include <sstream>
#include <string>
#include <list>
#include <thread>
#include <mutex>
#include <algorithm>
#include <cstring>
#include "../include/utils.h"


// Tipos de mensajes
enum MessageType {
    MSG_PUBLIC = 0,     //  público (broadcast)
    MSG_PRIVATE = 1,    //  privado a un usuario específico
    MSG_DISCONNECT = 2, //  de desconexión ordenada
    MSG_CONNECT = 3     //  de conexión (envío de nombre)
};

// Estructura para mensajes
struct Message {
    MessageType type;
    std::string username;
    std::string content;
    std::string recipient;  
    
    Message() : type(MSG_PUBLIC), username(""), content(""), recipient("") {}
    Message(MessageType t, const std::string& user, const std::string& msg, const std::string& recip = "")
        : type(t), username(user), content(msg), recipient(recip) {}
};

// Estructura para almacenar información del cliente
struct ClientInfo {
    int clientId;
    std::string username;
    
    ClientInfo(int id, const std::string& name) : clientId(id), username(name) {}
};

#endif 
