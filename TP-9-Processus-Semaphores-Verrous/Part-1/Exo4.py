# coding: utf8

# Imports
import multiprocessing as mp
import random, time

# Sémaphore pour l'écriture dans les queues (pas obligatoire puisque queues différentes donc ressources différentes c'est juste pour l'affichage des print)
sem = mp.Semaphore() 
# Sémaphore pour la lecture de la ressource et ainsi C1 attends la fin de l'exécution de C2
sem2 = mp.Semaphore()

# Fonctions
def inputQ(process_name, q):
	with sem:
		print("Je suis", process_name) # Plus pratique que d'utiliser mp.current_process().name

		# q.put([random.randint(0,10)])
		z =random.randint(0,10)
		q.put([z])
		print("J'ecris :", z)
	
def getQ(process_name, q):
	print("Je suis", process_name, "et je lis", q.get())
	
if __name__ == "__main__" :

	print("Saisir le nombre de messages à mettre dans la queue :")
	x = input()
	# Creation des queues
	q1 = mp.Queue()
	q2 = mp.Queue()

	i = 0
	while(i < x): # Ecrase les anciens processus à la nouvelle itération
		# Creation des processus P
		p1 = mp.Process(target=inputQ, args=("p1", q1,))	
		p2 = mp.Process(target=inputQ, args=("p2", q2,))

		p1.start()
		p2.start()

		# Recuperation des processus P
		p1.join()
		p2.join()

		i = i + 1

	print("Fin processus écriture.")
	
	i = 0
	while(i < x):
		print("Iteration", i)
		# Creation des processus C
		c1 = mp.Process(target=getQ, args=("c1", q1,))
		c2 = mp.Process(target=getQ, args=("c2", q2,))
		with sem2:
			c1.start()
		with sem2:
			c2.start()
			# Recuperation des processus C
		c1.join(); c2.join()
		i = i +1

	print("Fin processus lecture.")

# Ilies BELDJILALI & Brice FOLLEAS
