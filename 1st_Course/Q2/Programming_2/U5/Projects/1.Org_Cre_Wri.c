#include<stdio.h>

int main()
{
	int array[100];
	FILE *fp; 
	fp = fopen("a.txt", "r");

	if(fp!=NULL){
	}else{
		printf("ERROR");
	}

	return 0; 
}
