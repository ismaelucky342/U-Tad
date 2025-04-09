#include <iostream>
#include <vector>
#include <list>
#include <functional>

class HashTable {
private:
    std::vector<std::list<int>> table;
    size_t size;
    std::hash<int> hashFunction;

    size_t hash(int key) const {
        return hashFunction(key) % size;
    }

public:
    HashTable(size_t tableSize) : size(tableSize) {
        table.resize(size);
    }

    void insert(int key) {
        size_t index = hash(key);
        table[index].push_back(key);
    }

    bool search(int key) const {
        size_t index = hash(key);
        for (const int& element : table[index]) {
            if (element == key) {
                return true;
            }
        }
        return false;
    }

    void remove(int key) {
        size_t index = hash(key);
        table[index].remove(key);
    }

    void display() const {
        for (size_t i = 0; i < size; ++i) {
            std::cout << "Bucket " << i << ": ";
            for (const int& element : table[i]) {
                std::cout << element << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    HashTable hashTable(10);

    hashTable.insert(15);
    hashTable.insert(25);
    hashTable.insert(35);

    hashTable.display();

    std::cout << "Search 25: " << (hashTable.search(25) ? "Found" : "Not Found") << std::endl;

    hashTable.remove(25);
    hashTable.display();

    return 0;
}