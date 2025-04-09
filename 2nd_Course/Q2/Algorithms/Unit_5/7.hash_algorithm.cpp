#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    // Create an unordered_map to store key-value pairs
    std::unordered_map<std::string, int> hashTable;

    // Insert some key-value pairs into the hash table
    hashTable["apple"] = 5;
    hashTable["banana"] = 3;
    hashTable["cherry"] = 7;

    // Search for a key in the hash table
    std::string key = "banana";
    if (hashTable.find(key) != hashTable.end()) {
        std::cout << "Key: " << key << ", Value: " << hashTable[key] << std::endl;
    } else {
        std::cout << "Key: " << key << " not found in the hash table." << std::endl;
    }

    // Iterate through the hash table and print all key-value pairs
    std::cout << "Hash table contents:" << std::endl;
    for (const auto& pair : hashTable) {
        std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
    }

    return 0;
}