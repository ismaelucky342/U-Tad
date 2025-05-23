#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& list) {
    int n = list.size();
    for (int i = 1; i < n; i++) {
        int key = list[i];
        int j = i - 1;

        // Mover los elementos que son mayores que la key
        while (j >= 0 && list[j] > key) {
            list[j + 1] = list[j];
            j--;
        }
        list[j + 1] = key;
    }
}

void printList(const std::vector<int>& list) {
    for (int num : list) std::cout << num << " ";
    std::cout << "\n";
}

int main() {
    std::vector<int> numbers = {12, 11, 13, 5, 6};

    std::cout << "Lista original:\n";
    printList(numbers);

    insertionSort(numbers);

    std::cout << "Lista ordenada con Insertion Sort:\n";
    printList(numbers);

    return 0;
}
