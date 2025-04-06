#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct {
    char nombre[20];
    char apellido[20];
    char telefono[15];
} registro;

 

int main()
{
     FILE *fichero;
    if ((fichero = fopen( "nombres.txt", "a" )) == NULL) {
         printf( "No se puede abrir el fichero.\n" );
         exit( 1 );
    } 
    do {
         printf( "Nombre: " ); gets(registro.nombre);
         if (strcmp(registro.nombre,"")) {
             printf( "Apellido: " ); gets(registro.apellido);
             printf( "Teléfono: " ); gets(registro.telefono);
             /* Guarda el registro en el fichero */
             fwrite( &registro, sizeof(registro), 1, fichero );
         }
    } while (strcmp(registro.nombre,"")!= 0);
    fclose( fichero );
    return 0;
}

