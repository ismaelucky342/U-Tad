#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int contarCaracteres(const char *cadena);
int contarPalabras(const char *cadena); 
void reemplazarVocales(char *cadena);

int main()
{
    char string[256]; // asumiendo una longitud máxima de entrada de 255 caracteres
    printf("Insert string: \n");
    scanf("%255[^\n]", string); // Lee la línea completa incluyendo espacios

    int resultCC = contarCaracteres(string); 
    int resultCP = contarPalabras(string);
    reemplazarVocales(string);

    printf("The number of characters is: %d\n", resultCC); 
    printf("The number of words is: %d\n", resultCP); 
    printf("The new string is: %s\n", string);
    
    return 0; 
}

int contarCaracteres(const char *cadena) {
    int contador = 0;
    while (*cadena != '\0') {
        contador++;
        cadena++;
    }
    return contador;
}

int contarPalabras(const char *cadena) {
    int contador = 0;
    bool dentroPalabra = false;

    while (*cadena != '\0') {
        if (*cadena == ' ' || *cadena == '\t' || *cadena == '\n') {
            dentroPalabra = false;
        } else if (!dentroPalabra) {
            dentroPalabra = true;
            contador++;
        }
        cadena++;
    }
    return contador;
}

void reemplazarVocales(char *cadena) {
    while (*cadena != '\0') {
        switch (*cadena) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                *cadena = '*';
                break;
        }
        cadena++;
    }
}
