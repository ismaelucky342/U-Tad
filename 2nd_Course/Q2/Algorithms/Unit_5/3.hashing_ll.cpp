#include <iostream>
#include <list>
#include <vector>
#include <string>

class HashTable {
private:
    int bucketCount; // Number of buckets
    std::vector<std::list<std::string>> table; // Hash table

    // Hash function to map values to key
    int hashFunction(const std::string& key) {
        int hash = 0;
        for (char ch : key) {
            hash = (hash * 31 + ch) % bucketCount;
        }
        return hash;
    }

public:
    HashTable(int buckets) : bucketCount(buckets) {
        table.resize(bucketCount);
    }

    // Insert a key into the hash table
    void insert(const std::string& key) {
        int index = hashFunction(key);
        table[index].push_back(key);
    }

    // Remove a key from the hash table
    void remove(const std::string& key) {
        int index = hashFunction(key);
        table[index].remove(key);
    }

    // Search for a key in the hash table
    bool search(const std::string& key) {
        int index = hashFunction(key);
        for (const auto& element : table[index]) {
            if (element == key) {
                return true;
            }
        }
        return false;
    }

    // Display the hash table
    void display() {
        for (int i = 0; i < bucketCount; ++i) {
            std::cout << "Bucket " << i << ": ";
            for (const auto& key : table[i]) {
                std::cout << key << " -> ";
            }
            std::cout << "NULL\n";
        }
    }
};

int main() {
    HashTable hashTable(10); // Create a hash table with 10 buckets

    // Insert keys
    hashTable.insert("apple");
    hashTable.insert("banana");
    hashTable.insert("grape");
    hashTable.insert("orange");
    hashTable.insert("mango");

    // Display the hash table
    std::cout << "Hash Table:\n";
    hashTable.display();

    // Search for keys
    std::cout << "\nSearching for 'banana': " << (hashTable.search("banana") ? "Found" : "Not Found") << "\n";
    std::cout << "Searching for 'pear': " << (hashTable.search("pear") ? "Found" : "Not Found") << "\n";

    // Remove a key
    std::cout << "\nRemoving 'grape'\n";
    hashTable.remove("grape");

    // Display the hash table after removal
    std::cout << "Hash Table after removal:\n";
    hashTable.display();

    return 0;
}