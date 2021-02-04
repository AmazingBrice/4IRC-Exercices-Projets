# FOLLEAS Brice - Calcul de la somme d'un tableau (concurrentielle)

# Imports
import os
import multiprocessing as mp # pour Value

if __name__ == "__main__" :

n = 11
tableau = [1 for i in range(n)]
somme_totale = mp.Value(’i’, 0)
id_fils = os.fork()

if not id_fils : # Je suis le fils
somme(1, somme_totale, tableau[:n // 2])
else : # Le père fais l’autre moitié
somme(0, somme_totale, tableau[n // 2:])
os.wait()
print("La somme totale du tableau est ", somme_totale.value)
"""
TRACE :
Je suis le fils num 0 et je fais la somme du tableau [1, 1, 1, 1, 1, 1]
Je suis le fils num 1 et je fais la somme du tableau [1, 1, 1, 1, 1]
La somme totale du tableau est 11
"""