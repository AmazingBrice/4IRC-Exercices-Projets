#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <sys/types.h>

int main()
{
    int status;
    if (!fork()) {
        if (!fork())
        {
            if (!fork()){
                printf("who");
                execlp("who", "who", NULL);
            }
            wait(&status);
            printf("ps");
            execlp("ps", "ps", NULL);
        }
        wait(&status);
        printf("ls -l");
        execlp("ls", "ls", "-l", NULL);
    }
    wait(&status);
    return 0;
}
