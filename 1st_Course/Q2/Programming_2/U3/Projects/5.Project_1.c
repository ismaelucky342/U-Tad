#include <stdio.h>
#include <stdlib.h>
#define TAM_BLOQUE 10

char *LeeLineaDinamica();

void main (int argc, char *argv[])
{
      char *nombre;

      printf ("Intoduce nombre \n");
      nombre = LeeLineaDinamica ();
      printf ("En nombre es: %s",nombre);

      free (nombre);
}

char *LeeLineaDinamica()
{
      int tamBuffer = TAM_BLOQUE;
      char *linea = (char*)malloc(TAM_BLOQUE);
      int numCaracteres=0;
      char c = 0;

      c=getchar();
      while (c != '\n')
      {
            linea[numCaracteres] = c;
            numCaracteres ++;

            if (numCaracteres == tamBuffer){
                  tamBuffer += TAM_BLOQUE;
                  linea = (char *) realloc (linea,tamBuffer);
            }
            c=getchar();
      }
      linea[numCaracteres] = '\0';
      return linea;
}