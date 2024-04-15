
#include <stdio.h>

 

int main (int argc, char argv[]) {

   FILE * fichDesc;
   char Caracter;

   fichDesc = fopen("letras.txt", "r");

   if (fichDesc ==NULL) //Comprobar si ha habido errores   

       printf("Error, el archivo no existe\n");
   Caracter = getc (fichDesc);

   while (Caracter != EOF) {
      printf ("%c",Caracter);
      Caracter = getc(fichDesc);
   }

   fclose(fichDesc);
   return(0);

}