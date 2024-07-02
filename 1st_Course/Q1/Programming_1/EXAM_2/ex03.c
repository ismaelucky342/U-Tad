/*EJERCICIO 1
Se pide implementar un programa que pida una frase al usuario por consola,
escrita en una sola línea, y que calcule una serie de estadísticas sobre la misma,
y algunas modificaciones. Las condiciones de la frase de entrada son las
siguientes:
 Máximo tamaño de 200 caracteres.
 Solo se podrán utilizar letras minúsculas y espacios
Se pide implementar un programa que calcule las siguientes estadísticas:
 Pedir al usuario que introduzca la frase haciendo todas las
comprobaciones que estime oportunas.
 Cálculo de número total de caracteres (incluyendo los espacios en blanco)
que tiene la frase, número de vocales y consonantes que hay en la frase.
Mostrarlo al usuario
 Cálculo de número de palabras que hay en la frase. Mostrarlo al usuario
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 200

int main()
{
}

int is_valid(char c)


int str_len(char *str)
{
    int aux = 0;
    while (str[aux] != '\0')
    {
        aux++;
    }
    return aux;
}

int wordcount(char *str)
{

}