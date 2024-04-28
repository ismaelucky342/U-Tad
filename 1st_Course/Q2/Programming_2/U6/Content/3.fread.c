#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct {
    char nombre[20];
    char apellido[20];
    char telefono[15];
} registro;

int main(){
    FILE *fichero;

    if ((fichero = fopen( "nombres.txt", "r" )) == NULL) {
         printf( "No se puede abrir el fichero.\n" );
         exit( 1 );
    }
    while (!feof(fichero)) {
         if (fread( &registro, sizeof(registro), 1, fichero )) {
             printf( "Nombre: %s\n",   registro.nombre );
             printf( "Apellido: %s\n", registro.apellido);
             printf( "Teléfono: %s\n", registro.telefono);
         }
    }
    fclose( fichero );
    return 0;
}