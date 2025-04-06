#include <stdio.h>

int esPerfecto(int numero);

int main()
{
    for (int i = 1; i <= 10000; i++)
    {
        if (esPerfecto(i))
        {
            printf("%d es un número perfecto\n", i);
        }
    }
    return 0;
}

int esPerfecto(int numero)
{
    int suma = 0;
    for (int i = 1; i < numero; i++)
    {
        if (numero % i == 0)
        {
            suma += i;
        }
    }
    return suma == numero;
}
