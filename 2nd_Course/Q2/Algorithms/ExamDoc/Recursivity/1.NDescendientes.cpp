#include <iostream>

void imprimirDescendente(int n) {
    if (n <= 0) return;  // Caso base
    std::cout << n << " ";
    imprimirDescendente(n - 1);  // Llamada recursiva
}

int main() {
    int num = 10;
    imprimirDescendente(num);
    std::cout << "\n";
    return 0;
}
