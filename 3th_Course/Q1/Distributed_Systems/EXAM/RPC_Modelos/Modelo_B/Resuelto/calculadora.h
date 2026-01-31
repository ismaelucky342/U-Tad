#ifndef CALCULADORA_H
#define CALCULADORA_H

#include <vector>

// Interfaz Base
class Calculadora {
public:
    virtual int suma(int a, int b) { return a + b; }
    virtual int resta(int a, int b) { return a - b; }
    virtual int sumaVectorial(std::vector<int> numeros) { 
        int total = 0;
        for(int n : numeros) total += n;
        return total;
    }
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
