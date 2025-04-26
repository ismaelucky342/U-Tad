// polinomio.cpp
#include "../../includes/polinomio.hpp"
#include <iostream>

Polinomio::Polinomio(int g, const float* coeffs) : grado(g) {
    coeficientes = new float[grado + 1];
    for (int i = 0; i <= grado; ++i) {
        coeficientes[i] = coeffs[i];
    }
}

Polinomio::~Polinomio() {
    delete[] coeficientes;
}

float Polinomio::evaluar(float x) const {
    float resultado = 0.0f;
    for (int i = grado; i >= 0; --i) {
        resultado = resultado * x + coeficientes[i];
    }
    return resultado;
}

Polinomio::SolucionParcial::SolucionParcial(float x_val) : x(x_val) {}

void Polinomio::SolucionParcial::calcularY(const Polinomio& polinomio) {
    y = polinomio.evaluar(x);
}

void Polinomio::SolucionParcial::imprimir() const {
    std::cout << "(" << std::fixed << std::setprecision(6) << x << "," << y << ")" << std::endl;
}

float Polinomio::obtenerRaizRecursivo(SolucionParcial padre) {
    padre.calcularY(*this);
    std::cout << "Seleccionada" << std::endl;
    padre.imprimir();

    std::vector<SolucionParcial> hijos;
    std::normal_distribution<float> distribution(0.0f, 1.0f);
    std::mt19937 generator(static_cast<unsigned int>(std::rand()));

    std::cout << "Mutaciones" << std::endl;
    for (int i = 0; i < 10; ++i) {
        float mutacion = distribution(generator);
        SolucionParcial hijo(padre.x + mutacion);
        hijo.calcularY(*this);
        hijos.push_back(hijo);
        hijo.imprimir();
    }

    SolucionParcial mejor_hijo = hijos[0];
    for (const auto& hijo : hijos) {
        if (std::abs(hijo.y) < std::abs(mejor_hijo.y)) {
            mejor_hijo = hijo;
        }
    }

    if (std::abs(mejor_hijo.y) < std::abs(padre.y)) {
        return obtenerRaizRecursivo(mejor_hijo);
    } else {
        std::cout << "Iteracion final Raiz " << std::fixed << std::setprecision(6) << padre.x << std::endl;
        return padre.x;
    }
}