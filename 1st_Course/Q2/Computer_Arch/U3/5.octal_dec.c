#include <stdio.h>
#include <math.h>

int octal_a_decimal(int num) {
    int decimal = 0, i = 0, remainder;

    // Convertir el número octal a decimal
    while (num != 0) {
        remainder = num % 10;
        decimal += remainder * pow(8, i);
        num = num / 10;
        i++;
    }

    return decimal;
}

int main() {
    int num;
    printf("Ingrese un número octal: ");
    scanf("%d", &num);
    printf("El número decimal es: %d\n", octal_a_decimal(num));
    return 0;
}
