#include "../../includes/polinomio.hpp"

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << RED << "Uso: " << argv[0] << " <semilla> <grado> <coef_0> ... <coef_n>\n" << RESET;
        return 1;
    }

    int semilla = std::atoi(argv[1]);
    int grado = std::atoi(argv[2]);

    if (argc != 3 + grado + 1) {
        std::cerr << RED << "Error: número de coeficientes incorrecto (esperado: " << grado + 1 << ")\n" << RESET;
        return 1;
    }

    float* coeficientes = new float[grado + 1];
    for (int i = 0; i <= grado; ++i)
        coeficientes[i] = std::atof(argv[3 + i]);

    Polinomio p(grado, coeficientes);
    delete[] coeficientes;

    std::mt19937 gen(semilla);
    SolucionParcial inicial(0.0f);
    p.obtenerRaizRecursivo(inicial, gen);

    return 0;
}
