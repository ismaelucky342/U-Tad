/*
 * Apuntes rápidos sobre Tablas Hash en C++
 * ----------------------------------------
 * En C++ las tablas hash se usan principalmente con la clase std::unordered_map.
 * Es un contenedor que asocia claves (keys) a valores (values) con acceso promedio O(1).
 *
 * Operaciones comunes:
 *  - Insertar:   map[key] = value;
 *  - Buscar:     map.find(key) o map[key]
 *  - Borrar:     map.erase(key)
 *  - Comprobar si existe clave: map.count(key) > 0
 *
 * Ventajas:
 *  - Acceso rápido (O(1) promedio)
 *  - No mantiene orden (a diferencia de std::map que es árbol)
 *
 * Uso típico: contar ocurrencias, cache, índices, etc.
 */

#include <iostream>
#include <unordered_map>
#include <string>

int main() {
    // Declarar tabla hash: clave string, valor entero
    std::unordered_map<std::string, int> frequency;

    // Insertar elementos o actualizar el valor
    frequency["apple"] = 3;
    frequency["banana"] = 5;

    // Insertar o incrementar cuenta en forma segura
    frequency["orange"]++;  // si no existe, crea con 0 y suma 1

    // Buscar elemento con find
    auto it = frequency.find("apple");
    if (it != frequency.end()) {
        std::cout << "La frecuencia de apple es: " << it->second << "\n";
    } else {
        std::cout << "apple no está en la tabla\n";
    }

    // Comprobar si existe clave con count
    if (frequency.count("banana") > 0) {
        std::cout << "banana está en la tabla\n";
    }

    // Borrar un elemento
    frequency.erase("banana");

    // Iterar todos los elementos
    std::cout << "Contenido de la tabla:\n";
    for (const auto& pair : frequency) {
        std::cout << pair.first << ": " << pair.second << "\n";
    }

    // Ejemplo de uso: contar frecuencia de caracteres en un string
    std::string text = "hello world";
    std::unordered_map<char, int> charCount;
    for (char c : text) {
        if (c != ' ')  // ignorar espacios
            charCount[c]++;
    }

    std::cout << "Frecuencia de caracteres:\n";
    for (const auto& p : charCount) {
        std::cout << p.first << ": " << p.second << "\n";
    }

    return 0;
}
