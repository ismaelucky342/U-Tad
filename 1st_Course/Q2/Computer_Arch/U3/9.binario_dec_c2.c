#include <stdio.h>
#include <math.h>

int binario_a_decimal_complemento_a_dos(int num) {
    int i = 0;
    int decimal = 0;
    int signo = 1;

    if (num < 0) {
        num = ~num + 1;  // Si es negativo, convertimos el complemento a dos
        signo = -1;
    }

    while (num != 0) {
        decimal += (num % 10) * pow(2, i);
        num = num / 10;
        i++;
    }

    return decimal * signo;
}

int main() {
    int binario;
    printf("Ingrese un número binario en complemento a dos: ");
    scanf("%d", &binario);
    printf("El número decimal es: %d\n", binario_a_decimal_complemento_a_dos(binario));
    return 0;
}
