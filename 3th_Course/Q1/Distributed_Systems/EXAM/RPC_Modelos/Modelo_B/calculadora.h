#ifndef CALCULADORA_H
#define CALCULADORA_H

#include <vector>

// Interfaz Base
class Calculadora {
public:
    virtual int suma(int a, int b) { return 0; }
    virtual int resta(int a, int b) { return 0; }
    // Nuevo reto: Enviar un array/vector dinámico
    virtual int sumaVectorial(std::vector<int> numeros) { return 0; }
    virtual ~Calculadora() {}
};

// Clase Proxy
class CalculadoraRemota : public Calculadora {
private:
    int serverSocket;
public:
    CalculadoraRemota(int socket) : serverSocket(socket) {}
    int suma(int a, int b) override;
    int resta(int a, int b) override;
    int sumaVectorial(std::vector<int> numeros) override;
};

#endif
