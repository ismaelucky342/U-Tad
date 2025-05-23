#include <iostream>

void torreDeHanoi(int n, char origen, char destino, char auxiliar) {
    if (n == 1) {
        std::cout << "Mueve disco 1 de " << origen << " a " << destino << "\n";
        return;
    }
    torreDeHanoi(n - 1, origen, auxiliar, destino);
    std::cout << "Mueve disco " << n << " de " << origen << " a " << destino << "\n";
    torreDeHanoi(n - 1, auxiliar, destino, origen);
}

int main() {
    int discos = 3;
    torreDeHanoi(discos, 'A', 'C', 'B');
    return 0;
}
