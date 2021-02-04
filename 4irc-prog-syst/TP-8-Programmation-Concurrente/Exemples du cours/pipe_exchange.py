# FOLLEAS Brice - Calcul de la somme d'un tableau (concurrentielle)

# Imports
import os, array
import multiprocessing as mp # pour Value, Pipe

# La fonction des fils
def somme(num_process, table, debut, fin_inclue, entree_pere_Write, entree_fils_Read) :
	print("Je suis le fils num ", num_process, "et je fais la somme du tableau ", tableau[debut: fin_inclue] )
	S_local = 0
	for i in range(debut, fin_inclue) :
		S_local += tableau[i]
	entree_pere_Write.send(S_local) # Chaque fils transmet son resultat

if __name__ == "__main__" :
	taille = 3
	tableau = [i for i in range(taille)]
	entree_pere_Write, entree_fils_Read = mp.Pipe() # W/R des pipes
	id_fils1 = os.fork()
	if not id_fils1 : # Je suis le fils1
		somme(1, tableau, 0, taille // 2, entree_pere_Write, entree_fils_Read)
		os._exit(0)
	else : # Le pere
		id_fils2 = os.fork()
		if not id_fils2 : # Je suis le fils2
			somme(2, tableau, taille // 2, taille,entree_pere_Write, entree_fils_Read) # taille//2 car on commence a 0
			os._exit(0)


	# Le fils revient pas ici
	moitie1 = entree_fils_Read.recv() # Le pere recoit les resultats
	moitie2 = entree_fils_Read.recv()
	somme = moitie2 + moitie1
	#os.wait() NO MORE NEEDED ! why ?
	print("La somme totale du tableau est :", somme)
	print("Le pere verifie que la somme doit etre :", sum(tableau)) # Verification
