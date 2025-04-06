#include <stdio.h>
#include <math.h>

int binario_a_complemento_a_dos(int binario) {
    int decimal = 0, i = 0;

    // Verificar si el número es negativo
    if (binario < 0) {
        binario = ~binario + 1; // Convierte el complemento a dos a decimal
        return -binario;
    }

    while (binario != 0) {
        decimal += (binario % 10) * pow(2, i);
        binario = binario / 10;
        i++;
    }

    return decimal;
}

int main() {
    int binario;
    printf("Ingrese un número binario en complemento a dos: ");
    scanf("%d", &binario);
    printf("El número decimal es: %d\n", binario_a_complemento_a_dos(binario));
    return 0;
}
