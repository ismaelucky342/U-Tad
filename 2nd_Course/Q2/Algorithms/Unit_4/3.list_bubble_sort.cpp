#include <iostream>
#include <list>

void bubbleSort(std::list<int>& lst) {
    bool swapped;
    do {
        swapped = false;
        for (auto it = lst.begin(); it != std::prev(lst.end()); ++it) {
            auto next = std::next(it);
            if (*it > *next) {
                std::iter_swap(it, next);
                swapped = true;
            }
        }
    } while (swapped);
}

void printList(const std::list<int>& lst) {
    for (const auto& val : lst) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::list<int> numbers = {34, 7, 23, 32, 5, 62};

    std::cout << "Original list: ";
    printList(numbers);

    bubbleSort(numbers);

    std::cout << "Sorted list: ";
    printList(numbers);

    return 0;
}