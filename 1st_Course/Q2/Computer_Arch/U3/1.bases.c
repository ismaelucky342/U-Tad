#include <stdio.h>

void decimal_a_binario(int num) {
    int binario[32];  // Arreglo para almacenar los bits binarios
    int i = 0;

    // Convertir el número a binario
    while (num > 0) {
        binario[i] = num % 2;
        num = num / 2;
        i++;
    }

    // Mostrar el número binario en orden inverso
    printf("Número binario: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binario[j]);
    }
    printf("\n");
}

int main() {
    int num;
    printf("Ingrese un número decimal: ");
    scanf("%d", &num);
    decimal_a_binario(num);
    return 0;
}
