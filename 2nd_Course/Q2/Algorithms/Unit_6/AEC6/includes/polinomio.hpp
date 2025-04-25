/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC6 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        02/04/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    17/04/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

#ifndef POLINOMIO_H
#define POLINOMIO_H

/*=================================DEFINES======================================*/

#include <iostream>
#include <random>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <cmath>

/*=================================COLORS======================================*/

#define RED     "\033[0;31m"
#define RESET   "\033[0m"
#define GREEN   "\033[0;32m"
#define CYAN    "\033[0;36m"

/*=================================CLASS=====================================*/

class SolucionParcial {
public:
    float x;
    float y;

    SolucionParcial(float x_val = 0);
    void imprimir() const;
};

class Polinomio {
private:
    int grado;
    float* coeficientes;

public:
    Polinomio(int grado, const float* coefs);
    ~Polinomio();

    float evaluar(float x) const;
    float obtenerRaizRecursivo(const SolucionParcial& padre, std::mt19937& gen);
};

#endif
