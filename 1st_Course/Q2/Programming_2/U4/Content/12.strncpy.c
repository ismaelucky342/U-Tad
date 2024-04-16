#include <stdio.h>
#include <string.h>

int main() {
    // Source string
    char source[] = "Hello, world!";
    int source_length = strlen(source) + 1; // Include the null terminator

    // Destination string
    char destination[20]; // Make sure the destination buffer is large enough

    // Using strncpy to copy source to destination
    strncpy(destination, source, sizeof(destination) - 1); // Ensure space for null terminator
    destination[sizeof(destination) - 1] = '\0'; // Null terminate the string manually

    // Print the copied string
    printf("Copied string: %s\n", destination);

    return 0;
}
