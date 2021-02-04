# FOLLÉAS Brice - Calcul de PI par Arctg (concurentiell)

"""
Fonction d’un processus (1 travailleur) :
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−’
La tache de chaque Thread No i=1..k :
somme_locale = 0.0
verser dans la somme_locale l’aire des battons propres à ce processus
Avant de finir, verser la somme_locale dans la Somme_globale
Le travail du chef (main) :
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Définir le nombre N de bâtons : soit 10^6
Définir le nombre k de processus : soit 5
Somme globale = 0.0 (le résultat des calculs)
Créer les k processus et assigner à chacun un No (1..k) et sa "part"
Les lancer (conséquence de la création) = faire appeler la fonction ci−dessus
Attendre qu’ils finissent tous
Récupérer et afficher la Somme_globale
"""

import multiprocessing as mp
import random, time, os

# Code du processus fils
def calculer_une_part_de_PI_arc_tangente(my_num, nb_iter, nb_processus, integrale):
	ma_part_de_pi = 0.0
	for i in range(0,nb_iter,nb_processus):
		ma_part_de_pi += 4/(1+ ((i+0.5)/nb_iter) **	2) 
	# Je verse ma part dans la variable partagée
	integrale.value += (1/nb_iter) * ma_part_de_pi

if __name__ == "__main__" :
	nb_processus=8 # Nombre travailleurs
	nb_total_iteration = 1000000 # Nombre total d’essais pour l’estimation
	integrale = mp.Value(’f’, 0.0)
	
	start_time = time.time()
	tab_pid=[0 for i in range(nb_processus)]
	for i in range(nb_processus) :
		tab_pid[i]=os.fork()
		if tab_pid[i] == 0 :
			calculer_une_part_de_PI_arc_tangente(i+1, nb_total_iteration // nb_processus,nb_processus,integrale)
			os._exit(0)
		else : pass # le père
	
	for i in range(nb_processus) : _, _ = os.waitpid(tab_pid[i], 0) # OU os.wait()

	print("Valeur estimée Pi par la méthode Tangente : ", integrale.value)
	print("Temps d’execution : ", time.time() − start_time)
