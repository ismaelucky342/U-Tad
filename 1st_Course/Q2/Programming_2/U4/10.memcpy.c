#include <stdio.h>
#include <string.h>

int main() {
    // Source string
    char source[] = "Hello, world!";
    int source_length = strlen(source) + 1; // Include the null terminator

    // Destination string
    char destination[20]; // Make sure the destination buffer is large enough

    // Using memcpy to copy source to destination
    memcpy(destination, source, source_length);

    // Print the copied string
    printf("Copied string: %s\n", destination);

    return 0;
}
