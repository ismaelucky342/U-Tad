#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& list) {
    int n = list.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (list[j] < list[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(list[i], list[min_idx]);
    }
}

void printList(const std::vector<int>& list) {
    for (int num : list) std::cout << num << " ";
    std::cout << "\n";
}

int main() {
    std::vector<int> numbers = {29, 10, 14, 37, 14};

    std::cout << "Lista original:\n";
    printList(numbers);

    selectionSort(numbers);

    std::cout << "Lista ordenada con Selection Sort:\n";
    printList(numbers);

    return 0;
}
