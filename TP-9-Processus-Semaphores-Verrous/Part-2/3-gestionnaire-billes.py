# coding: utf-8
# BELDJILALI Ilies & FOLLÉAS Brice

# Imports
import multiprocessing as mp # Process, Value, Array
import os, time, math, random, sys, array  # Attention : différent des 'Array' des Process

#------------------------------------------------

Nb_process = 4
All_done = mp.Value('b',False)
Nb_max_billes = mp.Value('i', 10)
Nb_billes_dispo = mp.Value('i', Nb_max_billes.value)
Sem_billes = mp.Semaphore(Nb_max_billes.value)
Sem = mp.Lock()

def travailleur(k_billes, i):
    print('Le travailleur', i, 'commence.')
    print('Le nombre de billes dont j\'ai besoin : ', k_billes)
    demander(k_billes, i)
    try:
        time.sleep(0.1) # simulation travail
    finally:
        rendre(k_billes, i)
        print('Le travailleur', i, 'a terminé.')

def demander(k_billes, name):
    print(name, 'est dans demander')
    while True :
        with Sem:
            if (Nb_billes_dispo.value >= k_billes):
                i = 0
                while (i < k_billes):
                    Sem_billes.acquire()
                    i += 1
                Nb_billes_dispo.value = Nb_billes_dispo.value - k_billes
                break
        time.sleep(1)
    print('Nombre de billes dispo après avoir demandé', Nb_billes_dispo.value)

def rendre(k_billes, name):
    print(name, 'est dans rendre')
    i = 0
    while (i < k_billes):
        Sem_billes.release()
        i += 1
    Nb_billes_dispo.value = Nb_billes_dispo.value + k_billes
    print('Nombre de billes dispo', Nb_billes_dispo.value)

def controller(max_billes):
    while not All_done.value :
        if (Nb_billes_dispo.value < 0 or Nb_billes_dispo.value > max_billes):
            print('Il y a une erreur dans la gestion des billes.')
        time.sleep(1) # simulation contrôle

if __name__ == "__main__" :
        
    process_controller = mp.Process(target=controller, args=(Nb_max_billes.value,))
    process_controller.start()

    mes_process = [*range(Nb_process)]

    for i in range(Nb_process): # Lancer Nb_process processus
        mes_process[i] = mp.Process(target=travailleur, args=(random.randint(1,10),i))
        mes_process[i].start()
   
    for i in range(Nb_process): 
        mes_process[i].join()
    All_done.value = True
 
    process_controller.join()
    print("Bravo, c'est fini !")
    