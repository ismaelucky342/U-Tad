#include <stdio.h>

int esMultiploDe3(int numero);

int main()
{
    int contador = 0;
    for (int i = 1; i <= 100; i++)
    {
        if (esMultiploDe3(i))
        {
            printf("%d ", i);
            contador++;
        }
    }
    printf("\nTotal de múltiplos de 3: %d\n", contador);
    return 0;
}

int esMultiploDe3(int numero)
{
    return numero % 3 == 0;
}
