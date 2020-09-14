#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <sys/types.h>

int main( int argc , char *argv[] )
{
    int status;
    int n ;
    n = argc + 1 ;  
    char *arrayFiles[n];
    int i , j;
    if (argc > 1 ) {
        for (i = 1 ; i <= argc ; i++ ){
            if (!fork()){
                 execlp("gcc" , "gcc" , "-c" , argv[i], NULL);
            }
        }

        wait(&status);
        arrayFiles[0]  = "gcc" ;
        arrayFiles[1]  = "-o" ;
        for( j = 1; j < argc ; j++) {
        arrayFiles[j+1] = argv[j];
            if (j == argc){
                arrayFiles[j]= 0 ;
            }
        }

        execvp("gcc" ,  arrayFiles);

    } else {
        printf("erreur, veuillez ajouter un argument");
    }
    
    return 0;
}
