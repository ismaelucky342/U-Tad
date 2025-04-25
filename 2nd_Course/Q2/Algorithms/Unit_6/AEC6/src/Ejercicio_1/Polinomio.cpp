#include "../../includes/polinomio.hpp"

SolucionParcial::SolucionParcial(float x_val)
{
    x = x_val;
    y = 0;
}

void SolucionParcial::imprimir() const
{
    std::cout << CYAN << "Seleccionada\n(" << x << "," << y << ")\n"
              << RESET;
}

Polinomio::Polinomio(int g, const float *coefs)
{
    if (g < 0 || coefs == nullptr)
    {
        std::cerr << RED << "Error: grado inválido o coeficientes nulos\n"
                  << RESET;
        grado = 0;
        coeficientes = new float[1]{0};
        return;
    }

    grado = g;
    coeficientes = new float[grado + 1];
    for (int i = 0; i <= grado; ++i)
        coeficientes[i] = coefs[i];
}

Polinomio::~Polinomio()
{
    delete[] coeficientes;
}

float Polinomio::evaluar(float x) const
{
    float resultado = 0;
    for (int i = 0; i <= grado; ++i)
        resultado += coeficientes[i] * pow(x, i);
    return resultado;
}

float Polinomio::obtenerRaizRecursivo(const SolucionParcial &padre, std::mt19937 &gen)
{
    SolucionParcial mejor = padre;
    mejor.y = evaluar(mejor.x);
    mejor.imprimir();

    std::cout << "Mutaciones\n";

    std::vector<SolucionParcial> hijos;
    std::uniform_real_distribution<float> dist(-1.0f, 1.0f); // Distribución uniforme entre -1 y 1
    for (int i = 0; i < 10; ++i)
    {
        float mut = dist(gen); // Genera un número aleatorio entre -1 y 1
        float nuevoX = padre.x + mut;
        float nuevoY = evaluar(nuevoX);
        hijos.emplace_back(nuevoX);
        hijos.back().y = nuevoY;
        std::cout << "(" << nuevoX << "," << nuevoY << ")\n";
    }

    for (const auto &hijo : hijos)
    {
        if (std::abs(hijo.y) < std::abs(mejor.y))
            return obtenerRaizRecursivo(hijo, gen);
    }

    std::cout << GREEN << "Iteracion final Raiz " << mejor.x << RESET << "\n";
    return mejor.x;
}
