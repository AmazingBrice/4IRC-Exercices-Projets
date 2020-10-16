#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void redirect (int signal) {

    if (signal == SIGUSR1) {
        while(1){
            printf("tata\n");
            sleep(1);          
        }
    }
    else if (signal == SIGUSR2 ) {
        printf("Fin du programme.\n");
        kill (pid,SIGKILL);
    }
}

int main()
{
    int pid = fork(); // Renvoie le pid du fils
    if (pid){ // Je suis le père
        printf("pid du fils à kill : %d\n", pid); // On utilisera : kill pid
        for (int i = 0; i < 5; ++i)
        {
            if (i == 2 || i == 4){ // 3ème et 5ème itérations
                kill (pid,SIGUSR1);
            }
            printf("toto\n");
            sleep(1);
        }
        kill (pid,SIGUSR2);
    }
    else { // Je suis le fils
        struct sigaction prepaSignal; 
        prepaSignal.sa_handler=&redirect;
        while (1){
            sigaction(SIGUSR1,&prepaSignal,NULL); // Redirection de SIGUSR1 vers le gestionnaire (redirect)             
            sigaction(SIGUSR2,&prepaSignal,NULL); // Redirection de SIGUSR2             
        }
    }

    return 0;
}
