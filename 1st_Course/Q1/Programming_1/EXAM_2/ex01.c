#include <stdio.h>
#include <string.h>

#define NUM_MIN_CARACTERES 8
#define NUM_MAX_CARACTERES 15

int validaLogin(char login[NUM_MAX_CARACTERES]);
void generaPassword(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES]);

int main()
{
    char car;
    int i, valido, salir;
    char login[NUM_MAX_CARACTERES + 1];
    char password[NUM_MAX_CARACTERES + 1];

    printf("Introduce el login de usuario: \n");
    printf("Debe tener entre 8 y 15 caracteres, y tener mínimo tres números, una MAY, una MIN, y un '-'\n");

    valido = 0;

    while (!valido)
    {
        i = 0;
        salir = 0;
        printf("Introduce el login: ");

        for (; i < NUM_MAX_CARACTERES && !salir; i++)
        {

            if (scanf("%c", &car) == 1)
            {
                if (car != '\n')
                {
                    login[i] = car;
                }
                else if (car == '\n' && i < NUM_MIN_CARACTERES)
                {
                    printf("===>ERROR: El login debe tener mínimo 8 caracteres. Inténtalo de nuevo\n");
                    i = -1; // Reiniciar el índice para empezar de nuevo
                    printf("Introduce el login: ");
                }
                else
                {
                    salir = 1;
                }
            }
        }

        if (car != '\n')
        {
            while (getchar() != '\n')
                ; // Limpiar el buffer de entrada
        }

        login[i] = '\0';
        printf("\n===>El login introducido es: %s\n", login);
        printf("===> Su longitud es: %d\n", i);

        if (validaLogin(login) == 0)
        {
            printf("\n===>El login NO ES válido, inténtalo de nuevo\n");
        }
        else
        {
            valido = 1;
            printf("\n===>El login ES válido.\n");
        }
    }

    generaPassword(login, password);
    printf("===>La password de acceso es: %s\n", password);

    return 0;
}

int validaLogin(char login[NUM_MAX_CARACTERES])
{
    int i = 0;
    int cont_nums = 0;
    int cont_may = 0;
    int cont_min = 0;
    int cont_guion = 0;

    while (login[i] != '\0')
    {
        if (login[i] >= '0' && login[i] <= '9')
        {
            cont_nums++;
        }
        else if (login[i] >= 'A' && login[i] <= 'Z')
        {
            cont_may++;
        }
        else if (login[i] >= 'a' && login[i] <= 'z')
        {
            cont_min++;
        }
        else if (login[i] == '-')
        {
            cont_guion++;
        }
        i++;
    }
    return (cont_nums >= 3 && cont_may >= 1 && cont_min >= 1 && cont_guion >= 1);
}

void generaPassword(char login[NUM_MAX_CARACTERES], char password[NUM_MAX_CARACTERES])
{
    int i = 0, j = 0;
    char aux_passwd[NUM_MAX_CARACTERES];

    printf("\n==>Vamos a generar la password\n");

    while (login[i] != '\0')
    {
        if (login[i] >= '0' && login[i] <= '9')
        {
            aux_passwd[j] = login[i];
        }
        else if (login[i] >= 'A' && login[i] <= 'Z')
        {
            aux_passwd[j] = login[i] + ('a' - 'A');
        }
        else if (login[i] >= 'a' && login[i] <= 'z')
        {
            aux_passwd[j] = login[i] - ('a' - 'A');
        }
        else if (login[i] == '-')
        {
            aux_passwd[j] = '*';
        }
        i++;
        j++;
    }
    aux_passwd[j] = '\0';

    printf("Primera parte de la transformacion de la passwd: %s\n", aux_passwd);

    i = 0;
    while (aux_passwd[i] != '\0')
    {
        password[i] = aux_passwd[j - 1];
        i++;
        j--;
    }
    password[i] = '\0';
}
