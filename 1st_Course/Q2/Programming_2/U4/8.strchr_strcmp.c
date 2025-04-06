#include <stdio.h>
#include <string.h>

int main() {
    // Using strchr
    char str[] = "Hello, world!";
    char *ptr;

    ptr = strchr(str, 'o'); // Find the first occurrence of 'o' in str
    if (ptr != NULL) {
        printf("First occurrence of 'o' found at position: %ld\n", ptr - str);
    } else {
        printf("Character 'o' not found in the string.\n");
    }

    // Using strcmp
    char str1[] = "Hello";
    char str2[] = "Hello";
    char str3[] = "World";

    int result1 = strcmp(str1, str2); // Compare str1 and str2
    if (result1 == 0) {
        printf("str1 and str2 are equal\n");
    } else {
        printf("str1 and str2 are not equal\n");
    }

    int result2 = strcmp(str1, str3); // Compare str1 and str3
    if (result2 == 0) {
        printf("str1 and str3 are equal\n");
    } else {
        printf("str1 and str3 are not equal\n");
    }

    return 0;
}
