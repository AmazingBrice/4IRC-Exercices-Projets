# FOLLÉAS Brice - Calcul de la somme d'un tableau (séquentielle)

# Imports
import os
import multiprocessing as mp # pour Value

def somme(num_process, Val, tableau):
	print("Je suis le fils num ", num_process, "et je fais la somme du tableau ", tableau )
	S_local=0
	for i in range(len(tableau)):
		S_local += tableau[i]
		Val.value += S_local # Val est la Variable partagée par le multiprocessing