// BELDJILALI Ilies & FOLLEAS Brice

// Includes
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h> /*fichier test_sem_dijkstra.c */
#include <sys/ipc.h>
#include <sys/sem.h>
#include "dijkstra.c"
#define CLE 1

int main() {
  int sem ;
  sem = sem_create(CLE,0); // Creation semaphore
  printf("Creation du sémaphore d'identificateur %d\n",sem);
  if (fork() == 0) {
    printf("Je suis le fils et j'attends 15 secondes...\n");
    sleep(15) ;
    printf("Je suis le fils et je fais V sur le sémaphore\n");
    V(sem) ;
    exit(0);
  }
  else {
    printf("Je suis le père et je me bloque en faisant P sur le sémaphore\n\n");
    P(sem);
    printf("Je suis le père et je suis libre\n\n");
    sem_delete(sem);
  }
}
