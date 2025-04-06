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
#include <string.h>
#include <ctype.h>

int contar_vocales(const char *frase);
int contar_consonantes(const char *frase);
int contar_palabras(const char *frase);

int main()
{
    char    frase[201];

    printf("Introduce una frase (solo letras minúsculas y espacios, máximo 200 caracteres): ");
    fgets(frase, sizeof(frase), stdin);

    // Eliminar el salto de línea al final si está presente
    size_t len = strlen(frase);
    if (len > 0 && frase[len - 1] == '\n')
    {
        frase[len - 1] = '\0';
    }

    // Validar la frase
    int valida = 1;
    for (int i = 0; frase[i] != '\0'; i++)
    {
        if (!(islower(frase[i]) || frase[i] == ' '))
        {
            valida = 0;
            break;
        }
    }

    if (!valida)
    {
        printf("La frase contiene caracteres inválidos.\n");
        return 1;
    }

    // Calcular estadísticas
    int num_caracteres = strlen(frase);
    int num_vocales = contar_vocales(frase);
    int num_consonantes = contar_consonantes(frase);
    int num_palabras = contar_palabras(frase);

    // Mostrar resultados
    printf("Número total de caracteres: %d\n", num_caracteres);
    printf("Número de vocales: %d\n", num_vocales);
    printf("Número de consonantes: %d\n", num_consonantes);
    printf("Número de palabras: %d\n", num_palabras);

    return 0;
}

int contar_vocales(const char *frase)
{
    int vocales = 0;
    for (int i = 0; frase[i] != '\0'; i++)
    {
        char c = frase[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
        {
            vocales++;
        }
    }
    return vocales;
}

// Función para contar consonantes
int contar_consonantes(const char *frase)
{
    int consonantes = 0;
    for (int i = 0; frase[i] != '\0'; i++)
    {
        char c = frase[i];
        if (isalpha(c) && !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'))
        {
            consonantes++;
        }
    }
    return consonantes;
}

// Función para contar palabras
int contar_palabras(const char *frase)
{
    int palabras = 0;
    int inWord = 0; // Variable para verificar si estamos dentro de una palabra

    for (int i = 0; frase[i] != '\0'; i++)
    {
        if (isalpha(frase[i]))
        {
            if (!inWord)
            {
                palabras++;
                inWord = 1; // Estamos dentro de una palabra
            }
        }
        else
        {
            inWord = 0; // Hemos salido de una palabra
        }
    }
    return palabras;
}