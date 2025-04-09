#include <iostream>
#include <vector>
#include <algorithm>

class OrderedList {
private:
    std::vector<int> list;

public:
    // Insert an element in sorted order
    void insert(int value) {
        auto position = std::lower_bound(list.begin(), list.end(), value);
        list.insert(position, value);
    }

    // Remove an element if it exists
    bool remove(int value) {
        auto position = std::lower_bound(list.begin(), list.end(), value);
        if (position != list.end() && *position == value) {
            list.erase(position);
            return true;
        }
        return false;
    }

    // Check if an element exists
    bool contains(int value) const {
        return std::binary_search(list.begin(), list.end(), value);
    }

    // Print the ordered list
    void print() const {
        for (int value : list) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    OrderedList orderedList;

    orderedList.insert(5);
    orderedList.insert(3);
    orderedList.insert(8);
    orderedList.insert(1);

    std::cout << "Ordered List: ";
    orderedList.print();

    std::cout << "Contains 3? " << (orderedList.contains(3) ? "Yes" : "No") << std::endl;

    orderedList.remove(3);
    std::cout << "After removing 3: ";
    orderedList.print();

    return 0;
}