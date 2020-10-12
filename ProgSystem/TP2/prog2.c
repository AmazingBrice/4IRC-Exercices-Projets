#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <sys/types.h>

int main () {
    int k, retour, status, pid, ppid;
    for (k = 0 ; k < 3 ; k++)
    {
        ppid = getpid() ;      
        pid = fork() ;
        printf("dans le fork");

    
        wait(& status);
        retour = WEXITSTATUS(status);
        printf("(k= %d) : Je suis le processus: %d, mon père est de : %d, %d \n", k, pid, ppid, retour);
    }
   return 0;
}

