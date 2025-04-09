#include <iostream>
#include <list>

void insertionSort(std::list<int>& lst) {
    if (lst.empty()) return;

    auto it = lst.begin();
    ++it; // Start from the second element

    for (; it != lst.end(); ++it) {
        int key = *it;
        auto prev = it;
        --prev;

        while (prev != lst.begin() && *prev > key) {
            auto next = prev;
            ++next;
            *next = *prev;
            --prev;
        }

        if (*prev > key) {
            auto next = prev;
            ++next;
            *next = *prev;
            *prev = key;
        } else {
            auto next = prev;
            ++next;
            *next = key;
        }
    }
}

void printList(const std::list<int>& lst) {
    for (int val : lst) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::list<int> lst = {5, 2, 9, 1, 5, 6};

    std::cout << "Original list: ";
    printList(lst);

    insertionSort(lst);

    std::cout << "Sorted list: ";
    printList(lst);

    return 0;
}