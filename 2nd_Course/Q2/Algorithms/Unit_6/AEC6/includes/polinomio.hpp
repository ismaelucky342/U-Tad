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

// polinomio.hpp
#ifndef POLINOMIO_HPP
#define POLINOMIO_HPP

#include <vector>
#include <cmath>
#include <random>
#include <iomanip>

class Polinomio {
private:
    int grado;
    float* coeficientes;

public:
    Polinomio(int g, const float* coeffs);
    ~Polinomio();

    float evaluar(float x) const;

    class SolucionParcial {
    public:
        float x;
        float y;

        SolucionParcial(float x_val);
        void calcularY(const Polinomio& polinomio);
        void imprimir() const;
    };

    float obtenerRaizRecursivo(SolucionParcial padre);
};

#endif // POLINOMIO_HPP