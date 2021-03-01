#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

//Pour les timeout
#include <errno.h>
#include <string.h>

void timeout5()
{

    printf("terminé");
    exit(0);
}

int main(int argc, char *argv[])
{

    int entier;
    char entree[50];

    /**struct sigaction sa;
    *sa.sa_handler = timeout5;
    *sigaction(SIGALRM, &sa, NULL);
    
    */
    alarm(5);
    signal(SIGALRM, timeout5);

    while (1)
    {
        printf("veuillez entrer un entier : \n");
        scanf("%s", entree);

        //printf("%s\n", entree);

        //printf("test : %d format : %d\n ", entier, format);

        if (sscanf(entree, "%d", &entier) == 0)
        {
            printf("Mauvais format\n");
        }
        else
        {
            printf("merci \n");
            break;
        }
    }

    return (0);
}