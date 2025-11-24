#pragma once
#include "filemanager.h"
#include "utils.h"
#include <map>
#include <vector>
#include <string>

class ClientManager {
private:
    std::map<int, FileManager*> instances;
    int nextID = 0;
public:
/**
 * @brief Handles client requests for FileManager operations.
 * @param clientID The ID of the client connection.
 */
    void attendClient(int clientID);
};