#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main(){
    if(!fork()){
        if(!fork()){
            if(!fork()){
                execlp("who", "who", NULL);
            }
            execlp("ps", "ps", NULL);
        }
        execlp("ls", "ls", "-l", NULL);
        }
    return 0;
}
