#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	int i, n;
	if (argc == 2){
		n = strlen(argv[1])+1;
		char* string = malloc( n );
		char* reverseString = malloc( n );
		strcpy(string, argv[1]);
		for (i=0; i<n; i++){
			reverseString[i] = string[n-i-2];
			printf("%c\n",reverseString[i]);
		}
		reverseString[n]='\0';
		printf("%s\n",reverseString);
	}
	else
	{
		puts("Erreur: faut mettre un argument.");
		return -1;
	}
	return 0;
}
