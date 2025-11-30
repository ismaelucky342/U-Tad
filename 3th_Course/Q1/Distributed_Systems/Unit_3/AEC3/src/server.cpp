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
#include <regex>  // Para validación de IP

#define BROKER_PORT 8080

static std::atomic<bool> running{true};
static void handle_sigint(int) { running.store(false); }

// Función simple para validar IP (IPv4 básica)
bool isValidIP(const std::string& ip) {
    std::regex ipRegex(R"(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$)");
    if (!std::regex_match(ip, ipRegex)) return false;
    std::stringstream ss(ip);
    std::string token;
    while (std::getline(ss, token, '.')) {
        int num = std::stoi(token);
        if (num < 0 || num > 255) return false;
    }
    return true;
}

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
    if (argc > 2) {
        brokerHost = argv[2];
        if (!isValidIP(brokerHost)) {
            std::cerr << "IP del Broker inválida: " << brokerHost << ", usando 127.0.0.1" << std::endl;
            brokerHost = "127.0.0.1";
        }
    }
    if (argc > 3) {
        myPublicIP = argv[3];
        if (!isValidIP(myPublicIP)) {
            std::cerr << "IP pública inválida: " << myPublicIP << ", usando 127.0.0.1" << std::endl;
            myPublicIP = "127.0.0.1";
        }
    }

    std::signal(SIGINT, handle_sigint);

    // register with Broker
    connection_t brokerConn = initClient(brokerHost, BROKER_PORT);
    if (brokerConn.socket != -1) {
        std::vector<unsigned char> msg;
        try {
            pack(msg, std::string("SERVER"));
            pack(msg, myPublicIP);
            pack(msg, port);
            std::cout << "Debug: Packed message size: " << msg.size() << std::endl;  // Debug
            sendMSG<unsigned char>(brokerConn.id, msg);
            closeConnection(brokerConn.id);
            std::cout << "Registered with Broker: " << brokerHost << ":" << BROKER_PORT << std::endl;
        } catch (const std::exception& e) {
            std::cerr << "Error during registration: " << e.what() << std::endl;
            closeConnection(brokerConn.id);
        }
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