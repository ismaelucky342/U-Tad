#include <stdio.h>
#include <string.h>
#include <math.h>

int hexadecimal_a_decimal(char hex[]) {
    int decimal = 0, length = strlen(hex), base = 1;

    // Convertir el número hexadecimal a decimal
    for (int i = length - 1; i >= 0; i--) {
        if (hex[i] >= '0' && hex[i] <= '9') {
            decimal += (hex[i] - 48) * base;
        } else if (hex[i] >= 'a' && hex[i] <= 'f') {
            decimal += (hex[i] - 87) * base;
        } else if (hex[i] >= 'A' && hex[i] <= 'F') {
            decimal += (hex[i] - 55) * base;
        }
        base = base * 16;
    }

    return decimal;
}

int main() {
    char hex[100];
    printf("Ingrese un número hexadecimal: ");
    scanf("%s", hex);
    printf("El número decimal es: %d\n", hexadecimal_a_decimal(hex));
    return 0;
}
