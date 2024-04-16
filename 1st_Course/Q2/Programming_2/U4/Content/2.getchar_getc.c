#include <stdio.h>

int main() {
    char ch;

    printf("Enter a character:\n");

    // Using getchar()
    printf("Using getchar():\n");
    ch = getchar(); // Reads a single character from standard input (stdin)
    printf("Character entered using getchar(): %c\n", ch);

    // Clear the input buffer
    while (getchar() != '\n');

    // Using getc()
    printf("Enter another character:\n");
    printf("Using getc():\n");
    ch = getc(stdin); // Reads a single character from standard input (stdin)
    printf("Character entered using getc(): %c\n", ch);

    return 0;
}
