#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <sys/types.h>

int main () {
    int status;
    if(!fork()){
          if(!fork()){
            printf("Je suis le fils 1\n");
            execlp("echo","echo","POUR SANAAAA!",NULL);     
            exit(1);
        }
        wait(&status);
        printf("Je suis le fils 2\n");
        execlp("echo","echo","POUR HYUJIII!",NULL);     
        exit(1);
    }
    wait(&status);
    return 0;
}
