#include <stdio.h>

int sumaDigitos(int numero);

int main()
{
    int numero = 12345;
    int suma = sumaDigitos(numero);
    printf("Suma de los dígitos de %d: %d\n", numero, suma);
    return 0;
}

int sumaDigitos(int numero)
{
    int suma = 0;
    while (numero != 0)
    {
        suma += numero % 10;
        numero /= 10;
    }
    return suma;
}
