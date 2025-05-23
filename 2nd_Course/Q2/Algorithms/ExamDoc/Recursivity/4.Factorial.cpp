#include <iostream>

int factorial(int n) {
    if (n <= 1) return 1;  // Caso base
    return n * factorial(n - 1);  // Paso recursivo
}

int main() {
    int num = 5;
    std::cout << "Factorial de " << num << " es " << factorial(num) << "\n";
    return 0;
}
