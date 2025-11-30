#include "../includes/utils.h"
#include "../includes/clientManager.h"
#include <iostream>
#include <string>
#include <thread>
#include <list>
#include <chrono>

#define BROKER_PORT 8080

/**
 * @brief Main function for the FileManager server.
 * Registers with Broker and handles client connections.
 * @param argc Number of command line arguments.
 * @param argv Command line arguments, argv[1] can be the port.
 * @return 0 on success.
 * Uso: ./Server <PUERTO_SERVER> <IP_BROKER> <IP_PUBLICA_DE_ESTE_SERVER>
 */
int main(int argc, char** argv)
{
    int port = 8081;
    std::string brokerHost = "127.0.0.1";
    std::string myPublicIP = "127.0.0.1";

    if (argc > 1) port = atoi(argv[1]);
    if (argc > 2) brokerHost = argv[2];
    if (argc > 3) myPublicIP = argv[3];
    // register with Broker
    connection_t brokerConn = initClient(brokerHost, BROKER_PORT);    
    if (brokerConn.socket != -1) {
        std::vector<unsigned char> msg;
        pack(msg, std::string("SERVER"));
        pack(msg, myPublicIP); 
        
        pack(msg, port);
        sendMSG<unsigned char>(brokerConn.id, msg);
        closeConnection(brokerConn.id);
    } else {
        std::cerr << "Failed to connect to Broker, continuing without registration" << std::endl;
    }

    int server_fd = initServer(port);
    ClientManager cm;
    while (true) {
        if (checkClient()) {
            int clientID = getLastClientID();
            std::thread t(&ClientManager::attendClient, &cm, clientID);
            t.detach();
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    return 0;
}
