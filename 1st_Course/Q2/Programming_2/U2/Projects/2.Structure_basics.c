#include<stdio.h>

struct account 
{
    char name[30];
    char Surname[40];
    int id; 
    int balance;   
} ;
int  main() {
    struct account acc1,acc2;
    
    printf("Enter the first user id: \n");
    scanf("%d", &acc1.id);
    printf("Enter the second user id: \n");
    scanf("%d", &acc2.id);

    printf("Enter name and surname of 1st user: \n"); 
    scanf("%s\n %s\n", &acc1.name, &acc1.Surname);
    printf("Enter name and surname of 2nd user: \n"); 
    scanf("%s\n %s\n", &acc2.name, &acc2.Surname);
    return 0; 
}