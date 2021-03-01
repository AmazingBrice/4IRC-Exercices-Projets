#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

int main()
{
	struct sigaction prepaSignal; // Déclaration d'une structure sigaction pour la mise en place des gestionnaires
  
  prepaSignal.sa_handler=SIG_IGN; // Remplissage de la structure avec l'adresse du gestionnaire (ici SIG_IGN car on veut ignorer les signals dans le masque)
  prepaSignal.sa_flags=0; // Mise a zero du champ sa_flags theoriquement ignoré
  sigemptyset(&prepaSignal.sa_mask); // On initialise le masque à vide
	sigaddset(&prepaSignal.sa_mask,SIGINT); // On ajoute au masque le signal SIGINT

  while(1){
   	printf("toto\t");
  } // En attente d'une interruption
  return 0;
}
