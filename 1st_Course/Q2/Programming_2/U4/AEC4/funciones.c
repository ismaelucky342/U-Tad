#include "funciones.h"
#include <stdio.h>

char* encriptaMensaje(char* cadena_mayusculas);
char* encuentraDatos(char* cadena_encriptada);
char* decodificaDatos(char* cadena_encriptada_datos);
char tablaEncriptacion(char letra);
char* cambiaMayusculas(char* cadena_leida);

char* leeLineaDinamica() {
    char* buffer = NULL;
    size_t bufsize = 0;
    getline(&buffer, &bufsize, stdin);
    return buffer;
}

char* cambiaMayusculas(char* cadena_leida) {
    char* resultado = strdup(cadena_leida);
    int contiene_minusculas = 0;

    for (int i = 0; resultado[i] != '\0'; i++) {
        if (islower(resultado[i])) {
            contiene_minusculas = 1;
            break;
        }
    }

    if (!contiene_minusculas) {
        return resultado;
    }

    // Procedemos a cambiar las mayúsculas y minúsculas según corresponda
    int primera_letra = 1;
    for (int i = 0; resultado[i] != '\0'; i++) {
        if (isalpha(resultado[i])) {
            if (primera_letra) {
                resultado[i] = toupper(resultado[i]);
                primera_letra = 0;
            } else {
                resultado[i] = tolower(resultado[i]);
            }
        } else {
            primera_letra = 1; // Reiniciamos para la próxima palabra
        }
    }

    return resultado;
}

char* encriptaMensaje(char* cadena_mayusculas) {
    char* resultado = strdup(cadena_mayusculas);
    for (int i = 0; resultado[i] != '\0'; i++) {
        if (isalpha(resultado[i])) {
            if (resultado[i] >= 'A' && resultado[i] <= 'Z') {
                resultado[i] = tablaEncriptacion(resultado[i] - 'A');
            }
        }
    }
    return resultado;
}

char* encuentraDatos(char* cadena_encriptada) {
    char* inicio = strchr(cadena_encriptada, '(');
    char* fin = strchr(cadena_encriptada, ')');
    if (inicio != NULL && fin != NULL && fin > inicio) {
        int longitud = fin - inicio - 1;
        char* resultado = (char*)malloc((longitud + 1) * sizeof(char));
        strncpy(resultado, inicio + 1, longitud);
        resultado[longitud] = '\0';
        return resultado;
    } else {
        return NULL;
    }
}

char* decodificaDatos(char* cadena_encriptada_datos) {
    char* resultado = strdup(cadena_encriptada_datos);
    char* campos_decodificados = (char*)malloc(strlen(resultado) * sizeof(char));

    // Variables para almacenar los campos decodificados
    char* clave = NULL;
    char* identificador = NULL;
    char* especialidad = NULL;
    char* estado = NULL;

    // Tokenizar la cadena encriptada para extraer los campos
    char* token = strtok(resultado, "-");
    if (token != NULL) {
        clave = strdup(token);
        strcat(campos_decodificados, clave);
        token = strtok(NULL, "-");
        if (token != NULL) {
            identificador = strdup(token);
            strcat(campos_decodificados, identificador);
            token = strtok(NULL, "-");
            if (token != NULL) {
                especialidad = strdup(token);
                strcat(campos_decodificados, especialidad);
                token = strtok(NULL, "-");
                if (token != NULL) {
                    estado = strdup(token);
                    strcat(campos_decodificados, estado);
                }
            }
        }
    }

    // Liberar la memoria asignada
    free(resultado);
    free(clave);
    free(identificador);
    free(especialidad);
    free(estado);

    return campos_decodificados;
}

char tablaEncriptacion(char letra) {
    switch (letra) {
        case 'A': return 'W';
        case 'B': return 'X';
        case 'C': return 'A';
        case 'D': return 'H';
        case 'E': return 'Q';
        case 'F': return 'F';
        case 'G': return 'P';
        case 'H': return 'I';
        case 'I': return 'R';
        case 'J': return 'V';
        case 'K': return 'K';
        case 'L': return 'B';
        case 'M': return 'J';
        case 'N': return 'D';
        case 'O': return 'G';
        case 'P': return 'Q';
        case 'Q': return 'E';
        case 'R': return 'L';
        case 'S': return 'N';
        case 'T': return 'W';
        case 'U': return 'V';
        case 'V': return 'T';
        case 'W': return 'Y';
        case 'X': return 'U';
        case 'Y': return 'Z';
        case 'Z': return 'S';
        case '0': return '7';
        case '1': return '8';
        case '2': return '3';
        case '3': return '5';
        case '4': return '4';
        case '5': return '6';
        case '6': return '2';
        case '7': return '0';
        case '8': return '1';
        case '9': return '0';
        default: return letra; // Si no es un caracter válido, se mantiene igual
    }
}