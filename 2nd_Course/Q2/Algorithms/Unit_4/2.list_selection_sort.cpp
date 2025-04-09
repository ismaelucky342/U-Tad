#include <iostream>
#include <list>
#include <iterator>

void selectionSort(std::list<int>& lst) {
    for (auto it = lst.begin(); it != lst.end(); ++it) {
        auto minIt = it;
        for (auto jt = std::next(it); jt != lst.end(); ++jt) {
            if (*jt < *minIt) {
                minIt = jt;
            }
        }
        if (minIt != it) {
            std::swap(*it, *minIt);
        }
    }
}

void printList(const std::list<int>& lst) {
    for (const auto& val : lst) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::list<int> lst = {64, 34, 25, 12, 22, 11, 90};

    std::cout << "Original list: ";
    printList(lst);

    selectionSort(lst);

    std::cout << "Sorted list: ";
    printList(lst);

    return 0;
}