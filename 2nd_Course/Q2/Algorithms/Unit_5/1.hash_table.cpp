#include <iostream>
#include <list>
#include <vector>
#include <string>

class HashTable {
private:
    std::vector<std::list<std::pair<int, std::string>>> table;
    int size;

    int hashFunction(int key) const {
        return key % size;
    }

public:
    HashTable(int tableSize) : size(tableSize) {
        table.resize(size);
    }

    void insert(int key, const std::string& value) {
        int index = hashFunction(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value; // Update value if key already exists
                return;
            }
        }
        table[index].emplace_back(key, value);
    }

    std::string search(int key) const {
        int index = hashFunction(key);
        for (const auto& pair : table[index]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        return "Key not found";
    }

    void remove(int key) {
        int index = hashFunction(key);
        table[index].remove_if([key](const std::pair<int, std::string>& pair) {
            return pair.first == key;
        });
    }

    void display() const {
        for (int i = 0; i < size; ++i) {
            std::cout << "Bucket " << i << ": ";
            for (const auto& pair : table[i]) {
                std::cout << "[" << pair.first << ": " << pair.second << "] ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    HashTable hashTable(10);

    hashTable.insert(1, "Alice");
    hashTable.insert(2, "Bob");
    hashTable.insert(12, "Charlie");

    hashTable.display();

    std::cout << "Search key 2: " << hashTable.search(2) << std::endl;

    hashTable.remove(2);
    hashTable.display();

    return 0;
}