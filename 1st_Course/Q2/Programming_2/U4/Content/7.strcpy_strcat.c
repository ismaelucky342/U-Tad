#include <stdio.h>
#include <string.h>

int main() {
    // Using strcpy
    char source[] = "Hello, ";
    char destination[20]; // Make sure the destination buffer is large enough

    strcpy(destination, source); // Copy the content of source to destination
    printf("After strcpy, destination: %s\n", destination);

    // Using strcat
    char str1[] = "world";
    char str2[20] = "Hello, ";

    strcat(str2, str1); // Append the content of str1 to str2
    printf("After strcat, str2: %s\n", str2);

    return 0;
}
