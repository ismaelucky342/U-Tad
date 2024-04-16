#include <stdio.h>

int main() {
    char buffer[10]; // Declare a buffer of limited size

    // Using scanf with %s
    printf("Enter a word (scanf with %%s): ");
    scanf("%s", buffer); // The scanf function reads characters until encountering a whitespace or newline
    printf("Word entered: %s\n", buffer); // Prints the entered word

    // Using scanf safely to avoid buffer overrun
    printf("Enter a safe word (scanf with size limit): ");
    scanf("%9s", buffer); // Limit the read to 9 characters to leave space for the null character
    printf("Safe word entered: %s\n", buffer); // Prints the entered word

    return 0;
}
