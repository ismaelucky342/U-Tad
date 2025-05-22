/*
Implementar la función obtenerMedia utilizando el enfoque de divide y vencerás.

Enfoque:
La idea es dividir el array en dos mitades, calcular recursivamente la media de cada mitad, y luego combinar ambas usando la fórmula:

media_total = (L * m_L + R * m_R) / (L + R)

donde:
- L y R son los tamaños de las mitades izquierda y derecha
- m_L y m_R son las medias de las mitades izquierda y derecha
*/

#include <iostream>



// Función recursiva principal
float obtenerMedia(float *valores, int n) 
{
    if (n == 1) {
        return valores[0];  // Caso base: un solo elemento
    }

    int mitad = n / 2;

    // Dividir el array en dos partes
    float mediaIzq = obtenerMedia(valores, mitad);
    float mediaDer = obtenerMedia(valores + mitad, n - mitad);

    // Combinar los resultados
    return ((mitad * mediaIzq) + ((n - mitad) * mediaDer)) / n;
}

// Función de prueba
int main() {
    float v[] = {1.2, 2.0, -1.0, 0.0, 2.8, -0.5, 3.2};
    int n = sizeof(v) / sizeof(float);

    std::cout << "Media: " << obtenerMedia(v, n) << std::endl;  // Debería imprimir 1.1

    return 0;
}
