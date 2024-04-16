#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    // Using getchar
    printf("Enter a character (getchar): ");
    char ch = getchar(); // Reads a single character from standard input (stdin)
    getchar(); // Consume the newline character left in the input buffer
    printf("Character entered: %c\n", ch);

    // Using putchar
    printf("Character entered (putchar): ");
    putchar(ch); // Prints the character to the standard output (stdout)
    putchar('\n'); // Prints a newline character

    // Using gets (deprecated, use with caution)
    char str1[20];
    printf("Enter a string (gets): ");
    gets(str1); // Reads a string from the user (deprecated, avoid using in real code)
    printf("String entered (gets): %s\n", str1);

    // Using fgets
    char str2[20];
    printf("Enter another string (fgets): ");
    fgets(str2, sizeof(str2), stdin); // Reads a string from the user with a specified maximum length
    if (strlen(str2) > 0 && str2[strlen(str2) - 1] == '\n') {
        str2[strlen(str2) - 1] = '\0'; // Remove the newline character from the input buffer
    }
    printf("String entered (fgets): %s\n", str2);

    // Using printf and scanf
    int num;
    printf("Enter a number (scanf): ");
    scanf("%d", &num); // Reads an integer from the user
    printf("Number entered (printf): %d\n", num);

    // Using malloc and free
    int *ptr;
    ptr = (int *)malloc(5 * sizeof(int)); // Allocate memory dynamically
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    printf("Memory allocated dynamically (malloc)\n");
    free(ptr); // Free dynamically allocated memory

    return 0;
}
