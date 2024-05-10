#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    char str1[50]; 
    char a; 
    char b; 
    char c; 
    
    printf("Enter the string: \n");
    scanf("%s", &str1);
    getchar(); 
    
    printf("Enter char a: \n"); 
    scanf("%c", &a);  

    printf("Enter char b: \n"); 
    b = getchar();  
    
    printf("Enter char c: \n"); 
    c = getc(stdin); 
    printf("the string is: %s: \n", str1); 
    printf("char a: %c \n", a); 
    printf("char b: %c \n", b); 
    printf("char c: %c \n", c); 

    return 0; 
}