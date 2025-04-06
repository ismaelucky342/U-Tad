#include <stdio.h>
#include <string.h>

int main()
{
    char cadena1[] = "hello world"; 
    char *cadena2; 

    strcpy(cadena2, cadena1); 
    printf("%s", cadena2);
}

