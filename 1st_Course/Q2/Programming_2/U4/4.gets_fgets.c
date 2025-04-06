#include <stdio.h>
#include <string.h>

int main() {
    char str1[20];
    char str2[20];

    // Using gets
    printf("Enter a string (gets): ");
    gets(str1); // Read a string from the user (deprecated, avoid using in real code)
    printf("String entered using gets: %s\n", str1);

    // Using fgets
    printf("Enter another string (fgets): ");
    fgets(str2, sizeof(str2), stdin); // Read a string from the user with a specified maximum length
    // Remove the newline character from the input buffer
    if (strlen(str2) > 0 && str2[strlen(str2) - 1] == '\n') {
        str2[strlen(str2) - 1] = '\0';
    }
    printf("String entered using fgets: %s\n", str2);

    return 0;
}
