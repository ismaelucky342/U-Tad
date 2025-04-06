#include <stdio.h>

void tablaMultiplicar(int numero);

int main()
{
    int numero = 7;
    tablaMultiplicar(numero);
    return 0;
}

void tablaMultiplicar(int numero)
{
    for (int i = 1; i <= 10; i++)
    {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }
}
