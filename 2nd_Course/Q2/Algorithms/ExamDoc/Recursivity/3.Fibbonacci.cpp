#include <iostream>

int fibonacci(int n) {
    if (n <= 1) return n;  // Caso base para 0 y 1
    return fibonacci(n - 1) + fibonacci(n - 2);  // Paso recursivo
}

int main() {
    int num = 10;
    std::cout << "Fibonacci en la posición " << num << " es " << fibonacci(num) << "\n";
    return 0;
}
