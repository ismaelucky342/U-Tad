#include <stdio.h>

int main() {
    char str[] = "Hello";

    // Using putchar to print each character of the string
    printf("Using putchar:\n");
    for (int i = 0; str[i] != '\0'; i++) {
        putchar(str[i]); // Prints each character of the string
    }
    putchar('\n'); // Prints a newline character

    // Using putc to print each character of the string
    printf("Using putc:\n");
    for (int i = 0; str[i] != '\0'; i++) {
        putc(str[i], stdout); // Prints each character of the string to stdout
    }
    putc('\n', stdout); // Prints a newline character to stdout

    return 0;
}
