#include "calculadora.h"
#include "protocolo.h"
#include <sys/socket.h>
#include <vector>
#include <iostream>
#include <cstring>

int CalculadoraRemota::suma(int a, int b) {
    // 1. Empaquetar ID, a, b
    
    // 2. Enviar
    
    // 3. Recibir ACK y Resultado
    return 0;
}

int CalculadoraRemota::resta(int a, int b) {
    // Similar a suma
    return 0;
}

int CalculadoraRemota::sumaVectorial(std::vector<int> numeros) {
    // 1. Preparar paquete
    // OJO: Hay que enviar el TAMAÑO del vector primero, luego los datos
    
    // 2. Enviar (ID + Size + Datos...)
    
    // 3. Recibir resultado
    return 0;
}
