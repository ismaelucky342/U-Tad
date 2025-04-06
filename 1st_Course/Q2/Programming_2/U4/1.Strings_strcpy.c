#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Static initialization
    char string1[] = "Hello World";

    // Dynamic initialization using malloc
    char *string2 = malloc(12 * sizeof(char)); // Ensure to allocate enough memory.
    strcpy(string2, "Hello World");

    // Initialization by assigning characters
    char string3[12];
    string3[0] = 'H';
    string3[1] = 'e';
    string3[2] = 'l';
    string3[3] = 'l';
    string3[4] = 'o';
    string3[5] = ' ';
    string3[6] = 'W';
    string3[7] = 'o';
    string3[8] = 'r';
    string3[9] = 'l';
    string3[10] = 'd';
    string3[11] = '\0'; // The null character indicating the end of the string.

    // Initialization using strcpy
    char string4[12];
    strcpy(string4, "Hello World");

    // Print the initialized strings
    printf("cadena1: %s\n", string1);
    printf("cadena2: %s\n", string2);
    printf("cadena3: %s\n", string3);
    printf("cadena4: %s\n", string4);

    // Free dynamically allocated memory
    free(string2);

    return 0;
}
