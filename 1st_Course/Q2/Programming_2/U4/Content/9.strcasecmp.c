#include <stdio.h>
#include <string.h>

int main() {
    // Using strcasecmp
    char str1[] = "hello";
    char str2[] = "HELLO";
    char str3[] = "world";

    int result1 = strcasecmp(str1, str2); // Compare str1 and str2
    if (result1 == 0) {
        printf("str1 and str2 are equal (case-insensitive)\n");
    } else {
        printf("str1 and str2 are not equal (case-insensitive)\n");
    }

    int result2 = strcasecmp(str1, str3); // Compare str1 and str3
    if (result2 == 0) {
        printf("str1 and str3 are equal (case-insensitive)\n");
    } else {
        printf("str1 and str3 are not equal (case-insensitive)\n");
    }

    return 0;
}
