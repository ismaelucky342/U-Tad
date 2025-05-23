#include <iostream>
#include <vector>

int partition(std::vector<int>& list, int low, int high) {
    int pivot = list[high];  // pivote como último elemento
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (list[j] < pivot) {
            i++;
            std::swap(list[i], list[j]);
        }
    }
    std::swap(list[i + 1], list[high]);
    return i + 1;
}

void quickSort(std::vector<int>& list, int low, int high) {
    if (low < high) {
        int pi = partition(list, low, high);

        quickSort(list, low, pi - 1);
        quickSort(list, pi + 1, high);
    }
}

void printList(const std::vector<int>& list) {
    for (int num : list) std::cout << num << " ";
    std::cout << "\n";
}

int main() {
    std::vector<int> numbers = {10, 7, 8, 9, 1, 5};

    std::cout << "Lista original:\n";
    printList(numbers);

    quickSort(numbers, 0, numbers.size() - 1);

    std::cout << "Lista ordenada con Quick Sort:\n";
    printList(numbers);

    return 0;
}
