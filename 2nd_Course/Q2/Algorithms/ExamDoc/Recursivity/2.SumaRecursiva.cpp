#include <iostream>

int sumaRecursiva(int arr[], int n) {
    if (n == 0) return 0; // Caso base: suma de 0 elementos es 0
    return arr[n - 1] + sumaRecursiva(arr, n - 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Suma de elementos: " << sumaRecursiva(arr, size) << "\n";
    return 0;
}
