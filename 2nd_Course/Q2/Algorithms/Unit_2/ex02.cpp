/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      UNIT 2                             ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        02/02/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    02/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

#include <iostream>

using namespace std;

class Complejo {
    private:
        double real;
        double imaginario;

    public:
        // Constructor estÃ¡ndar
        Complejo(double r, double i) {
            real = r;
            imaginario = i;
        }

        // Constructor de copia
        Complejo(const Complejo &otro) {
            real = otro.real;
            imaginario = otro.imaginario;
        }

        // MÃ©todo para multiplicar dos nÃºmeros complejos
        Complejo multiplicar(const Complejo &otro) const {
            double nuevoReal = (real * otro.real) - (imaginario * otro.imaginario);
            double nuevoImaginario = (real * otro.imaginario) + (imaginario * otro.real);
            return Complejo(nuevoReal, nuevoImaginario);
        }

        // FunciÃ³n recursiva para calcular la potencia de un nÃºmero complejo
        Complejo potencia(int exponente) const {
            if (exponente == 0) return Complejo(1, 0); // Caso base: cualquier nÃºmero elevado a 0 es 1
            if (exponente == 1) return *this; // Caso base: potencia de 1 es el mismo nÃºmero

            // Divide y vencerÃ¡s: reduce el exponente a la mitad para mejorar la eficiencia
            Complejo mitad = potencia(exponente / 2);
            Complejo resultado = mitad.multiplicar(mitad);

            // Si el exponente es impar, multiplicamos una vez mÃ¡s por el nÃºmero base
            if (exponente % 2 != 0) {
                resultado = resultado.multiplicar(*this);
            }

            return resultado;
        }

        // MÃ©todo para mostrar el nÃºmero complejo
        void mostrar() const {
            cout << real;
            if (imaginario >= 0)
                cout << " + " << imaginario << "i" << endl;
            else
                cout << " - " << -imaginario << "i" << endl;
        }
};

int main() {
    double real, imaginario;
    int exponente;

    // Pedir al usuario que ingrese un nÃºmero complejo
    cout << "Ingrese la parte real del nÃºmero complejo: ";
    cin >> real;
    cout << "Ingrese la parte imaginaria del nÃºmero complejo: ";
    cin >> imaginario;
    cout << "Ingrese el exponente al que desea elevar el nÃºmero complejo: ";
    cin >> exponente;

    // Crear objeto de la clase Complejo
    Complejo num(real, imaginario);

    // Calcular la potencia usando la funciÃ³n recursiva
    Complejo resultado = num.potencia(exponente);

    // Mostrar el resultado
    cout << "El resultado de (" << real << " + " << imaginario << "i)^" << exponente << " es: ";
    resultado.mostrar();

    return 0;

}