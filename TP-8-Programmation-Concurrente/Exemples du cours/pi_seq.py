# FOLLÉAS Brice - Calcul de PI par Arctg (séquentielle)

# Imports
import random, time, math

def arc_tangente(n):
	pi = 0
	for i in range(n):
		pi += 4/(1+ ((i+0.5)/n) ** 2)
	return (1/n) * pi

if __name__ == "__main__" :

	nb_total_iteration = 1000000 # Nombre d’essai pour l’estimation
	start_time = time.time() # Comparaison du temps d'execution avec le programme concurentielle d'où l'affichage du temps
	
	result = arc_tangente(nb_total_iteration)
	print("Valeur estimée Pi par la méthode Tangente : ", result)
	print("Temps d’execution séquentielle : ", time.time() - start_time)