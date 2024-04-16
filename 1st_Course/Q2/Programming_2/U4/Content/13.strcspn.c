#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world!";
    char charset[] = "aeiou"; // Set of vowels

    // Using strcspn to find the length of the initial segment of str without any vowels
    int length = strcspn(str, charset);

    printf("Length of initial segment without vowels: %d\n", length);

    return 0;
}

