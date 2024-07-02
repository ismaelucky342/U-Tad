#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_ELEMENTOS 12
#define NUM_TERMINACIONES 10
 
void leeNumeros(int num_premiados[], int num_elementos);
void calculaTerminaciones(int* terminaciones, int* num_premiados, int num_elementos); 
int maximoNumeroPremiado(int num_premiados[], int num_elementos);
int terminacionMasPopular(int terminaciones[], int num_elementos);

	
int main(int argc, char** argv)
{
	int i, j;
	int num_premiados[NUM_ELEMENTOS];
	int numMasAlto=0;
	int terminaciones[NUM_TERMINACIONES]={0,0,0,0,0,0,0,0,0,0};		
	
	printf("Introduce 12 números entre 0 y 90.000. Deben ser los premiados en los últimos 12 sorteos\n");
	leeNumeros(num_premiados, NUM_ELEMENTOS);
	
	printf("\n==> Los números premiados en los últimos 12 sorteos son:\n");
	
	for (i=0; i<NUM_ELEMENTOS; i++)
	{
		 printf("%d	", num_premiados[i] );
	}
	printf("\n");	
	calculaTerminaciones(terminaciones, num_premiados, NUM_ELEMENTOS); 
	
	for (i=0; i<NUM_TERMINACIONES; i++)
	{
		printf("Numeros terminados en %d: %d\n", i, terminaciones[i]);
	}
	int termPopular = terminacionMasPopular(terminaciones, NUM_TERMINACIONES);
	printf("==> La terminación más popular en estos años ha sido el: %d\n", termPopular); 
	
	numMasAlto= maximoNumeroPremiado(num_premiados, NUM_ELEMENTOS);
	printf("\n==>El número premiado más alto premiado en estos últimos años ha sido el: %d\n", numMasAlto);

}

void leeNumeros(int num_premiados[], int num_elementos)
{
	int res;
	
	for (int i=0; i<num_elementos; i++)
	{
		printf("Introduce el número: %d\n", i+1);
		do{
			 res=scanf("%d", &num_premiados[i]);
			 while (getchar()!='\n');
			 if (num_premiados[i] <= 0 || num_premiados[i]>90000) printf("El número no es correcto. Intentalo de nuevo\n");
			 if (res!=1) printf("El dato no es válido\n");
		}while (num_premiados[i] <= 0 || num_premiados[i] > 90000 || res!=1);
	}
}

void calculaTerminaciones(int terminaciones[], int num_premiados[], int num_elementos)
{
	int cifra;
		
	for (int i=0; i<num_elementos; i++)
	{
		cifra=num_premiados[i]%10;
		terminaciones[cifra]++;
	}
	return;
}

int terminacionMasPopular(int terminaciones[], int num_elementos)
{
	int numMax, popular;
	
	numMax=terminaciones[0];
	for (int i=1; i<num_elementos; i++)
	{
		if (terminaciones[i]>numMax){
				numMax=terminaciones[i];
				popular=i;
		}
	}
	
	return popular;
	
}


int maximoNumeroPremiado(int num_premiados[], int num_elementos)
{
	int maximo;
	
	maximo=num_premiados[0];
	for (int i=1; i<num_elementos; i++)
	{
		if (num_premiados[i]>maximo){
				maximo=num_premiados[i];
		}
	}
		return maximo;
}
