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

/*Desarrolla una función recursiva que encuentre la suma de los primeros n números naturales. Recuerda que la suma de los primeros n números naturales se puede expresar como 1+2+3+...+n.*/

#include <iostream>

int sumaNaturales(int n) {
    if (n <= 1) {
        return n;
    } else {
        return n + sumaNaturales(n - 1);
    }
}

int main() {
    int n;
    std::cout << "Introduce un número: ";
    std::cin >> n;
    std::cout << "La suma de los primeros " << n << " números naturales es: " << sumaNaturales(n) << std::endl;
    return 0;
}