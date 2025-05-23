#include <iostream>
#include <vector>

// Función para imprimir la lista
void printList(const std::vector<int>& list) {
    for (int num : list) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}

// Bubble Sort
void bubbleSort(std::vector<int>& list) {
    bool swapped;
    int n = list.size();
    do {
        swapped = false;
        for (int i = 1; i < n; i++) {
            if (list[i - 1] > list[i]) {
                std::swap(list[i - 1], list[i]);
                swapped = true;
            }
        }
        n--; // Después de cada pasada, el último elemento está ordenado
    } while (swapped);
}

int main() {
    std::vector<int> numbers = {64, 34, 25, 12, 22, 11, 90};

    std::cout << "Lista original:\n";
    printList(numbers);

    bubbleSort(numbers);

    std::cout << "Lista ordenada con Bubble Sort:\n";
    printList(numbers);

    return 0;
}
