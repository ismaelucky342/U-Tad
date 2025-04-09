#include <iostream>
#include <vector>

int main() {
    // Example: Contiguous list using std::vector
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::cout << "Vector elements: ";
    for (int val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
