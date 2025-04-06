#include <stdio.h>

int esPalindromo(int numero);

int main()
{
    int num = 12321;
    if (esPalindromo(num))
        printf("%d es un palíndromo\n", num);
    else
        printf("%d no es un palíndromo\n", num);
    return 0;
}

int esPalindromo(int numero)
{
    int original = numero, invertido = 0;
    while (numero != 0)
    {
        invertido = invertido * 10 + numero % 10;
        numero /= 10;
    }
    return original == invertido;
}
