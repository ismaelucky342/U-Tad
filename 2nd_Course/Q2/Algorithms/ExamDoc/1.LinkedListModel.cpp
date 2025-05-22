#include <iostream>
#include <list>

int main() {
    std::list<int> nums;
    int x;

    std::cout << "Introduce números (-1 para terminar):\n";
    while (std::cin >> x && x != -1) {
        nums.push_back(x);
    }

    // Eliminar pares
    for (auto it = nums.begin(); it != nums.end(); ) {
        if (*it % 2 == 0) {
            it = nums.erase(it);
        } else {
            ++it;
        }
    }

    // Ordenar lista
    nums.sort();

    // Eliminar duplicados consecutivos
    nums.unique();

    // Mostrar resultado
    std::cout << "Lista resultante:\n";
    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << "\n";

    return 0;
}
