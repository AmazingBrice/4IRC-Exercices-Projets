#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int StartsWith(const char *a, const char *b)
{
   if(strncmp(a, b, strlen(b)) == 0) return 1;
   return 0;
}

int main(int nbarg, char **arg) {
    extern char** environ;
    char* ptr;
    int i;
    if (nbarg == 2){
        for (i=0; environ[i]!=NULL; i++ ){
            ptr = environ[i];
            if( StartsWith(ptr,arg[1])){

                printf("La valeur de %s \n", ptr);
            }
        }
        return 0;
    }
	return -1;
}
