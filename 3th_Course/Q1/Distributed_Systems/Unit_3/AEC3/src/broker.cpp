#include "../includes/utils.h"
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <chrono>

struct ServerInfo {
    std::string host;
    int port;
    int connections;
};

/**
 * @brief Main function for the Broker server.
 * Manages server registrations and client requests for load balancing.
 * @param argc Number of command line arguments.
 * @param argv Command line arguments, argv[1] can be the port.
 * @return 0 on success.
 */
int main(int argc, char** argv) {
    int port = 8080;
    if (argc > 1) port = atoi(argv[1]);

    int server_fd = initServer(port);
    std::vector<ServerInfo> servers;

    while (true) {
        if (checkClient()) {
            int clientID = getLastClientID();
            std::vector<unsigned char> msg;
            recvMSG<unsigned char>(clientID, msg);
            if (msg.empty()) {
                std::cerr << "ERROR: Client/Server closed connection. Cleaning up." << std::endl;
                closeConnection(clientID); 
                continue; 
            }
            std::string type = unpack<std::string>(msg);
            if (type == "SERVER") {
                std::string host = unpack<std::string>(msg);
                int port = unpack<int>(msg);
                servers.push_back({host, port, 0});
                std::cout << "Server registered: " << host << ":" << port << std::endl;
            } else if (type == "CLIENT") {
                if (servers.empty()) {
                    std::vector<unsigned char> resp;
                    pack(resp, std::string(""));
                    pack(resp, 0);
                    sendMSG<unsigned char>(clientID, resp);
                } else {
                    int minIdx = 0;
                    for (size_t i = 1; i < servers.size(); ++i) {
                        if (servers[i].connections < servers[minIdx].connections) minIdx = i;
                    }
                    servers[minIdx].connections++;
                    std::vector<unsigned char> resp;
                    pack(resp, servers[minIdx].host);
                    pack(resp, servers[minIdx].port);
                    sendMSG<unsigned char>(clientID, resp);
                }
            }
            closeConnection(clientID);
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    return 0;
}