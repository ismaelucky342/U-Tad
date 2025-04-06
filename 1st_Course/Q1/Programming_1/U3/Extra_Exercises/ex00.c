#include <stdio.h>

int esPar(int numero);

int main()
{
    int suma = 0;
    for (int i = 1; i <= 100; i++)
    {
        if (esPar(i))
        {
            suma += i;
        }
    }
    printf("Suma de números pares del 1 al 100: %d\n", suma);
    return 0;
}

int esPar(int numero)
{
    return numero % 2 == 0;
}
