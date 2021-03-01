#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	int i, j, n;
	if (argc >= 2){
        for (j=1; j<argc; j++ ){
            n = strlen(argv[j])+1;
		    char* string = malloc( n );
            char* reverseString = malloc( n );
		    strcpy(string, argv[j]);
            for (i=0; i<n; i++){
			    reverseString[i] = string[n-i-2];
		    }
            reverseString[n]='\0';
		    printf("%s\n",reverseString);
        }
	}
	else
	{
		puts("Erreur: faut mettre un ou plusieurs arguments connard.");
		return -1;
	}
	return 0;
}
