#include "../../includes/polinomio.hpp"
#include <iostream>
#include <vector>
#include <cstdlib> // Para srand y rand
#include <limits>  // Para std::numeric_limits
#include <string>  // Para std::string

void mostrarMenu() {
    std::cout << "=== Menú ===\n";
    std::cout << "1. Introducir coeficientes del polinomio\n";
    std::cout << "q. Salir\n";
    std::cout << "Elige una opción: ";
}

int leerEntero(const std::string& mensaje) {
    int valor;
    while (true) {
        std::cout << mensaje;
        std::cin >> valor;
        if (std::cin.fail() || valor <= 0) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Entrada inválida. Por favor, introduce un número entero positivo.\n";
        } else {
            return valor;
        }
    }
}

float leerFlotante(const std::string& mensaje) {
    float valor;
    while (true) {
        std::cout << mensaje;
        std::cin >> valor;
        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Entrada inválida. Por favor, introduce un número válido.\n";
        } else {
            return valor;
        }
    }
}

int main() {
    std::string opcion;
    do {
        mostrarMenu();
        std::cin >> opcion;

        if (opcion == "q") {
            std::cout << "Saliendo del programa...\n";
            break;
        }

        try {
            int opcionNumerica = std::stoi(opcion);

            switch (opcionNumerica) {
                case 1: {
                    int semilla = leerEntero("Introduce la semilla para el generador de números aleatorios: ");
                    std::srand(semilla);

                    int n = leerEntero("Introduce el grado del polinomio (número de coeficientes): ");
                    std::vector<float> coefs(n);
                    for (int i = 0; i < n; ++i) {
                        coefs[i] = leerFlotante("Introduce el coeficiente " + std::to_string(i + 1) + ": ");
                    }

                    Polinomio polinomio(n - 1, coefs.data());
                    Polinomio::SolucionParcial inicial(0.0f);
                    polinomio.obtenerRaizRecursivo(inicial);

                    break;
                }
                default:
                    std::cout << "Opción inválida. Por favor, elige una opción válida.\n";
                    break;
            }
        } catch (const std::invalid_argument&) {
            std::cout << "Opción inválida. Por favor, elige una opción válida.\n";
        }
    } while (true);

    return 0;
}