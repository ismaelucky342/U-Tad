/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC1 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        01/02/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    02/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

#include <iostream>
#include <stdexcept> // Para manejar excepciones

using namespace std;

/**
 * @brief Calcula la suma de los primeros N números naturales.
 *
 * @param n Número entero positivo.
 * @return int Suma de los números desde 1 hasta n.
 *
 * @throws invalid_argument si n es menor o igual a 0.
 *
 * Complejidad temporal: O(1) (uso de la fórmula matemática de suma).
 * Complejidad espacial: O(1) (uso de una única variable).
 */
int sumarPrimerosNumeros(int n)
{
    if (n <= 0)
    {
        throw invalid_argument("El número debe ser un entero positivo.");
    }
    return (n * (n + 1)) / 2;
}

/**
 * @brief Función principal que recibe un número entero desde la línea de comandos y calcula la suma de los primeros N números.
 *
 * @param argc Cantidad de argumentos pasados al programa.
 * @param argv Arreglo de cadenas que contienen los argumentos.
 * @return int Código de salida del programa (0 = éxito, 1 = error).
 *
 * @details
 * - Se usa argv y argc en vez de cin para recibir argumentos desde la línea de comandos. (mas capacidad de manejo de errores)
 * - Se utiliza la función `stoi` para convertir una cadena a un número entero. Si la conversión falla, se lanza una excepción.
 * - El programa espera que el usuario pase un número como argumento.
 * - Si no hay argumentos suficientes o el número ingresado no es válido, se muestra un mensaje de error.
 * - La función `sumarPrimerosNumeros` calcula la suma de los primeros N números naturales.
 */
int main(int argc, char *argv[])
{

    int numero;

    if (argc != 2)
    {
        cerr << "Uso: " << argv[0] << " <número entero positivo>" << endl;
        return 1;
    }

    try
    {
        numero = stoi(argv[1]);

        if (numero <= 0)
        {
            throw invalid_argument("El número debe ser positivo.");
        }

        int resultado = sumarPrimerosNumeros(numero);
        cout << "La suma de los primeros " << numero << " números es: " << resultado << endl;
    }
    catch (const invalid_argument &e)
    {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }

    return 0;
}