#include <iostream>
#include <vector>

void merge(std::vector<int>& list, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<int> L(n1);
    std::vector<int> R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = list[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = list[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            list[k++] = L[i++];
        } else {
            list[k++] = R[j++];
        }
    }

    while (i < n1) {
        list[k++] = L[i++];
    }
    while (j < n2) {
        list[k++] = R[j++];
    }
}

void mergeSort(std::vector<int>& list, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(list, left, mid);
        mergeSort(list, mid + 1, right);
        merge(list, left, mid, right);
    }
}

void printList(const std::vector<int>& list) {
    for (int num : list) std::cout << num << " ";
    std::cout << "\n";
}

int main() {
    std::vector<int> numbers = {38, 27, 43, 3, 9, 82, 10};

    std::cout << "Lista original:\n";
    printList(numbers);

    mergeSort(numbers, 0, numbers.size() - 1);

    std::cout << "Lista ordenada con Merge Sort:\n";
    printList(numbers);

    return 0;
}
