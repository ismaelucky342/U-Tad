#include <iostream>
#include <list>
using namespace std;

// Ejercicio 1: Algoritmo con listas
// Función que recibe dos listas ordenadas y devuelve una lista con la intersección
list<int> interseccionListas(const list<int>& l1, const list<int>& l2) {
    list<int> resultado;
    auto it1 = l1.begin(), it2 = l2.begin();
    while (it1 != l1.end() && it2 != l2.end()) {
        if (*it1 == *it2) {
            resultado.push_back(*it1);
            ++it1; ++it2;
        } else if (*it1 < *it2) {
            ++it1;
        } else {
            ++it2;
        }
    }
    return resultado;
}

// Ejercicio 2: Recursividad
// Función recursiva para calcular la suma de los dígitos de un número
int sumaDigitos(int n) {
    if (n < 10) return n;
    return n % 10 + sumaDigitos(n / 10);
}

int main() {
    // Prueba ejercicio 1
    list<int> l1 = {1, 2, 3, 4, 5};
    list<int> l2 = {3, 4, 5, 6, 7};
    list<int> inter = interseccionListas(l1, l2);
    cout << "Intersección de listas: ";
    for (int x : inter) cout << x << " ";
    cout << endl;

    // Prueba ejercicio 2
    int numero = 12345;
    cout << "Suma de dígitos de " << numero << ": " << sumaDigitos(numero) << endl;

    return 0;
}







