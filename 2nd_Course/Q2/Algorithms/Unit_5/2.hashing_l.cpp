#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    // Create an unordered_map (hash table)
    std::unordered_map<std::string, int> hashTable;

    // Insert key-value pairs into the hash table
    hashTable["Alice"] = 25;
    hashTable["Bob"] = 30;
    hashTable["Charlie"] = 35;

    // Access elements using keys
    std::cout << "Alice's age: " << hashTable["Alice"] << std::endl;
    std::cout << "Bob's age: " << hashTable["Bob"] << std::endl;

    // Check if a key exists
    std::string key = "David";
    if (hashTable.find(key) != hashTable.end()) {
        std::cout << key << "'s age: " << hashTable[key] << std::endl;
    } else {
        std::cout << key << " not found in the hash table." << std::endl;
    }

    // Iterate through the hash table
    std::cout << "All entries in the hash table:" << std::endl;
    for (const auto& pair : hashTable) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}