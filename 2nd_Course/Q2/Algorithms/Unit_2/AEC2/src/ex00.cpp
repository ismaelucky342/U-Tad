/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        01/03/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    15/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

# include "../includes/lib.hpp"

/**
 * Calcula la raíz cuadrada de un número mediante aproximaciones sucesivas.
 *
 * @param numero El número del cual calcular la raíz cuadrada.
 * @param error El valor de error máximo permitido en la aproximación. Se usa dprintf en salida 2 para mostrar errores.
 *
 * @return La raíz cuadrada calculada con la precisión requerida.
 *
 * Complejidad temporal: O(log(n/error)), donde n es el número objetivo y error es la tolerancia.
 * Complejidad espacial: O(1).
 * @details
 * - Se usa argv y argc en vez de cin para recibir argumentos desde la línea de comandos. (mas capacidad de manejo de errores)
 * - Se verifica que el número sea positivo y que el error sea mayor a 0.
 * - usamos atof para convertir los argumentos de la línea de comandos a números de coma flotante.
 * - Se inicializan los valores inferior y superior para la búsqueda binaria.
 * - Se calcula la aproximación de la raíz cuadrada mediante la fórmula (inferior + superior) / 2.
 * - Se compara el cuadrado de la aproximación con el número objetivo.
 * - Si la diferencia es menor que el error, se retorna la aproximación.
 * - Si el cuadrado de la aproximación es mayor que el número, se actualiza el valor de superior.
 */
double raiz_cuadrada(double numero, double error)
{
    double inferior = 0.0;
    double superior = numero;
    double aproximacion;

    if (numero < 0 || error <= 0)
    {
        dprintf(2, RED "ERROR\n" RESET);
        return -1;
    }

    while (1)
    {
        aproximacion = (inferior + superior) / 2.0;

        if (fabs(aproximacion * aproximacion - numero) < error)
            break;
        if (aproximacion * aproximacion > numero)
            superior = aproximacion;
        else
            inferior = aproximacion;
        printf("%.6g\n", aproximacion);
    }

    return aproximacion;
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        dprintf(2, RED "ERROR: Uso: %s <numero> <error>\n" RESET , argv[0]);
        return 1;
    }
    double numero = atof(argv[1]);
    double error = atof(argv[2]);
    if (numero < 0 || error <= 0)
    {
        dprintf(2, RED "ERROR: Los valores de numero y error deben ser positivos.\n" RESET);
        return 1;
    }
    double resultado = raiz_cuadrada(numero, error);
    if (resultado != -1)
        printf(GREEN "La raíz cuadrada de %f con un error de %f es %f\n" RESET, numero, error, resultado);
    return 0;
}
