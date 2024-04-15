#include <stdio.h>

int main (int argc, char argv[]) {

   FILE * fichDesc;
   char Cadena[50];

   fichDesc = fopen("letras.txt", "r");

   if (fichDesc ==NULL) //Comprobar si ha habido errores   
       printf("Error, el archivo no existe\n");

   if( fgets (Cadena, 500, fichDesc)!=NULL ) {
      /* escribiendo el contenido al stdout */
      printf("%s\n",Cadena);
   }
   fclose(fichDesc);

   return(0);
}