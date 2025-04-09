#include <iostream>
#include <list>
#include <vector>

class HashTable {
private:
    int bucketCount; // Number of buckets
    std::vector<std::list<int>> table; // Array of lists for separate chaining

    int hashFunction(int key) {
        return key % bucketCount; // Simple modulo-based hash function
    }

public:
    HashTable(int buckets) : bucketCount(buckets), table(buckets) {}

    void insert(int key) {
        int index = hashFunction(key);
        table[index].push_back(key);
    }

    void remove(int key) {
        int index = hashFunction(key);
        table[index].remove(key);
    }

    bool search(int key) {
        int index = hashFunction(key);
        for (int element : table[index]) {
            if (element == key) {
                return true;
            }
        }
        return false;
    }

    void display() {
        for (int i = 0; i < bucketCount; ++i) {
            std::cout << "Bucket " << i << ": ";
            for (int element : table[i]) {
                std::cout << element << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    HashTable hashTable(5); // Create a hash table with 5 buckets

    hashTable.insert(10);
    hashTable.insert(15);
    hashTable.insert(20);
    hashTable.insert(25);
    hashTable.insert(30);

    std::cout << "Hash Table:" << std::endl;
    hashTable.display();

    std::cout << "Search 15: " << (hashTable.search(15) ? "Found" : "Not Found") << std::endl;

    hashTable.remove(15);
    std::cout << "After removing 15:" << std::endl;
    hashTable.display();

    return 0;
}