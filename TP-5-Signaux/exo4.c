#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

int main()
{
    int pid = fork(); // Renvoie le pid du fils
    if (pid){ // Je suis le père
        for (int i = 0; i < 3; ++i)
        {
            printf("toto\n");
            sleep(1);
        }
        kill(pid, SIGKILL);
    }
    else { // Je suis le fils
        while(1){
            printf("tata\n");
            sleep(1);
        }
    }
}
