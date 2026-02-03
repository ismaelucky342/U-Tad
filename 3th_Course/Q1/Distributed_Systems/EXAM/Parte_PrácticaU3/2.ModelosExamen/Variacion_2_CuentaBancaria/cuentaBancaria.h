#pragma once
#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

class CuentaBancaria {

private:
    string titular;
    double saldo;
    string numeroCuenta;
public:

    /**
    * @brief Constructor por defecto
    */
    CuentaBancaria();

    /**
    * @brief Constructor con parámetros, recibe "titular", "saldo" y "numeroCuenta"
    * @param titular
    * @param saldo
    * @param numeroCuenta
    */
    CuentaBancaria(string titular, double saldo, string numeroCuenta);
    
    /**
    * @brief Destructor por defecto
    */
    ~CuentaBancaria();

    /**
    * Getter/Setter para parámetros
    */
    void setTitular(string titular);
    string getTitular();
    void setSaldo(double saldo);
    double getSaldo();
    void setNumeroCuenta(string numeroCuenta);
    string getNumeroCuenta();

    /**
    * Métodos para leer/escribir una cuenta a un archivo de texto
    */
    void escribirAFichero(string nombreFichero);
    void leerDeFichero(string nombreFichero);

    /**
    * Operador para mostrar por terminal los datos de la cuenta formateados
    */
    friend ostream& operator << (ostream& out, const CuentaBancaria& c);
};
