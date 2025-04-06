#include <stdio.h>

void decimal_a_hexadecimal(int num) {
    char hexadecimal[100];
    int i = 0;

    // Convertir el número decimal a hexadecimal
    while (num != 0) {
        int remainder = num % 16;
        if (remainder < 10) {
            hexadecimal[i] = 48 + remainder;  // Convertir a caracteres '0'-'9'
        } else {
            hexadecimal[i] = 87 + remainder;  // Convertir a caracteres 'a'-'f'
        }
        num = num / 16;
        i++;
    }

    // Mostrar el número hexadecimal en orden inverso
    printf("Número hexadecimal: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%c", hexadecimal[j]);
    }
    printf("\n");
}

int main() {
    int num;
    printf("Ingrese un número decimal: ");
    scanf("%d", &num);
    decimal_a_hexadecimal(num);
    return 0;
}
