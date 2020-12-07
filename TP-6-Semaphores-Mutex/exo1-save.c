// BELDJILALI Ilies & FOLLEAS Brice

// Includes

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#define KEY 123


union semun {
  int val;  /* Value for SETVAL */
  struct semid_ds *buf;    /* Buffer for IPC_STAT, IPC_SET */
  unsigned short  *array;  /* Array for GETALL, SETALL */
  // ushort array[1] ; /*tableau de taille égale au nombre de sémaphores de l'ensemble */
} arg;

int main()
{
  int semid; // Déclaration id du semaphore
  // Creation du semaphore
  semid = semget((key_t)KEY, 1, IPC_CREAT|IPC_EXCL|0666) // Déclaration : int semget(key_t key, int nsems, int semflg)
  if (semid == -1) {
  perror("Echec de semget") ;
    exit(1) ;
  }
  printf(" le semid de l'ensemble de semaphore est : %d\n",semid) ;
  printf(" cet ensemble est identifie par la cle unique : %d\n" , (key_t)KEY) ;

  arg.val = 1;
  // int semctl(int semid, int semnum, int cmd, arg...);
  semctl(semid, 0, SETVAL, arg == -1) ; /* mise à 1 du 1er sémaphore */
  val_sem = semctl(semid, 0, GETVAL, arg) ; /*lecture du 1er sémaphore */
  printf("la valeur du semaphore est : %d\n",val_sem) ;
  /* lecture du pid du processus qui a effectue la dernière opération */
  

  val_pid = semctl(semid,0,GETPID,arg) ;
  


  printf("la valeur du pid du processus qui a effectue la dernière opération est : %d,\n mon pid est :%d\n",val_pid,getpid());
  semctl(semid,0,IPC_RMID,0) /* destruction du semaphore */













  // Creation des processus
  p1 = mp.Process(target=processing, args=())
  p2 = mp.Process(target=processing, args=())

  // Lancement des processus
  p1.start()
  
  with sem :
    p2.start()
  
  // Recuperation des fils
  p1.join(); p2.join()



  struct sigaction prepaSignal; // Déclaration d'une structure sigaction pour la mise en place des gestionnaires
  
  prepaSignal.sa_handler=&redirect; // Remplissage de la structure avec l'adresse du gestionnaire (redirect)
  prepaSignal.sa_flags=0; // Mise a zero du champ sa_flags theoriquement ignoré
  sigemptyset(&prepaSignal.sa_mask); // On ne bloque pas de signaux spécifiques

  // Pour voir les différents signaux depuis un raccourci clavier utiliser : `stty -a`

  // Mise en place du gestionnaire pour gérer la redirection de SIGINT
  sigaction(SIGINT,&prepaSignal,0); // `CTRL+C`

  // Il faut le tuer avec un kill pid */
  while (1){
      printf("toto\t");
  }

  return 0;
}   

def processing():
  if (mp.current_process().name == "Process-1"):
    # instructions de Process-1
    sem.release()
  print(mp.current_process().name)
  # instructions
if __name__ == "__main__" :

