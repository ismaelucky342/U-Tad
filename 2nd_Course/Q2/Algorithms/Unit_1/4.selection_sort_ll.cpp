#include <iostream>
#include <vector>
#include <cstdlib> // For std::atoi

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        std::swap(arr[i], arr[minIndex]);
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <list of integers>" << std::endl;
        return 1;
    }

    std::vector<int> numbers;
    for (int i = 1; i < argc; ++i) {
        numbers.push_back(std::atoi(argv[i]));
    }

    std::cout << "Original array: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    selectionSort(numbers);

    std::cout << "Sorted array: ";
    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}