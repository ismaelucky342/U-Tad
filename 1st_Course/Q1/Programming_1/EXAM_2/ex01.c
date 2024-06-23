#include <stdio.h>
#include <string.h>

#define NUM_MIN_CARACTERES 	8
#define NUM_MAX_CARACTERES 15


// Funcion que valida el formato del login (3 numeros, 1 letra MAY, 1 letra min y un guión
// y devuelve 1 su es valido y 0 en caso contrario
int validaLogin(char login[NUM_MAX_CARACTERES]);

// Genera la password según el algortimo de transformación
void generaPassword(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES]);

// Función que valida el formato del login (3 numeros, 1 letra MAY, 1 letra min y un guión
// y devuelve 1 su es valido y 0 en caso contrario
// al mismo tiempo genera la password según el algortimo de transformación
// int validaLoginYgeneraPasswd(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES]);


int main()
{
	char car; 
	int i, valido,salir;
	char login[NUM_MAX_CARACTERES+1];
	char password[NUM_MAX_CARACTERES+1];
	
	printf("Introduce el login de usuario: \n");
	printf("Debe tener entre 8 y 15 caracteres, y tener mínimo tres números, una MAY, una MIN, y un '-'\n"); 
	
	valido=0;
	salir=0;
	i=0;
	login[i]='\0';
	
	do {
		car=getchar();
		while(i<NUM_MAX_CARACTERES &&!salir)
		{
			if (car!='\n')
			{
				login[i] = car;
				i++;
				car=getchar();
			}
			else if(car=='\n' && i< NUM_MIN_CARACTERES)
			{
				printf("===>ERROR: El login debe tener mínimo 8 caracteres. Intentalo de nuevo\n");
				i=0;
				car=getchar();
			}
			else // car=='\n' y long >=8
			{
				salir=1;
			}
		}
		
		// si nos hemos salido porque car!='\n' y la long supera el maximo, limpiamos el buffer
		if (car!='\n') while(getchar()!='\n');
		
		// y terminamos el login
		login[i]='\0';
		printf("\n===>El login introducido es: %s\n", login);
		printf("===> Su longitud es: %d\n", i);
		
		// Validamos si tiene el formato adecuado
		//if (validaLoginYgeneraPasswd(login, password) == 0)
		if (validaLogin(login) == 0)
		{
			printf("\n===>El login NO ES valido, intentalo de nuevo\n");
			i=0;
			salir=0;
		}
		else
		{
			valido=1;
			printf("\n===>El login ES válido.\n");
		}
	}while (!valido);

	generaPassword(login, password);
	printf("===>La password de acceso es: %s\b", password);
	
}

// Funcion que valida si el formato del login es correcto
int validaLogin(char login[NUM_MAX_CARACTERES])
{
	int i=0;
	int cont_nums=0;
	int cont_may=0;
	int cont_min=0;
	int cont_guion=0;
	
	while(login[i] != '\0')
	{
		if (login[i] >= '0' && login[i] <='9')
		{
			cont_nums++;
			
		}
		else if (login[i] >='A' && login[i] <='Z')
		{
			cont_may++;
			
		}
		else if (login[i] >= 'a' && login[i] <='z')
		{
			cont_min++;
			
		}
		else if (login[i] == '-')
		{
			cont_guion++;
			
		}
		i++;
		
	}
	if (cont_nums>=3 && cont_may>=1 && cont_min>=1 && cont_guion>=1) return 1;
	else return 0;
	
}

// Función que genera la password con el algoritmo de transformación
void generaPassword(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES])
{
	int i=0, j=0;
	char aux_passwd[NUM_MAX_CARACTERES];
	
	printf("\n==>Vamos a generar la password\n");
	
	while(login[i] != '\0')
	{
		if (login[i] >= '0' && login[i] <='9')
		{
			aux_passwd[j] = login[i];
		}
		else if (login[i] >= 'A' && login[i] <='Z')
		{
			aux_passwd[j] = login[i] + ('a' -'A');
		}
		else if (login[i] >= 'a' && login[i] <='z')
		{
			aux_passwd[j] = login[i] - ('a' -'A');
		}
		else if (login[i] == '-')
		{
			aux_passwd[j] = '*';
		}
		i++;
		j++;
	}
	aux_passwd[j]='\0';
	
	printf("Primera parte de la transformacion de la passwd: %s\n", aux_passwd);
	
	// Ahora invertimos la password para transformarla totalmente
	i=0;
	while(aux_passwd[i] != '\0')	// "hola"  j=4 i=0
	{
		password[i] = aux_passwd[j-1];
		i++;
		j--;
	}
	password[i]='\0';
	
}


/*

// Función que genera la password con el algoritmo de transformación
void generaPassword(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES])
{
	int i=0, j=0;
	
	while(login[i] != '\0')
	{
		if (login[i] >= '0' && login[i] <='9')
		{
			password[j] = login[i] + ('z' - '9');

		}
		else if (login[i] >= 'A' && login[i] <='Z')
		{
			password[j] = login[i] + ('a' -'A');
		}
		else if (login[i] >= 'a' && login[i] <='z')
		{
			password[j] = login[i] - ('a' -'A');
		}
		else if (login[i] == '-')
		{
			password[j] = '*';
		}
		i++;
		j++;
	}
	password[j]='\0';
}
*/



// Función que valida el formato del login y genera la password al mismo tiempo. 
//int validaLoginYgeneraPasswd(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES])
/*
{
	int i=0,j=0;
	int cont_nums=0;
	int cont_may=0;
	int cont_min=0;
	int cont_guion=0;
	
	while(login[i] != '\0')
	{
		if (login[i] >= '0' && login[i] <='9')
		{
			cont_nums++;
			password[j] = login[i] + ('z' - '9');
		}
		else if (login[i] >='A' && login[i] <='Z')
		{
			cont_may++;
			password[j] = login[i] + ('a' -'A');
		}
		else if (login[i] >= 'a' && login[i] <='z')
		{
			cont_min++;
			password[j] = login[i] - ('a' -'A');
		}
		else if (login[i] == '-')
		{
			cont_guion++;
			password[j] = '*';
		}
		i++;
		j++;
	}
	password[j]='\0';
	
	if (cont_nums>=3 && cont_may>=1 && cont_min>=1 && cont_guion>=1) return 1;
	else return 0;
	
}
*/