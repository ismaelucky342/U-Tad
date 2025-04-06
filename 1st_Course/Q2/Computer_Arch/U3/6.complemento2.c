#include <stdio.h>

void decimal_a_complemento_a_dos(int num) {
    unsigned int mask = 1;
    int nbits = sizeof(num) * 8;  // Tamaño del entero en bits (32 bits por un int de 4 bytes)

    printf("Complemento a dos de %d: ", num);

    if (num < 0) {
        // Si el número es negativo, mostramos el complemento a dos
        unsigned int complemento = (unsigned int)(~num + 1);
        for (int i = nbits - 1; i >= 0; i--) {
            // Mostrar los bits
            printf("%d", (complemento >> i) & mask);
        }
        printf("\n");
    } else {
        // Si es positivo, mostramos el número en binario
        for (int i = nbits - 1; i >= 0; i--) {
            printf("%d", (num >> i) & mask);
        }
        printf("\n");
    }
}

int main() {
    int num;
    printf("Ingrese un número decimal
