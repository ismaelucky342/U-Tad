#include <stdio.h>

void decimal_a_complemento_a_dos(int num) {
    unsigned int nbits = 8;  // Usamos 8 bits (un byte)
    unsigned int mask = 1;

    // Verificamos si el número es negativo
    if (num < 0) {
        // Calculamos el complemento a dos para números negativos
        unsigned int complemento = (unsigned int)(~num + 1);

        printf("Complemento a dos: ");
        for (int i = nbits - 1; i >= 0; i--) {
            printf("%d", (complemento >> i) & mask);
        }
        printf("\n");
    } else {
        // Para números positivos mostramos el binario directamente
        printf("Binario positivo: ");
        for (int i = nbits - 1; i >= 0; i--) {
            printf("%d", (num >> i) & mask);
        }
        printf("\n");
    }
}

int main() {
    int num;
    printf("Ingrese un número decimal (8 bits): ");
    scanf("%d", &num);
    decimal_a_complemento_a_dos(num);
    return 0;
}
