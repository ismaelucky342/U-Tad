#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define NUM_DIAS 30

void leeTemperaturas(float temperaturas[], int num_dias);
float calculaMaxima(float temperaturas[], int num_dias);
float calculaMinima(float temperaturas[], int num_dias);
float calculaMedia(float temperaturas[], int num_dias);
int cuentaDiasSobreMedia(float temperaturas[], int num_dias, float media);

int main()
{
    int temperaturas[NUM_DIAS];

    printf("ingrese las temperaturas en los ultimos 30 dias: \n");
    leeTemperaturas(temperaturas, NUM_DIAS);

    printf("temperaturas registradas: \n");
    for (int i = 0; i < NUM_DIAS; i++)
    {
        printf("%.2f", temperaturas[i]);
    }
    printf("\

    return 0;
}

void leeTemperaturas(float temperaturas[], int num_dias)
{
    for (i = 0; i < num_dias; i++)
    {
        printf("ingrese la temperatura del dia %d: ", i + 1);
        scanf("%f", &temperaturas[i]);
    }
}

float calculaMaxima(float temperaturas[], int num_dias)
{
    float max = temperaturas[0];
    for (int i = 1; i < num_dias; i++)
    {
        if (temperaturas[i] > max)
        {
            max = temperaturas[i];
        }
        return max;
    }

}
    
float calculaMinima(float temperaturas[], int num_dias)
{
    float min = temperaturas[0];
    for (int i = 1; i < num_dias; i++)
    {
        if (temperaturas[i] < min)
        {
            min = temperaturas[i];
        }
        return min;
    }

}

float calculaMedia(float temperaturas[], int num_dias)
{
    float suma = 0;
    for (int i = 0; i < num_dias; i++) {
        suma += temperaturas[i];
    }
    return suma / num_dias;
}


int cuentaDiasSobreMedia(float temperaturas[], int num_dias, float media) ç
{
    int cuenta = 0;
    for (int i = 0; i < num_dias; i++) {
        if (temperaturas[i] > media) {
            cuenta++;
        }
    }
    return cuenta;
}