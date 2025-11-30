#include "../includes/filemanager.h"
#include "../includes/utils.h"
#include <string>
#include <vector>
#include <cstdlib>
#include <iostream>

#define BROKER_HOST "127.0.0.1"
#define BROKER_PORT 8080

static int clientID = -1;
static bool connected = false;
static int instID = -1;

/**
 * @brief Default constructor for FileManager. Sets ready to false.
 */
FileManager::FileManager() {
    ready = false;
}

/**
 * @brief Constructor for FileManager that connects to a remote server via Broker.
 * @param path The directory path for the FileManager on the server.
 */
FileManager::FileManager(string path) {
    if (!connected) {
        const char* env_broker_ip = std::getenv("BROKER_IP");
        std::string broker_ip = (env_broker_ip) ? std::string(env_broker_ip) : "127.0.0.1";

        connection_t conn = initClient(broker_ip, BROKER_PORT);
        if (conn.socket == -1) {
            std::cerr << "Failed to connect to Broker" << std::endl;
            ready = false;
            return;
        }
        int brokerID = conn.id;
        // send "CLIENT"
        std::vector<unsigned char> msg;
        pack(msg, std::string("CLIENT"));
        sendMSG<unsigned char>(brokerID, msg);
        // recv server host and port
        std::vector<unsigned char> resp;
        recvMSG<unsigned char>(brokerID, resp);
        std::string serverHost = unpack<std::string>(resp);
        int serverPort = unpack<int>(resp);
        // close broker connection
        closeConnection(brokerID);
        if (serverHost.empty()) {
            std::cerr << "No servers available" << std::endl;
            ready = false;
            return;
        }
        // connect to server
        conn = initClient(serverHost, serverPort);
        if (conn.socket == -1) {
            std::cerr << "Failed to connect to Server" << std::endl;
            ready = false;
            return;
        }
        clientID = conn.id;
        connected = true;
    }
    std::vector<unsigned char> msg;
    pack(msg, std::string("CREATE"));
    pack(msg, path);
    sendMSG<unsigned char>(clientID, msg);
    std::vector<unsigned char> resp;
    recvMSG<unsigned char>(clientID, resp);
    instID = unpack<int>(resp);
    dirPath = path;
    ready = true;
}

/**
 * @brief Destructor for FileManager. Sends DESTROY command to server if connected.
 */
FileManager::~FileManager() {
    if (ready && instID != -1) {
        std::vector<unsigned char> msg;
        pack(msg, std::string("DESTROY"));
        pack(msg, instID);
        sendMSG<unsigned char>(clientID, msg);
        // no response
    }
}

/**
 * @brief Lists files in the remote FileManager directory.
 * @return Vector of file names.
 */
vector<string> FileManager::listFiles() {
    if (!ready) return {};
    std::vector<unsigned char> msg;
    pack(msg, std::string("LIST"));
    pack(msg, instID);
    sendMSG<unsigned char>(clientID, msg);
    std::vector<unsigned char> resp;
    recvMSG<unsigned char>(clientID, resp);
    int numFiles = unpack<int>(resp);
    vector<string> files;
    for (int i = 0; i < numFiles; i++) {
        string f = unpack<std::string>(resp);
        files.push_back(f);
    }
    return files;
}

/**
 * @brief Reads a file from the remote FileManager.
 * @param fileName Name of the file to read.
 * @param data Vector to store the file data.
 */
void FileManager::readFile(string fileName, vector<unsigned char> &data) {
    if (!ready) return;
    std::vector<unsigned char> msg;
    pack(msg, std::string("READ"));
    pack(msg, instID);
    pack(msg, fileName);
    sendMSG<unsigned char>(clientID, msg);
    std::vector<unsigned char> resp;
    recvMSG<unsigned char>(clientID, resp);
    int size = unpack<int>(resp);
    data.resize(size);
    if (size > 0) {
        unpackv<unsigned char>(resp, data.data(), size);
    }
}

/**
 * @brief Writes a file to the remote FileManager.
 * @param fileName Name of the file to write.
 * @param data Data to write.
 */
void FileManager::writeFile(string fileName, vector<unsigned char> &data) {
    if (!ready) return;
    std::vector<unsigned char> msg;
    pack(msg, std::string("WRITE"));
    pack(msg, instID);
    pack(msg, fileName);
    int size = data.size();
    pack(msg, size);
    if (size > 0) {
        packv<unsigned char>(msg, data.data(), size);
    }
    sendMSG<unsigned char>(clientID, msg);
    // no response
}