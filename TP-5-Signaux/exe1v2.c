#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

// Pour utiliser sigaction, on doit faire appel à des gestionnaires
// Ici on définit un gestionnaire vers lequel seront redirigés les signaux par la suite

void redirect(int signal)
{
  printf("\n Je receptionne le signal %d\n",signal);
  if (signal == 2){
    printf("Reception du signal SIGINT -> Arret du programme\n");
    exit(1);
  }
  fflush(stdout); // On vide le buffer
}

int main()
{
  struct sigaction prepaSignal; // Déclaration d'une structure sigaction pour la mise en place des gestionnaires
  
  prepaSignal.sa_handler=&redirect; // Remplissage de la structure avec l'adresse du gestionnaire (redirect)
  prepaSignal.sa_flags=0; // Mise a zero du champ sa_flags theoriquement ignoré
  sigemptyset(&prepaSignal.sa_mask); // On ne bloque pas de signaux spécifiques

  // Pour voir les différents signaux depuis un raccourci clavier utiliser : `stty -a`

  // Mise en place du gestionnaire pour gérer la redirection de SIGINT
  sigaction(SIGINT,&prepaSignal,0); // `CTRL+C`

  // Il faut le tuer avec un kill -HUP avec le PID */
  while (1){
      printf("toto\t");
  }

  return 0;
}   