#include <iostream>
#include <vector>
#include <string>

class HashTable {
private:
    struct HashNode {
        std::string key;
        int value;
        bool isOccupied;
        HashNode() : key(""), value(0), isOccupied(false) {}
    };

    std::vector<HashNode> table;
    int capacity;

    int hashFunction(const std::string& key) {
        int hash = 0;
        for (char ch : key) {
            hash = (hash * 31 + ch) % capacity;
        }
        return hash;
    }

    int probe(int index) {
        return (index + 1) % capacity;
    }

public:
    HashTable(int size) : capacity(size) {
        table.resize(size);
    }

    void insert(const std::string& key, int value) {
        int index = hashFunction(key);
        while (table[index].isOccupied && table[index].key != key) {
            index = probe(index);
        }
        table[index].key = key;
        table[index].value = value;
        table[index].isOccupied = true;
    }

    int search(const std::string& key) {
        int index = hashFunction(key);
        int start = index;
        while (table[index].isOccupied) {
            if (table[index].key == key) {
                return table[index].value;
            }
            index = probe(index);
            if (index == start) break; // Full cycle, key not found
        }
        throw std::runtime_error("Key not found");
    }

    void remove(const std::string& key) {
        int index = hashFunction(key);
        int start = index;
        while (table[index].isOccupied) {
            if (table[index].key == key) {
                table[index].isOccupied = false;
                return;
            }
            index = probe(index);
            if (index == start) break; // Full cycle, key not found
        }
        throw std::runtime_error("Key not found");
    }

    void display() {
        for (int i = 0; i < capacity; ++i) {
            if (table[i].isOccupied) {
                std::cout << i << ": " << table[i].key << " -> " << table[i].value << "\n";
            } else {
                std::cout << i << ": [empty]\n";
            }
        }
    }
};

int main() {
    HashTable hashTable(10);

    hashTable.insert("apple", 5);
    hashTable.insert("banana", 10);
    hashTable.insert("orange", 15);

    hashTable.display();

    try {
        std::cout << "Value for 'apple': " << hashTable.search("apple") << "\n";
        hashTable.remove("apple");
        hashTable.display();
    } catch (const std::exception& e) {
        std::cerr << e.what() << "\n";
    }

    return 0;
}