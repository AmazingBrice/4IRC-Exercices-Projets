# FOLLEAS Brice - Calcul de la somme d'un tableau (concurrentielle)

# Imports
import os, array, sys
import multiprocessing as mp # pour Value, Pipe

# La fonction des fils
def compilate(num_process, srcfile):
	# table, debut, fin_inclue, entree_pere_Write, entree_fils_Read) :
	print("Je suis le fils num ", num_process, "et je compile ", srcfile)
	cmd = ["gcc", "-c", srcfile];
	p = os.popen(cmd);
	p.wait();  

if __name__ == "__main__" :
	n = len(sys.argv)
	# sys.argv
	# tableau = [i for i in range(taille)]
	for i in range(n)
		if not (os.fork()): # Je suis le fils
			compilate(i, sys.argv[i])
			os._exit(0)
		else: # Je suis le pere
		
			os.popen(["gcc", "-o", file])


	# Le fils revient pas ici
