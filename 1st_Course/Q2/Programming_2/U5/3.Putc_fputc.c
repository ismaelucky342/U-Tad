#include <stdio.h>

int main (int argc, char argv[]) {

   FILE *fichDesc;
   //int Caracter; //es indiferente char que int

   char Caracter;
   fichDesc = fopen("letras.txt", "w");

   for( Caracter = 65 ; Caracter <= 122; Caracter++ ){
      putc(Caracter, fichDesc);
      putc (';',fichDesc);
   }
    fclose(fichDesc);
   return(0);

}