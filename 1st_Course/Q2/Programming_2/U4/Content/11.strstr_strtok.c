#include <stdio.h>
#include <string.h>

int main() {
    // Using strstr
    char str[] = "This is a sample string";
    char *ptr;

    ptr = strstr(str, "sample"); // Find the first occurrence of "sample" in str
    if (ptr != NULL) {
        printf("Substring 'sample' found at position: %ld\n", ptr - str);
    } else {
        printf("Substring 'sample' not found in the string.\n");
    }

    // Using strtok
    char sentence[] = "The quick brown fox jumps over the lazy dog";
    char *token;

    // Tokenize the sentence based on space delimiter
    token = strtok(sentence, " ");
    while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok(NULL, " "); // NULL parameter to continue tokenizing from previous position
    }

    return 0;
}
