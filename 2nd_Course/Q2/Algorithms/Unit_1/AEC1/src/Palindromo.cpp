/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC1 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
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
#include <string>
#include <stdexcept> // Manejo de escepciones

using namespace std;

/**
 * @brief Verificamos si una cadena de caracteres es un palíndromo.
 *
 * @param str Cadena de caracteres (máx. 20 caracteres).
 * @return bool Retorna `true` si la cadena es un palíndromo, `false` en caso contrario.
 *
 * @throws invalid_argument si la longitud de la cadena es mayor a 20.
 *
 * Complejidad temporal: O(n), donde n es la longitud de la cadena (comparación de extremos).
 * Complejidad espacial: O(1), ya que no usa estructuras adicionales.
 */
bool esPalindromo(const string &str)
{
    if (str.length() > 20)
    {
        throw invalid_argument("La cadena no debe superar los 20 caracteres.");
    }

    int inicio = 0, fin = str.length() - 1;
    while (inicio < fin)
    {
        if (str[inicio] != str[fin])
        {
            return false;
        }
        inicio++;
        fin--;
    }
    return true;
}

/**
 * @brief Función principal del programa que recibe argumentos desde la línea de comandos.
 *
 * @param argc Cantidad de argumentos pasados al programa.
 * @param argv Arreglo de cadenas que contienen los argumentos.
 * @return int Código de salida del programa (0 = éxito, 1 = error).
 *
 * @details
 * - El programa espera que el usuario pase una palabra como argumento.
 * - Si no hay argumentos suficientes o hay más de uno, se muestra un mensaje de error.
 * - Se llama a la función `esPalindromo` y se imprime `1` si la palabra es un palíndromo, `0` si no lo es.
 */
int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        cerr << "Uso: " << argv[0] << " <palabra>" << endl;
        return 1;
    }

    string palabra = argv[1];
    try
    {
        bool resultado = esPalindromo(palabra);

        if (resultado)
        {
            cout << "1" << endl;
        }
        else
        {
            cout << "0" << endl;
        }
    }
    catch (const invalid_argument &e)
    {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }

    return 0;
}