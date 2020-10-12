#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main( int argc, char *argv[]) {
	int tab[2];
	int pid;
	if(pipe(tab)!=0){ // Pipe return 0 on success
		perror("Error while creating the pipe.");
	}; // création du tube
	// 1 sera l'entrée du tube et 0 la sortie du tube


	if (argc > 1){

		if (fork()) { //processus fils
			close(tab[1]); // ferme l’entrée du tube
			dup2(tab[0] , 0); // copie la sortie du tube vers l’entrée standard
			close(tab[0]); // ferme le descripteur de la sortie du tube
			execlp("wc", "wc",NULL); // remplace les instructions du fils par wc
		}
		else { // processus pere
			close(tab[0]); // ferme la sortie du tube.
			dup2(tab[1] , 1); // copie l’entrée du tube vers la sortie standard
			close(tab[1]); // ferme le descripteur de l’entrée du tube
			execlp("cat", "cat",argv[1],NULL); // rempace les isnructions du pere par cat
		}

		printf("cat %s | wc : \n", argv[1]);
		return 0 ;
		
	}
	else {
		perror("Error not enough arguments");
	}
}

// Expected output 0	4	21