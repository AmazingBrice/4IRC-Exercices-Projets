#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

// Pour s'aider on utilisera la commande : ps -l
void redirect (int signal) {
    printf("\nReception signal SIGINT\n");
}   

int main()
{
    int pid = fork(); // Renvoie le pid du fils
    if (pid){ // Je suis le père
        printf("pid du fils à kill : %d\n", pid); // On utilisera : kill pid
        for (int i = 0; i < 3; ++i)
        {
            printf("toto\n");
            sleep(1);
        }
    }
    else { // Je suis le fils
        struct sigaction prepaSignal; 
        prepaSignal.sa_handler=&redirect;
        sigaction(SIGINT,&prepaSignal,NULL); // Appel de la fonciton sigaction plus propre
        while(1){
            printf("tata\n");
            sleep(1);            
        }
    }
}

/* Ouput : une fois le signal envoyé, le père est arrêté mais 
le fils lui ne reçois pas d'interruption et continue sa boucle infinie
*/