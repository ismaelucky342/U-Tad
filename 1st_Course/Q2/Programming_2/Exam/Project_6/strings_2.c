#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* leeLineaDinamica();
void cambiaMayusculas(char *cadena);
void encriptaMensaje(char *mensaje);
char* encuentraDatos(const char *mensaje);
void separaDatos(const char *datos, char **campos); 
void decodificaDatos(char **campos);

int main() {

    printf("Ingrese el mensaje: ");
    char *mensaje = leeLineaDinamica();

 
    cambiaMayusculas(mensaje);
    printf("Mensaje transformado: %s\n", mensaje);

    encriptaMensaje(mensaje);
    printf("Mensaje encriptado: %s\n", mensaje);

    char *datos = encuentraDatos(mensaje);
    printf("Datos complejos: %s\n", datos);

    char *campos[4];
    separaDatos(datos, campos);

    decodificaDatos(campos);

    free(mensaje);
    free(datos);

    return 0;
}

char* leeLineaDinamica() {
    char *linea = NULL;
    size_t tam = 0;
    getline(&linea, &tam, stdin);
    linea[strcspn(linea, "\n")] = '\0'; 
    return linea;
}

void cambiaMayusculas(char *cadena) {
    int i = 0;
    while (cadena[i] != '\0') {
        if (i == 0 || cadena[i - 1] == ' ') {
            if (cadena[i] >= 'a' && cadena[i] <= 'z') {
                cadena[i] -= 32; 
            }
        } else {
            if (cadena[i] >= 'A' && cadena[i] <= 'Z') {
                cadena[i] += 32; 
            }
        }
        i++;
    }
}

void encriptaMensaje(char *mensaje) {
    char caracteres[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    char reemplazos[] = "WXAHQFPIRVKBJDGMELNOYUTCZS7835462910";
    
    for (int i = 0; mensaje[i] != '\0'; i++) {
        if (mensaje[i] >= 'A' && mensaje[i] <= 'Z') {
            mensaje[i] = reemplazos[mensaje[i] - 'A'];
        } else if (mensaje[i] >= '0' && mensaje[i] <= '9') {
            mensaje[i] = reemplazos[mensaje[i] - '0' + 26];
        }
    }
}

char* encuentraDatos(const char *mensaje) {
    char *inicio = strchr(mensaje, '[');
    char *fin = strchr(inicio, ']');
    if (inicio != NULL && fin != NULL) {
        char *datos = (char*)malloc(fin - inicio);
        strncpy(datos, inicio + 1, fin - inicio - 1);
        datos[fin - inicio - 1] = '\0';
        return datos;
    }
    return NULL;
}

void separaDatos(const char *datos, char **campos) {
    char *token = strtok((char*)datos, "-");
    int i = 0;
    while (token != NULL) {
        campos[i++] = token;
        token = strtok(NULL, "-");
    }
}

void decodificaDatos(char **campos) {
    printf("Clave: %s\n", campos[0]);
    printf("Identificador: %s\n", campos[1]);
    printf("Especialidad: %s\n", campos[2]);
    printf("Estado: %s\n", campos[3]);
}
