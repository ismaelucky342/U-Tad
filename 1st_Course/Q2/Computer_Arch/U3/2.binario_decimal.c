#include <stdio.h>
#include <math.h>

int binario_a_decimal(int num) {
    int decimal = 0, i = 0, bit;

    // Convertir el número binario a decimal
    while (num != 0) {
        bit = num % 10;  // Obtiene el último bit
        decimal += bit * pow(2, i);  // Suma al total
        num = num / 10;  // Elimina el último bit
        i++;
    }

    return decimal;
}

int main() {
    int num;
    printf("Ingrese un número binario: ");
    scanf("%d", &num);
    printf("El número decimal es: %d\n", binario_a_decimal(num));
    return 0;
}
