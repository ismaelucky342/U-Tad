/*
 * Apuntes rápidos sobre Listas Doblemente Enlazadas en C++
 * --------------------------------------------------------
 * En C++ se usa std::list para representar listas **doblemente enlazadas**.
 *
 * Características:
 *  - Inserciones y eliminaciones en cualquier parte: O(1)
 *  - Acceso secuencial, NO aleatorio (no hay operator[])
 *  - Soporta iteradores bidireccionales
 *
 * Operaciones comunes:
 *  - push_back(val), push_front(val)
 *  - pop_back(), pop_front()
 *  - insert(), erase()
 *  - sort(), reverse(), remove(val), unique()
 */         

#include <iostream>
#include <list>


int main() {

    // Declarar lista de enteros
    std::list<int> nums;

    // Agregar elementos al final y al principio
    nums.push_back(10);
    nums.push_back(20);
    nums.push_front(5);

    // Mostrar la lista
    std::cout << "Contenido de la lista:\n";
    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << "\n";

    // Eliminar primero y último elemento
    nums.pop_front();
    nums.pop_back();

    std::cout << "Después de pop_front y pop_back:\n";
    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << "\n";

    // Insertar en el medio con iterador
    auto it = nums.begin(); // apunta al primer elemento
    nums.insert(it, 99);    // inserta antes del primero

    // Insertar múltiples elementos
    nums.insert(nums.end(), {7, 7, 7});

    // Eliminar por valor (todas las ocurrencias)
    nums.remove(7);

    // Agregar duplicados y luego hacer única
    nums.push_back(50);
    nums.push_back(50);
    nums.unique();  // elimina duplicados consecutivos

    // Ordenar y revertir
    nums.push_back(3);
    nums.push_back(1);
    nums.sort();     // orden ascendente
    nums.reverse();  // orden descendente

    std::cout << "Final:\n";
    for (int n : nums) {
        std::cout << n << " ";
    }
    std::cout << "\n";

    return 0;
}
