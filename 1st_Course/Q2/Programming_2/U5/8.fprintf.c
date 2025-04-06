#include <stdio.h>
#include <stdlib.h>
//creates a file.txt and write a string 
int main () {
   FILE * fp;
   fp = fopen ("file.txt", "w+");

   fprintf(fp, "%s %s %s %d", "We", "are", "in", 2012);

   fclose(fp);
   
   return(0);
}