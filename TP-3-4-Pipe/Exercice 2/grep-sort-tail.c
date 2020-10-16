#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char *argv[]) {
	int tab[2],tab2[2]; 
	int sort;
	pipe(tab); // Création premier pipe
	pipe(tab2);	// Création deuxième pipe

	if (fork()==0) { // Je suis dans le processus fils 
		if (fork()==0) { // Je suis dans le processus petit-fils
			close(tab[1]); // Fermeture de l'entrée du premier pipe	
			close(tab2[0]);	 // Fermeture de la sortie du deuxième pipe
			dup2(tab[0],0); // Copie la sortie du tube vers l’entrée standard
			close(tab[0]); 	// Fermeture de la sortie du premier pipe
			dup2(tab2[1] , 1); // Copie l'entrée du tube vers l’entrée standard
			close(tab[1]); // Fermeture de la sortie du premier pipe
			execlp("grep","grep",argv[1], "toto.txt", NULL); // remplace les instructions du petit fils par grep avec notre fichier
		}
		else {
    		wait(NULL);
			close(tab2[0]); 	
			close(tab2[1]);	
			close(tab[0]); 
			dup2(tab[1] , 1);
			close(tab[1]); 
			execlp("sort", "sort","toto.txt", NULL); // remplace les instructions du fils par sort avec notre fichier
		}
	}		 
	else {
    	wait(NULL);
		close(tab[0]);
		close(tab[1]);	
		close(tab2[1]);	
		dup2(tab2[0] , 0); 	
		close(tab2[0]); 		
		sort=open("Sortie", O_CREAT | O_WRONLY, 0664); // On ouvre le fichier en création / écriture avec tous les droits 
		dup2(sort,1);
		execlp("tail", "tail","-n","5",NULL); // remplace les instructions du père par tail avec les 5 dernières lignes 
	}

	return 0 ;
}
