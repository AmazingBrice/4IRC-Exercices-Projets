#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

int fin = 1;

void redirect (int signal) {
    if (signal == 2){
        printf("Reception signal SIGINT\n");
        printf("Set bool to true");
        fin = 0;
    }
}

int main()
{
    // Si Le signal SIGINT est envoyé, il est redirigé vers redirect
    struct sigaction prepaSignal; // Déclaration d'une structure sigaction pour la mise en place des gestionnaires
  
    prepaSignal.sa_handler=&redirect;
     // Remplissage de la structure avec l'adresse du gestionnaire (redirect)
    prepaSignal.sa_flags=0; // Mise a zéro du champ sa_flags theoriquement ignoré
    sigemptyset(&prepaSignal.sa_mask); // On initialise le masque à vide
    sigaddset(&prepaSignal.sa_mask,SIGINT); // On ajoute au masque le signal SIGINT

    while(fin){
        printf("toto\t");
    } // En attente d'une interruption
    return 0;
}
