#include <iostream>
#include <list>

int main() {
    // Create a non-contiguous list of integers
    std::list<int> numbers = {10, 20, 30, 40, 50};

    // Insert elements
    numbers.push_front(5);  // Insert at the beginning
    numbers.push_back(60);  // Insert at the end

    // Display the list
    std::cout << "List elements: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Remove elements
    numbers.pop_front();  // Remove the first element
    numbers.pop_back();   // Remove the last element

    // Display the list after removal
    std::cout << "List after removal: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Insert at a specific position
    auto it = numbers.begin();
    std::advance(it, 2);  // Move iterator to the 3rd position
    numbers.insert(it, 25);

    // Display the list after insertion
    std::cout << "List after insertion: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}