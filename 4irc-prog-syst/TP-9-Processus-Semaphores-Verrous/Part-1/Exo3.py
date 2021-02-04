# coding: utf8

# Imports
import multiprocessing as mp

sem = mp.Semaphore(0) # Initialisation à 0, seul le processus 1 va faire le release et le processus 2 va avoir besoin du semaphore.

# Fonctions
def processing():
	if (mp.current_process().name == "Process-1"):
		# instructions de Process-1
		sem.release()
	print(mp.current_process().name)
	# instructions
if __name__ == "__main__" :

	# Creation des processus
	p1 = mp.Process(target=processing, args=())
	p1.start()
	
	p2 = mp.Process(target=processing, args=())
	with sem :
		p2.start()
	# Recuperation des fils
	p1.join(); p2.join()

# Ilies BELDJILALI & Brice FOLLEAS
