#include <iostream>
#include <vector>
#include <algorithm>
#include <execution> // For parallel execution policies

int main() {
    // Example data
    std::vector<int> data = {42, 23, 17, 13, 8, 99, 65, 4, 1, 0};

    // Print original data
    std::cout << "Original data: ";
    for (const auto& num : data) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Parallel sort using std::execution::par
    std::sort(std::execution::par, data.begin(), data.end());

    // Print sorted data
    std::cout << "Sorted data: ";
    for (const auto& num : data) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}