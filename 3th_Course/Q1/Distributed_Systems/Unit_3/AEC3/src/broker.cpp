#include "../includes/utils.h"
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <chrono>
#include <mutex>
#include <atomic>
#include <csignal>
#include <cstdlib>

struct ServerInfo {
    std::string host;
    int port;
    int connections;
};

static std::atomic<bool> running{true};
static void handle_sigint(int) { running.store(false); }

/**
 * @brief Main function for the Broker server.
 * Manages server registrations and client requests for load balancing.
 * @param argc Number of command line arguments.
 * @param argv Command line arguments, argv[1] can be the port.
 * @return 0 on success.
 */
int main(int argc, char** argv) {
    int listenPort = 8080;
    if (argc > 1) listenPort = atoi(argv[1]);

    int server_fd = initServer(listenPort);
    if (server_fd == -1) {
        std::cerr << "Failed to init server on port " << listenPort << std::endl;
        return 1;
    }
    std::vector<ServerInfo> servers;
    std::mutex servers_mtx;
    std::signal(SIGINT, handle_sigint);

    while (running.load()) {
        if (checkClient()) {
            int clientID = getLastClientID();
            std::vector<unsigned char> msg;
            recvMSG<unsigned char>(clientID, msg);
            if (msg.empty()) {
                std::cerr << "ERROR: Empty message or lost connection (id=" << clientID << "). Cleaning up." << std::endl;
                closeConnection(clientID);
                continue;
            }
            std::string type = unpack<std::string>(msg);
            if (type == "SERVER") {
                std::string host = unpack<std::string>(msg);
                int srv_port = unpack<int>(msg);
                if (srv_port <= 0 || srv_port >= 65536) {
                    std::cerr << "WARNING: Invalid port " << srv_port << " from " << host << " (id=" << clientID << ")" << std::endl;
                } else {
                    std::lock_guard<std::mutex> lg(servers_mtx);
                    servers.push_back({host, srv_port, 0});
                    std::cout << "Server registered: " << host << ":" << srv_port << " (id=" << clientID << ")" << std::endl;
                }
            } else if (type == "CLIENT") {
                std::lock_guard<std::mutex> lg(servers_mtx);
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
            } else {
                std::cerr << "WARNING: Unknown type: " << type << " (id=" << clientID << ")" << std::endl;
            }
            closeConnection(clientID);
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
    std::cerr << "Shutting down broker..." << std::endl;
    ::close(server_fd);
    return 0;
}