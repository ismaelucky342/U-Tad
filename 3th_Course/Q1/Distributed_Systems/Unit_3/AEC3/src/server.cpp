#include "../includes/utils.h"
#include "../includes/clientManager.h"
#include <iostream>
#include <string>
#include <thread>
#include <list>
#include <chrono>
#include <unistd.h>
#include <atomic>
#include <csignal>
#include <cstdlib>
#include <vector>

#define BROKER_PORT 8080

static std::atomic<bool> running{true};
static void handle_sigint(int) { running.store(false); }

int main(int argc, char** argv) {
    int port = 8081;
    std::string brokerHost = "127.0.0.1";
    std::string myPublicIP = "127.0.0.1";

    if (argc > 1) {
        try {
            int p = std::stoi(argv[1]);
            if (p > 0 && p < 65536) port = p;
            else std::cerr << "Puerto fuera de rango, usando " << port << std::endl;
        } catch (...) {
            std::cerr << "Puerto inválido, usando " << port << std::endl;
        }
    }
    if (argc > 2) brokerHost = argv[2];
    if (argc > 3) myPublicIP = argv[3];

    std::signal(SIGINT, handle_sigint);

    // register with Broker
    connection_t brokerConn = initClient(brokerHost, BROKER_PORT);
    if (brokerConn.socket != -1) {
        std::vector<unsigned char> msg;
        pack(msg, std::string("SERVER"));
        pack(msg, myPublicIP);
        pack(msg, port);
        sendMSG<unsigned char>(brokerConn.id, msg);
        closeConnection(brokerConn.id);
        std::cout << "Registered with Broker: " << brokerHost << ":" << BROKER_PORT << std::endl;
    } else {
        std::cerr << "Failed to connect to Broker at " << brokerHost << ":" << BROKER_PORT << ", continuing..." << std::endl;
    }

    int server_fd = initServer(port);
    if (server_fd == -1) {
        std::cerr << "initServer failed on port " << port << std::endl;
        return 1;
    }
    ClientManager cm;
    std::vector<std::thread> threads;
    while (running.load()) {
        if (checkClient()) {
            int clientID = getLastClientID();
            threads.emplace_back(&ClientManager::attendClient, &cm, clientID);
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    std::cerr << "Shutting down server..." << std::endl;
    for (auto& t : threads) if (t.joinable()) t.join();
    ::close(server_fd);
    return 0;
}