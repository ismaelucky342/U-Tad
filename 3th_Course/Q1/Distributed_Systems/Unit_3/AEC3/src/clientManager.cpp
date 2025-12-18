#include "../includes/clientManager.h"
#include <iostream>

void ClientManager::attendClient(int clientID)
{
    while (true)
    {
        std::vector<unsigned char> msg;
        try
        {
            recvMSG<unsigned char>(clientID, msg);
        }
        catch (...)
        {
            // connection closed
            break;
        }
        if (msg.empty())
            break;
        std::string command = unpack<std::string>(msg);
        if (command == "CREATE")
        {
            std::string path = unpack<std::string>(msg);
            FileManager *fm = new FileManager(path);
            instances[nextID] = fm;
            std::vector<unsigned char> resp;
            pack(resp, nextID);
            sendMSG<unsigned char>(clientID, resp);
            nextID++;
        }
        else if (command == "DESTROY")
        {
            int id = unpack<int>(msg);
            if (instances.find(id) != instances.end())
            {
                delete instances[id];
                instances.erase(id);
            }
        }
        else if (command == "LIST")
        {
            int id = unpack<int>(msg);
            if (instances.find(id) != instances.end())
            {
                auto files = instances[id]->listFiles();
                std::vector<unsigned char> resp;
                pack(resp, (int)files.size());
                for (auto &f : files)
                {
                    pack(resp, f);
                }
                sendMSG<unsigned char>(clientID, resp);
            }
        }
        else if (command == "READ")
        {
            int id = unpack<int>(msg);
            std::string filename = unpack<std::string>(msg);
            if (instances.find(id) != instances.end())
            {
                std::vector<unsigned char> data;
                instances[id]->readFile(filename, data);
                std::vector<unsigned char> resp;
                pack(resp, (int)data.size());
                if (!data.empty())
                {
                    packv<unsigned char>(resp, data.data(), data.size());
                }
                sendMSG<unsigned char>(clientID, resp);
            }
        }
        else if (command == "WRITE")
        {
            int id = unpack<int>(msg);
            std::string filename = unpack<std::string>(msg);
            int size = unpack<int>(msg);
            std::vector<unsigned char> data(size);
            if (size > 0)
            {
                unpackv<unsigned char>(msg, data.data(), size);
            }
            if (instances.find(id) != instances.end())
            {
                instances[id]->writeFile(filename, data);
            }
        }
    }
}